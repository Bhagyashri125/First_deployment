from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu',views.menu,name='menu'),
    path('contact',views.contact,name='contact'),
    path('order_pickup',views.order_pickup,name='order_pickup'),
    path('about',views.about,name='about'),
    path('<str:section>',views.food_items,name='food_items'),
    path('menu/form_upload',views.form_upload,name='form_upload'),
]
