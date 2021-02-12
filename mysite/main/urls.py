
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "main"

urlpatterns = [

 	path('', views.indexPage, name="indexPage"),
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logout_request, name="logout"),
	path('about/', views.aboutPage, name="about"),
	path('category/', views.categoryPage, name="category"),
	path('contact/', views.contactPage, name="contact"),
	path('customer/<str:id>/', views.customerPage, name="customer"),
	path('dashboard/', views.dashboardPage, name="dashboard"),

	path('update_book/<str:id>/', views.updateBook, name="update_book"),
	path('delete_book/<str:id>/', views.deleteBook, name="delete_book"),
	path('delete_customer/<str:id>/', views.deleteCustomer, name="delete_customer"),
	path('customer_profile/<str:id>/', views.profileUpdate, name="customer_profile"),
	path('customer_details/', views.customerDetails, name="customer_details"),

	path('view_book/<str:id>/', views.viewBook, name="view_book"),
	path('cart_page/', views.cartPage, name="cart_page"),

	path('sell_book/', views.sellPage, name="sell_book"),
	path('checkout/', views.checkoutPage, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('confirm/', views.confirm, name="confirm"),
	path('mylibrary/', views.mylibrary, name="mylibrary"),
	path('export_csv/', views.export_csv, name="export_csv"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
