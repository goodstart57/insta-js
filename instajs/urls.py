from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('accounts/', include('accounts.urls')),
]

# static(통과시키고자 하는 url, 실제 저장 장소)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
