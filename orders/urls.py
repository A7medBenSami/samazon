from django.urls import re_path
from . import views


app_name = 'orders'

urlpatterns = [
	re_path(r'^create/$',views.order_create,name='order_create'),
	re_path('admin/order/<order_id>/pdf/',views.admin_order_pdf,name='admin_order_pdf')
]