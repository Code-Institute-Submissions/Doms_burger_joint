from django.shortcuts import render


def index(request):
    """ Main index page view """
    return render(request, 'order/order.html')
