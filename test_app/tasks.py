from pydantic import BaseModel
from openai import OpenAI
from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist
import openai
from test_app.models import Article
import environ

env = environ.Env()
environ.Env.read_env()

class SummaryResponse(BaseModel):
    summary: str

client = OpenAI(api_key=env("OPENAI_API_KEY"))

@shared_task(bind=True, default_retry_delay=30, max_retries=5)
def ai_summery(self, text: str, id: int):
    try:
        response = client.chat.completions.create( 
            model="gpt-4",
            messages=[
                {"role": "system", "content": "شما یک ابزار خلاصه‌کننده متن هستید."},
                {"role": "user", "content": f"لطفاً این متن را خلاصه کن: {text}"}
            ],
            temperature=0.0,
            max_tokens=150,
            timeout=30  
        )

        summary = response.choices[0].message.content.strip()
        summary_response = SummaryResponse(summary=summary)

        try:
            article = Article.objects.get(id=id)
            article.summary = summary_response.summary
            article.save()
        except ObjectDoesNotExist:
            raise f"Article with id {id} not found."

    except openai.APIConnectionError as e:  
        print(f"Error connecting to OpenAI: {str(e)}")
        raise self.retry(exc=e)
    except Exception as e:
        raise self.retry(exc=e, max_retries=1)
