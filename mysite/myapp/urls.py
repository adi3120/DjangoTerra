from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
	 path('aws/', views.aws, name='aws'),
	 path('azure/', views.azure, name='azure'),
	 path('gcp/', views.gcp, name='gcp'),
	 path('vmware/', views.vmware, name='vmware'),
]