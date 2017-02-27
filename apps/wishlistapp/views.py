from django.shortcuts import render, redirect
from ..loginapp.models import Registration
from .models import Item, Wishlist
from django.contrib import messages
def index(request):

    if 'user' not in request.session:
        return redirect('Login:my_index')
    user = Registration.objects.get(id = request.session['user'])
    context = {
    'user': user,
    'wishlist': Wishlist.objects.all().exclude(my_wish_list = False),
    'otherwishlist':Wishlist.objects.all().exclude(user_id = request.session['user'])

    }
    return render(request, "wishlistapp/success.html", context)
def create(request):
    print "got to the create"

    return render(request, 'wishlistapp/create.html')

def this_product(request):
    Item_Output = Item.objects.add_item(request.POST)
    if Item_Output['outcome'] == "error":
        for key, value in Item_Output.items():
            messages.error(request, value)
        return redirect("wishitems:create")
    else:
        User_Output = Wishlist.objects.add_wishlist(Item_Output['item'], request.session['user'])
        return redirect("wishitems:show", User_Output['item'])

def show(request, id):
    name = Item.objects.get(id = id)
    context = {"item": Item.objects.get(id = id),
    "users": Registration.objects.filter(UserofWishlist__item_id__name = name.name)
    }
    return render(request, 'wishlistapp/show.html',context)
def remove(request, id):
    Wishlist.objects.get(id = id).delete()
    return redirect("First:my_index")
def delete(request, id):

    Item.objects.get(id = id).delete()
    return redirect("First:my_index")
def add(request, id ):
    Outcome = Wishlist.objects.direct_wishlist(id, request.session['user'])


    return redirect("First:my_index")
