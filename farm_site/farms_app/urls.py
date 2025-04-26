from django.urls import path
from farms_app import views




app_name = 'farms_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('our-product/', views.our_product, name='our-product'),
    path('shop/', views.shop, name='shop'),
    path('servces/', views.services, name='services'),
]