from .cart import Cart

# create context processor so cart can work on all pages
def cart(request):
    # return default data from Cart
    return{'cart': Cart(request)}