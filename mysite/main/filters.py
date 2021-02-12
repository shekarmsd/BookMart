import django_filters

from .models import *

class BookFilter(django_filters.FilterSet):
	class Meta:
		model = Bookmart
		fields = {'book_category', 'book_title'}