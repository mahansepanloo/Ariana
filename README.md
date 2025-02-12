# Project Name

## Overview
This Django project manages articles and knowledge bases, incorporating advanced text summarization using OpenAI's API. It features two primary models, `Article` and `Knowledge`, with a many-to-many relationship between them. CRUD operations are handled through Django views, while Celery is utilized for asynchronous tasks, particularly summarizing article descriptions.

## Features
- **Article Management:** Create, read, update, and delete articles.
- **Knowledge Base:** Manage knowledge entries with relationships to multiple articles.
- **Automated Summarization:** Use Celery and OpenAI to generate summaries of article descriptions.

## Technologies Used
- **Django:** Web framework for building the application.
- **Celery:** Task queue for handling asynchronous operations.
- **OpenAI API:** For summarizing article descriptions.
- **rabbitmql:** Message broker for Celery.

## Setup Instructions

### Prerequisites
- Python 3.x
- Redis Server
- Virtual Environment (optional but recommended)

### Installation
1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create and Activate Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

5. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```



### Usage
- Access the application at `http://127.0.0.1:8000/`.
- Use the provided views to perform CRUD operations on `Article` and `Knowledge`.
- When a new article is created or updated, Celery will handle the summarization of the `description` field asynchronously.

## Project Structure
```
<project_name>/
|│-- <project_name>/          # Django project files
|│-- app/                   # Django app with models, views, and tasks
|│   |│-- models.py        # Contains Article and Knowledge models
|│   |│-- views.py         # CRUD operations for the models
|│   |│-- tasks.py         # Celery tasks for summarization
|│-- requirements.txt       # List of dependencies
|│-- manage.py              # Django management script
```

## Example Models
```python
# models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Knowledge(models.Model):
    name = models.CharField(max_length=255)
    articles = models.ManyToManyField(Article)
```



## Contributing
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, please contact [Your Name] at [Your Email].

