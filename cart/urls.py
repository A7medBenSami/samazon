from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
	path('', views.cart_detail, name='cart_detail'),
	path('add/<int:id>/<slug:slug>', views.cart_add, name='cart_add'),
	path('remove/<int:id>/<slug:slug>', views.cart_remove, name='cart_remove'),
	#path('add_qty/<int:id>', views.add_qty, name='add_qty'),
	#path('remove/<slug:slug>', views.cart_remove, name='cart_remove'),
]
