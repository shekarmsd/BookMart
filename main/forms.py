from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from main.models import Bookmart, Contact




class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class BookUploadForm(forms.ModelForm):
	class Meta:
		model = Bookmart
		fields = ("book_title", "book_author","book_description", "book_image", "book_pdf", "book_price", "book_category")
			
class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = ("name", "email", "phone_number", "subject", "message")