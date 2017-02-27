from __future__ import unicode_literals

from django.db import models
from ..loginapp.models import Registration

class Manager(models.Manager):
    def add_item(self, DataPost):
        #adding item to item table here first
        Response = {}
        Response['outcome'] = "success"
        if len(DataPost['item_name'])< 3:
            Response['outcome'] = "error"
            Response['response1'] = "need to be greater than 3"
        if DataPost['item_name'] == '':
            Response['outcome'] = "error"
            Response['response1'] = "no empty entries"

        if Response['outcome'] == "error":

            return Response
        else:
            item_id = Item.objects.create(name = DataPost['item_name'])
            Response['item'] = item_id.id
            Response['outcome'] = "success"
            return Response
    def add_wishlist(self, item, user):
        #adding item ID & User ID to wishlist next
        Response = {}
        this_wishlist = Wishlist.objects.create(user_id = Registration.objects.get(id = user), my_wish_list = True )
        wishlist = Wishlist.objects.get(id = this_wishlist.id)
        user_id = Registration.objects.get(id = user)

        item_id = Item.objects.get(id = item)
        wishlist.item_id.add(item_id)

        Response['user'] = user_id.id
        Response['item'] = item_id.id
        return Response
    def direct_wishlist(self, item, user):
        this_wishlist = Wishlist.objects.create(user_id = Registration.objects.get(id = user), my_wish_list = True )
        wishlist = Wishlist.objects.get(id = this_wishlist.id)
        user_id = Registration.objects.get(id = user)
        item_id = Item.objects.get(id = item)
        wishlist.item_id.add(item_id)
class Item(models.Model):
    name = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = Manager()

class Wishlist(models.Model):
    user_id = models.ForeignKey(Registration, related_name = "UserofWishlist")
    item_id = models.ManyToManyField(Item, related_name = "ItemsonWishlist")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    my_wish_list = models.BooleanField(default = False)
    objects = Manager()
