from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from test_app.models import Article, Knowledge
from django.contrib.auth.models import User

#base serializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id')

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ["title" , "status", "created_by"]
        read_only_fields = ["id",'created_by', 'updated_at', 'created_at' ]

#end


class ArticleCreateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ["id",'created_by', 'updated_at', 'created_at', "summary" ]


class ArticleListSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Article
        fields = ("id", "title", "status", "created_by")
        read_only_fields = ["id",'created_by', 'updated_at', 'created_at' ]


class ArticleRetrieveSerializer(ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ["id",'created_by', 'updated_at', 'created_at' ]


class KnowledgeCreateSerializer(ModelSerializer):
    class Meta:
        model = Knowledge
        fields = '__all__'
        read_only_fields = ["id",'created_by', 'updated_at', 'created_at' ]

class  KnowledgeListAdminSerializer(ModelSerializer):
    created_by = UserSerializer()
    articles = ArticleSerializer(many=True)
    class Meta:
        model = Knowledge
        fields = ("id", "title", "status", "created_by", "articles")
        read_only_fields = ["id",'created_by', 'updated_at', 'created_at' ]

class KnowledgeListSerializer(ModelSerializer):
    created_by = UserSerializer()
    articles = serializers.SerializerMethodField()
    class Meta:
        model = Knowledge
        fields = ['id', 'title', 'status', 'articles', 'created_at', 'created_by']
        
    def get_articles(self, obj):
        filtered_articles = obj.articles.filter(status='p')
        return ArticleSerializer(filtered_articles, many=True).data


class KnowledgeRetrieveSerializer(ModelSerializer):
    created_by = UserSerializer()
    articles = ArticleSerializer(many=True)
    class Meta:
        model = Knowledge
        fields = '__all__'
        read_only_fields = ["id",'created_by', 'updated_at', 'created_at' ]





