from django.db import models
from test_app.enums import STATUS_CHOICES
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='articles'
    )
    summary = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        description_changed = False

        if self.pk:
            previous = Article.objects.filter(pk=self.pk).only('description').first()
            if previous and previous.description != self.description:
                description_changed = True
        else:
            description_changed = True

        super().save(*args, **kwargs)

        if description_changed:
            from test_app.tasks import ai_summery
            ai_summery.delay(self.description, self.id)


class Knowledge(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    articles = models.ManyToManyField(
        Article, 
        related_name='knowledges'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='knowledges'
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Knowledge'
        verbose_name_plural = 'Knowledges'

    def __str__(self):
        return self.title
