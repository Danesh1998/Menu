from django.contrib import admin
from django.urls import path
from . import views 
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index, name="councilhome"),
    path("home/",views.home, name="home"),
    path("index2/",views.sign, name="index2"),
    path('index3/',views.index3, name="index3"),
    path('complnts/<int:pk>',views.comp, name="complnts"),
    path('index4/',views.compa,name="table"),
    # path('',views.basepage,name="base"),
    path('login/',views.login,name="login"),
    path('index5/',views.error,name="error"),
    path('save-photo/', views.save_photo, name='save_photo'),
    path("main/", views.main, name="mainpage"),
    path('index6/',views.boot, name="index6"),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)