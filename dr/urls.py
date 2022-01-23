from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import download

urlpatterns=[
    path('download.php', download, name='download')
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)