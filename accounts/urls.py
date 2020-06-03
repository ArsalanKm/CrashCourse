from django.urls import path

from accounts import views

urlpatterns = [
    path('', views.home),
    path('customers/<str:pk>', views.customer),
    path('products/', views.products),
]
