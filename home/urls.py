from django.urls import path, include
from .views import home,service_version

app_name = 'home'

urlpatterns = [
    path('',home,name='home1'),
    path('version',service_version,name='service_version'),
]
