from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse

from menu.models import Food_Item
# Create your views here.


def food_order(request):
    """ Order page view """

    return render(request, 'food_order/order_items.html')


def add_to_order(request, item_id):
    """ Add a quantity of the specified product to the food order """

    print(item_id)
    # food_item = get_object_or_404(Food_Item, pk=item_id)
    redirect_url = request.POST.get('redirect_url')

    order = request.session.get('food_order', {})
    print(order.keys())

    if item_id in list(order.keys()):
        order[item_id] += 1
    else:
        order[item_id] = 1

    request.session['food_order'] = order
    print('order is : ')
    print(order)

    return redirect(redirect_url)


def remove_from_order(request, item_id):
    """ Removes item from order effectively taking that item's quantity
    to zero. """

    order = request.session.get('food_order', {})
    order.pop(item_id)
    request.session['food_order'] = order
    print(request.session.get('food_order'))

    return HttpResponse(status=200)


def edit_order(request, item_id):
    """ Edits quantity of the specified product to the food order """

    order = request.session.get('food_order', {})
    order[item_id] = int(request.POST.get('qtyVal'))
    request.session['food_order'] = order
    print(request.session.get('food_order'))

    return HttpResponse(status=204)