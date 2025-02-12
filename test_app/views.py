from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from test_app.models import Article,Knowledge
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from test_app.serializer import (ArticleCreateSerializer, ArticleListSerializer, ArticleRetrieveSerializer, KnowledgeCreateSerializer, 
                                 KnowledgeListSerializer,  KnowledgeRetrieveSerializer, KnowledgeListAdminSerializer )
from rest_framework.response import Response

class KnowledgeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeCreateSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = ["title"]

    def get_serializer(self, *args, **kwargs):
        if self.action == "list":
            if self.request.user.is_staff:
                return KnowledgeListAdminSerializer(*args, **kwargs)
            return KnowledgeListSerializer(*args, **kwargs)
        if self.action == "retrieve":
            return KnowledgeRetrieveSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Knowledge.objects.all()
        return Knowledge.objects.filter(status ="p")
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(instance)
        data = serializer.data

        if not request.user.is_staff:
            data['articles'] = [article for article in data['articles'] if article['status'] == 'p']

        return Response(data)
    


class ArticleViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = ["title"]

    def get_serializer(self, *args, **kwargs):
        if self.action == "list":
            return ArticleListSerializer(*args, **kwargs)
        if self.action == "retrieve":
            return ArticleRetrieveSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)
        
    def get_queryset(self):
        if self.request.user.is_staff:
            return Article.objects.all()
        else:
            return Article.objects.filter(status ="p")
    
    def perform_create(self, serializer):
        data = serializer.save(created_by=self.request.user)
