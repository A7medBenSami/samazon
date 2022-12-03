from django.shortcuts import render

from .models import ShopCart



def shopcart(request):
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    items = 0
    for rs in shopcart:
        total += rs.variant.price * rs.quantity
        items = rs.quantity
    return {'shopcart': shopcart, 'total': total,'items':items}