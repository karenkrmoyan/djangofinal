from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),
    # Store app
    path("", include("store.urls")),
    # Cart app
    path("cart/", include("cart.urls")),
    # Account app
    path("account/", include("account.urls")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)