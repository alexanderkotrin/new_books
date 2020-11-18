from django import forms
from .models import Book, Lead
from bootstrap_datepicker_plus import DatePickerInput
from isbn_field import ISBNField


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('isbn', 'contributor', 'email_contributor', 'title', 'publication_date', 'pages', 'isbn_received', 'isbn_due', 'book_type', 'price', 'print_partner' )
        widgets = {
            'publication_date': DatePickerInput(format='%Y-%m-%d'),
            'isbn_received': DatePickerInput(format='%Y-%m-%d'),
            'isbn_due': DatePickerInput(format='%Y-%m-%d'),
        }

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('book', 'title', 'username', 'email', 'date_sent', )
        widgets = {
            'date_sent': DatePickerInput(format='%Y-%m-%d'),
        }
