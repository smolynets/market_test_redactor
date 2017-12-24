
from cart.cart import Cart
#from .utils import get_lang




def cart(request):
    return {'cart': Cart(request)}






#select language
#def lang_processor(request):
	#return {'PK': get_lang(request)}




