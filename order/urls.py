from django.urls import path, re_path
from . import views


urlpatterns = [
    path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),
    path('shopcart/', views.shopcart, name='shopcart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    path('orderproduct/', views.orderproduct, name='orderproduct'),
    path('pay_success', views.pay_success, name='pay_success'),
    path('pay_cancel', views.pay_cancel, name='pay_cancel'),
    path('checkout_session/',views.checkout_session,name='checkout_session'),
    path('webhook/stripe', views.my_webhook_view, name='webhook-stripe'),



    #path('admin/order/<order_id>/pdf/',views.admin_order_pdf,name='admin_order_pdf'),


]

