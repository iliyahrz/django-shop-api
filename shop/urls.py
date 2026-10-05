from django.contrib import admin
from django.urls import path
from landing.views import index, contact
from products.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('contact', contact, name="contact"),
    path('shop', ProductListAPIView.as_view(), name="shop"),
    path('product/<slug:slug>/', ProductAPIView.as_view(), name='product-item'),     
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)