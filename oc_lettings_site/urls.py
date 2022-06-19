from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include(('app_lettings.urls', 'lettings'), namespace='lettings')),
    path('profiles/', include(('app_profiles.urls', 'profiles'), namespace='profiles')),
    path('admin/', admin.site.urls),
]
