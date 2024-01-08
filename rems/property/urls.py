from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_list, name='home'),
    path('<int:pk>', views.property_retrieve),
    path('add-property/', views.property_create, name='add-property'),
    path('success/', views.success_page_view, name='success_page'),
]