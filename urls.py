from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import sites.urls as main_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(main_urls.urlpatterns))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
