from django.urls import path
from . import views

urlpatterns = [
    #views.index：使用vews.py裡面定義的function:index()
    #name='index':.html的樣本template檔裡面，要寫href超連結語法的話，就會用到
    path('', views.index, name='index'),
]