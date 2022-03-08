from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('billing/', include("billing.urls", namespace="billing")),
    path('blog/', include("blog.urls", namespace="blog")),
]

if settings.DEBUG:
    urlpatterns = [
        path('admin/', admin.site.urls),
    ] + urlpatterns

# adding randomness to admin URL when in PROD
# to avoid brute force attacks
if not settings.DEBUG:
    urlpatterns = [
        path('77randomAdmin@33/', admin.site.urls),
    ] + urlpatterns