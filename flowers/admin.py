from django.contrib import admin

from .models import Seller, SellerReview, LotReview, Lot, Shade, Deal, Flower, Customer


admin.site.register(Seller)
admin.site.register(SellerReview)
admin.site.register(LotReview)
admin.site.register(Lot)
admin.site.register(Shade)
admin.site.register(Deal)
admin.site.register(Flower)
admin.site.register(Customer)
