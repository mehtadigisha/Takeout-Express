from django.shortcuts import render,get_object_or_404 ,redirect
# to import whole page we use render.
from .models import Menu , CartItem
from django.contrib.auth.decorators import login_required

# Create your views here.

def menu(request):
    searchTerm=request.GET.get('searchMenu')
    if not searchTerm:
        menus=Menu.objects.all()
    else:
        menus=Menu.objects.filter(item__icontains=searchTerm)
    return render(request,'menu.html',{'Menu':searchTerm,'menu':menus})

def detail(request,menu_id):
     menu=get_object_or_404(Menu,pk=menu_id)  
     return render(request,'detail.html',{'menu':menu})

@login_required
def add_to_cart(request, menu_id):
    product = Menu.objects.get(id=menu_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('menu')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)

    total=0

    for cart_item in cart_items:
        cart_item.total = cart_item.product.price * cart_item.quantity
        total+=cart_item.total

    return render(request, 'view_cart.html', {'cart_items': cart_items,'total':total})

@login_required
def delete_from_cart(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(id=cart_item_id, user=request.user)
        cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    return redirect('view_cart')

def order(request):
    cart_items = CartItem.objects.filter(user=request.user)

    total=0

    for cart_item in cart_items:
        cart_item.total = cart_item.product.price * cart_item.quantity
        total+=cart_item.total
    return render(request,'order.html',{'total':total})