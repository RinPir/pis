from django.contrib import admin
from django.urls import path
from flatpages import views

urlpatterns = [
    path('', views.home, name='home'),  # главная страница
    path('hello/', views.home, name='hello'),  # задание: второй адрес с тем же текстом
    path('admin/', admin.site.urls),  # административная панель
]