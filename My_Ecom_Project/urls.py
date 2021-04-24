
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.static import serve

from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('App_Shop.urls')),
   path('account/', include('App_Login.urls')),
   path('shop/', include('App_Order.urls')),
   path('payment/', include('App_Payment.urls')),

   url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
