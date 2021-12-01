from django.urls import path

from .views import *
from . import views

app_name = 'locdata'

urlpatterns = [
    #path('', HomePageView.as_view(), name='home'),
    path('', views.index, name='index'),
    path('<int:locdata_id>', views.detail, name='detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contactTracing/', views.contactTracing, name='Contact Tracing'),
    path('assetManagement/', views.assetManagement, name='Asset Management'),
    path('changePermissions/', views.changePermissions, name='Change Permissions'),
    path('bTest/', views.homepage, name='Home')
]
