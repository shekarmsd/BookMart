from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone

# Create your models here.

class Bookmart(models.Model):
	CATEGORY = (
				('Fiction', 'Fiction'),
				('Nonfiction', 'Nonfiction'),
			)

	book_publisher = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	book_category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	book_title = models.CharField(max_length=200)
	book_author = models.CharField(max_length=200)
	book_description = models.CharField(max_length=100, null=True)
	book_price = models.FloatField()
	book_image = models.ImageField(null=True, blank=True)
	book_pdf = models.FileField(null=True, blank=True)
	book_published = models.DateTimeField(auto_now_add=True, null=True)

	
	def __str__(self):
		return self.book_title

	@property
	def imageURL(self):
		try:
			url = self.book_image.url
		except:
			url = ''
		return url
	

class Order(models.Model):
	customer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	complete = models.BooleanField(default=False, null=True, blank=False)
	package = models.IntegerField(default=0, null=True, blank=True)
	date_ordred = models.DateField(auto_now_add=True)
	end_date = models.DateField(default = datetime.now())
	transaction_id = models.CharField(max_length=200, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total
	

class OrderItem(models.Model):
	books = models.ForeignKey(Bookmart, on_delete=models.CASCADE, blank=True, null=True)
	order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_ordred = models.DateField(auto_now_add=True)
	end_date = models.DateField(default = datetime.now())


	@property
	def get_total(self):
		total = self.books.book_price * self.quantity
		return total
	

class Payment(models.Model):
	card_number = models.CharField(max_length=200, null=True)
	expire_date = models.DateField(auto_now_add=True, null=True)
	cvv = models.CharField(max_length=200, null=True)
	date_added = models.DateTimeField(auto_now_add=True)


class CustomerOrders(models.Model):
	customer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE, blank=True, null=True)
	quantity = models.CharField(max_length=200, null=True)
	package = models.IntegerField(default=0, null=True, blank=True)
	total_amount = models.IntegerField(default=0, null=True, blank=True)
	date_ordred = models.DateField(auto_now_add=True)
	end_date = models.DateField(default = datetime.now())

class CustomerBooks(models.Model):
	book = models.ForeignKey(Bookmart, on_delete=models.CASCADE, blank=True, null=True)
	customer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	order_id = models.ForeignKey(CustomerOrders, on_delete=models.CASCADE, blank=True, null=True)

class OrderPackage(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
	package = models.IntegerField(default=0, null=True, blank=True)


class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	subject = models.CharField(max_length=600)
	phone_number = models.CharField(max_length=100)
	message = models.TextField(max_length=700)
	created_date = models.DateTimeField(auto_now_add=True, null=True)
	
	def __str__(self):
		return self.name






# class Customer(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
# 	name = models.CharField(max_length=200, null=True, blank=True)
# 	email = models.CharField(max_length=200, null=True, blank=True)

# 	def __str__(self):
# 		return str(self.user)


# def create_customer(sender, instance, created, **kwargs):

# 	if created:
# 		Customer.objects.create(user=instance)
# 		print('profile created!')

# post_save.connect(create_customer, sender=User)

# def update_customer(sender, instance, created, **kwargs):

# 	if created == False:
# 		instance.customer.save()
# 		print('profile updated!')

# post_save.connect(update_customer , sender=User)


# class Product(models.Model):
# 	name = models.CharField(max_length=200, null=True)
# 	price = models.FloatField()
# 	digital = models.BooleanField(default=False, null=True, blank=True)
# 	# image = models.ImageField(null=True, blank=True)

# 	def __str__(self):
# 		return self.name