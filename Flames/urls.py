from django.contrib import admin
from django.urls import path
from run import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home",views.home,name="home"),
    path("love_test",views.love_test,name="love")
]
