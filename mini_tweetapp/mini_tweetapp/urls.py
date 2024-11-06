from django.contrib import admin
from django.urls import path, include
from tweets.views import home 

urlpatterns = [
    path('', include('tweets.urls')),
    path('', home, name='home'), 
    path('admin/', admin.site.urls),
    path('api/', include('tweets.urls')),
]
