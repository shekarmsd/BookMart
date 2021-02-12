from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
import csv
from datetime import datetime, date
from django.core.mail import send_mail

from datetime import date, timedelta
from django.utils import timezone


from django.contrib.auth.decorators import login_required
# from .decorators import allowed_users

from .models import *
from .forms import CreateUserForm, BookUploadForm, ContactForm
from .filters import BookFilter

# Create your views here.
# @unauthenticated_user
def registerPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			form.save()
			print(email)
			send_mail(
            'Welcome to Book Mart',
            'Welcome to Bookmart we are excited that you joned!    ',
            'thepictureperf@gmail.com',
            [email],
            fail_silently=False,
                                )
			messages.success(request, "Registration Successful! Please login now.")
			return redirect('main:login')

	context = {'form':form}
	return render(request, "main/register.html", context)


# @unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			admin=User.objects.get(username=username)

			if admin.is_staff==1:
				return redirect("main:dashboard")
			elif user is not None:
				login(request, user)
				return redirect("main:indexPage")
			else:
				messages.error(request, "Invalid username or password") 
		else:
			messages.error(request, "Invalid username or password")


	form = AuthenticationForm()
	context = {'form':form, "login": "active"}
	return render(request, 'main/login.html', context)



def logout_request(request):
	logout(request)
	messages.success(request, "Logged out successfully!")
	return redirect("main:login")


def aboutPage(request):
	context = {}
	return render(request, "main/about.html", context)

@login_required(login_url='main:login')
def categoryPage(request):

	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_total':0}
		cartItems = order['get_cart_items']

	books = Bookmart.objects.all()
	nonfiction = Bookmart.objects.all().filter(book_category='Nonfiction')
	fiction = Bookmart.objects.all().filter(book_category='Fiction')
	return render(request, "main/category.html", context={"nonfiction":nonfiction, "fiction":fiction, "books":books, "category":"active", 'cartItems':cartItems})


def contactPage(request):


	form = ContactForm()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Thank you for reachning us. We'll get back to you soon!")
			return redirect("main:contact")
		else:
			messages.info(request, "Something went wrong! please try later.")
			return redirect("main:contact")

	context = {'form':form, 'contact':'active'}
	return render(request, "main/contact.html", context)


@login_required(login_url='main:login')
def customerPage(request, id):


	user = User.objects.get(id=id)
	context = {'user':user, "customer": "active"}
	return render(request, "main/customer.html", context)


def indexPage(request):

	books = Bookmart.objects.all()
	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
		context = {'books':books, 'items':items, 'cartItems':cartItems, "index":"active"}
	else:
		context = {'books':books}
	return render(request, "main/index.html", context)


# @login_required(login_url='main:login')
# @allowed_users(allowed_roles=['admin'])
def dashboardPage(request):
	books = Bookmart.objects.all()	
	account = User.objects.all()
	order = CustomerOrders.objects.all()

	total_books = books.count()
	total_users = account.count()
	total_orders = order.count()

	myFilter = BookFilter()

	form = Bookmart()	
	if request.method == 'POST':

		form.book_publisher = request.user
		form.book_title = request.POST['booktitle']
		form.book_author = request.POST['author']
		form.book_price = request.POST['price']
		form.book_description = request.POST['description']
		form.book_image = request.FILES['image']
		form.book_pdf = request.FILES['pdf']
		form.book_category = request.POST['category']

		form.save()
		messages.success(request, "New Book Added Successfully.")
			
	context = {'books':books, 'account':account, 'order':order, 'total_orders':total_orders, 'total_books':total_books, 'total_users':total_users, "dashboard": "active", 'myFilter':myFilter}
	return render(request, 'main/dashboard.html', context)


# @login_required(login_url='main:login')
def updateBook(request, id):
	books = Bookmart.objects.get(id=id)
	form = BookUploadForm(instance=books)

	if request.method == 'POST':
		form = BookUploadForm(request.POST, request.FILES, instance=books)
		if form.is_valid():
			form.save()
			messages.success(request, "Book Updated Successfully.")
			return redirect("main:dashboard")
		else:
			messages.info(request, "Something Went Wrong! Try Again Later.")
			return redirect("main:dashboard")

	context = {'form':form}
	return render(request, "main/update_book.html", context)


# @login_required(login_url='main:login')
def deleteBook(request, id):
	books = Bookmart.objects.get(id=id)
	if request.method == 'POST':
		books.delete()
		messages.info(request, "Book has been deleted!")
		return redirect("main:dashboard")
	context = {'book':books}
	return render(request, "main/delete_book.html", context)


@login_required(login_url='main:login')
def profileUpdate(request, id):
	customer = User.objects.get(id=id)
	form = CreateUserForm(instance=customer)

	if request.method == 'POST':
		form = CreateUserForm(request.POST, instance=customer)
		if form.is_valid():
			form.save()
			messages.success(request, "Profile Updated Successfully!")
			return redirect("main:customer.html")
		else:
			messages.info(request, "Something Went Wrong! Try Again Later.")
			return redirect("main:indexPage")

	context = {'form':form}
	return render(request, "main/customer_profile.html", context)

# @login_required(login_url='main:login')
def deleteCustomer(request, id):
	customer = User.objects.get(id=id)
	if request.method == 'POST':
		customer.delete()
		messages.info(request, "Customer has been deleted!")
		return redirect("main:dashboard")
	context = {'customer':customer}
	return render(request, "main/delete_customer.html", context) 

def delete_Order(request, id):
	orders = CustomerOrders.objects.get(id=id)
	if request.method == 'POST':
		orders.delete()
		messages.info(request, "Order has been deleted!")
		return redirect("main:dashboard")
	context = {'orders':orders}
	return render(request, "main/delete_customer.html", context) 


# @login_required(login_url='main:login')
def customerDetails(request):

	account = User.objects.all()
	total_users = account.count()
	context = {'account':account, 'total_users':total_users}
	return render(request, "main/customer_details.html", context)


@login_required(login_url='main:login')
def viewBook(request, id):

	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_total':0}
		cartItems = order['get_cart_items']

	book = Bookmart.objects.get(id=id)
	context = {'book':book, 'cartItems':cartItems}
	return render(request, "main/view_book.html", context)


@login_required(login_url='main:login')
def cartPage(request):


	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		print(customer)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_total':0}
		cartItems = order['get_cart_items']

	context = {"cart":"active", 'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, "main/cart_page.html", context)


@login_required(login_url='main:login')
def sellPage(request):

	form = BookUploadForm()	
	
	context = {"sell_book":"active", 'form':form}
	return render(request, "main/sell_book.html", context)




@login_required(login_url='main:login')
def checkoutPage(request):

	pc = ''
	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_total':0}
		cartItems = order['get_cart_items']

	amount = 0
	total = 0
	form = OrderPackage()
	order_id=Order.objects.get(customer=request.user.id)
	if request.POST:
		form.order = order_id
		form.package = request.POST['pack']
		amount =int(form.package)
		if amount == 50:
			form.end_date=timezone.now().date() + timedelta(days=7)
		elif amount == 80:
			form.end_date=timezone.now().date() + timedelta(days=14)
		else:
			form.end_date=timezone.now().date() + timedelta(days=30)

		form.save()

		total = amount * cartItems

	if amount == 50:
		pc = "One Week Package"
	elif amount == 80:
		pc = "Two Week Package"
	else:
		pc = "One Month package"

	context = {"cart":"active", 'items':items, 'order':order, 'cartItems':cartItems, 'amount':amount, 'total':total, 'pc':pc}

	return render(request, "main/checkout.html", context)


def confirm(request):
	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
		total_amt = order.get_cart_total

	card = request.POST['card_no']
	payment=Payment.objects.get(card_number=card)

	order=Order.objects.get(customer=request.user.id)

	pack=OrderPackage.objects.filter(order=order.id)
	package_amount = 0
	for i in pack:
		package_amount=i.package
		if package_amount == 50:
			exp_date=timezone.now().date() + timedelta(days=7)
		elif package_amount == 80:
			exp_date=timezone.now().date() + timedelta(days=14)
		else:
			exp_date=timezone.now().date() + timedelta(days=30)
	total = package_amount * cartItems
	print("total:",total)

	# 

	if payment is not None:
		post=CustomerOrders()
		post.customer=request.user
		post.payment_id=payment
		post.order_id = order.id
		post.quantity = cartItems
		post.package = package_amount
		post.total_amount = total
		post.end_date = exp_date
		post.save()
		print("order is: ",post.id)
		orderid =CustomerOrders.objects.get(id=post.id)

		
		# obj=CustomerBooks()
		# books = Bookmart.objects.all()
		for i in items:
			obj=CustomerBooks()
			a=Bookmart.objects.get(id=i.books.id)
			obj.customer=request.user
			obj.book=a
			obj.order_id = orderid
			print(obj.order_id)
			obj.save()


		orderitem=Order.objects.get(customer=request.user.id)
		print(orderitem)
		

		package=OrderPackage.objects.filter(order=orderitem.id)
		print(orderitem)
		package.delete()
		orderitem.delete()


		send_mail(
            'Order Confirmation',
            'Dear user, payment has been successfully complated! \n Enjoy reading books \n Thank you!',
            'thepictureperf@gmail.com',
            [request.user.email],
            fail_silently=False,
                                )

		messages.success(request, "You're order has been successfully completed")

		return redirect('main:mylibrary')
	else:
		messages.error(request, "Invalid card details! Try again.")


def mylibrary(request):

	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_total':0}
		cartItems = order['get_cart_items']

	if request.method == 'POST':
		post=Bookmart()
		post.book_publisher=request.user
		post.book_category=request.POST['book_category']
		post.book_title=request.POST['book_title']
		post.book_author=request.POST['book_author']
		post.book_description=request.POST['book_description']
		post.book_price=request.POST['book_price']
		post.book_image=request.FILES['book_image']
		post.book_pdf=request.FILES['book_pdf']
		post.save()


	fiction = CustomerBooks.objects.filter(customer=request.user)

	today=datetime.now()
	tot = fiction.count()

	context = {'fiction':fiction, 'tot':tot, "library":"active", 'cartItems':cartItems,'today':today}
	return render(request, "main/mylibrary.html", context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']

	print('Action:', action)
	print('productId:', productId)


	customer = request.user
	books = Bookmart.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, books=books)


	# if action == 'clear':
	# 	orderItem = orderItem.delete()
	# 	messages.info(request, "Item removed from cart!")
	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
		messages.success(request, "Item added to cart!")
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)
		messages.info(request, "Item removed from cart!")



	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('item was added', safe=False)

# Export CSV

def export_csv(request):

	response = HttpResponse(content_type = 'text/csv')
	response['Content-Disposition'] = 'attachemnt; filename=Bookmart.csv' 

	writer = csv.writer(response)
	writer.writerow(['Customer Name', 'Email Address', 'IS_ACTIVE', 'IS_STAFF', 'Created Date'])

	customers = User.objects.all()

	for customer in customers:
		writer.writerow([customer.username, customer.email, customer.is_active, customer.is_staff, customer.date_joined])

	return response


def order_cvs(request):

	response = HttpResponse(content_type = 'text/csv')
	response['Content-Disposition'] = 'attachemnt; filename=orders_report.csv' 

	writer = csv.writer(response)
	writer.writerow(['Customer', 'Quantity', 'Package', 'End Date', 'Amount', 'Ordred Date'])

	customers = CustomerOrders.objects.all()

	for customer in customers:
		writer.writerow([customer.customer, customer.quantity, customer.package, customer.end_date, customer.total_amount, customer.date_ordred])

	return response