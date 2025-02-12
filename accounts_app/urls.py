from django.urls import path
from . import views



app_name = 'auth-token'

urlpatterns = [
    path('login/', views.Login.as_view(), name='token_obtain_pair'),
    path('refresh/', views.Refresh.as_view(), name='token_refresh'),
]