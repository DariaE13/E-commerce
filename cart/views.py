from django.shortcuts import redirect,render,get_object_or_404
from store.models import Product
from django.views.decorators.http import require_POST
from cart.cart import Cart
from cart.forms import CartAddPrroductForm

@require_POST
def cart_add(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddPrroductForm(request.POST)
    if form.is_valit(): #Проверяет корректные ли данные
        cData = form.cleaaner_data
        cart.add(product=product,quantity=cData['quantity'],update_quantity=cData['update'])
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request) #Экзкмпляр корзины 
    for item in cart:
        item['update_quantity_form'] = CartAddPrroductForm(
            initial = {'quantity':item['quantity'],'update':True}
        )
    return render(request,'cart/detail.html',{'cart':cart})
