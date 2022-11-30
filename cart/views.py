from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm
from django.conf import settings




@require_POST
def cart_add(request, slug,id):
	cart = Cart(request)
	product=Product.objects.get(pk=id)
	form = CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(
                    product=product,
                    quantity=cd['quantity'],
                    update_quantity=cd['update']
                )
	return redirect('cart:cart_detail')

def cart_remove(request, slug):
	cart = Cart(request)
	product=Product.objects.get(pk=id)
	cart.remove(product)
	return redirect('cart:cart_detail')
	
def cart_detail(request):
	cart = Cart(request)
	for item in cart:
		item['update_quantity_form'] = CartAddProductForm(
			initial={'quantity': item['quantity'], 'update': True})
	coupon_apply_form = CouponApplyForm()
	context = {
		'cart': cart,
		'coupon_apply_form': coupon_apply_form
	}
	return render(request, 'cart/detail.html', context)








    
    
	
	




