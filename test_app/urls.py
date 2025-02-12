from django.urls import path
from test_app.views import ArticleViewSet, KnowledgeViewSet
from rest_framework.routers import DefaultRouter
app_name = 'test_app'


router = DefaultRouter()
router.register(r"article", ArticleViewSet)
router.register(r"knowledge", KnowledgeViewSet)

urlpatterns = [
] + router.urls