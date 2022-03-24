
from django.contrib import admin
from django.urls import path, include

import sites.urls as main_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(main_urls.urlpatterns))
]
