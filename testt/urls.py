from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('test_app.urls')),
    path('accounts/', include('accounts_app.urls')),
]



from django.contrib import admin
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('accounts_app.urls', namespace="auth-token")),
    path('api/', include('test_app.urls', namespace="test_app")),


    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)