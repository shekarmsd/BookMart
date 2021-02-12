from django.contrib import admin
from .models import *

# Register your models here.

class BookmartAdmin(admin.ModelAdmin):

	list_display = ('book_title', 'book_author', 'book_description', 'book_price', 'book_published')
	search_fields = ('book_title', 'book_author')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

class ContactAdmin(admin.ModelAdmin):

	list_display = ('name', 'email', 'subject', 'phone_number', 'message', 'created_date')
	search_fields = ('name', 'email', 'phone_number')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	
class PaymentAdmin(admin.ModelAdmin):
     
    list_display=('card_number','expire_date','cvv')

	

admin.site.register(Bookmart, BookmartAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(CustomerOrders)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(CustomerBooks)
admin.site.register(OrderPackage)