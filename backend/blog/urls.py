from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
     path('', TemplateView.as_view(template_name='build/index.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
