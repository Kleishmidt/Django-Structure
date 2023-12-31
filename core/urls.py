from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core import settings
from core.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.api.urls', namespace='api'), name='api'),
]
urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
