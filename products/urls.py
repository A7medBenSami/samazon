from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('<int:id>/<slug:slug>', views.product, name='product'),
    path('ajaxcolor/', views.ajaxcolor, name='ajaxcolor'),
    #path('category/<int:id>/<slug:slug>/', views.category_products,name='category_products'),
]
