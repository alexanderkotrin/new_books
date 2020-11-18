from django.contrib import admin
from .models import Book, Lead

class BookAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True    
    list_display = ('title', 'book_type', 'publication_date', )
    list_display_links = ('title', )
    search_fields = ('title', )
    # exclude = ('pk', )
    fields = ('isbn', 'contributor', 'email_contributor', 'title', 'publication_date', 'pages', 'isbn_received', 'isbn_due', 'book_type', 'price', 'print_partner' )
    # readonly_fields = ('pk', )

admin.site.register(Book, BookAdmin)


class LeadAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    save_as = True
    save_on_top = True
    list_display = ('title', 'book', 'username', 'email', 'date_sent')
    list_display_links = ('title', 'book')
    search_fields = ('title', 'book')
    list_filter = ('book', 'date_sent', )
    # list_editable = ('', )
    # readonly_fields = ('username',)
    fields = (('title', 'slug'), ('username', 'email'), ('book', 'date_sent'), )

admin.site.register(Lead, LeadAdmin)



    # isbn = models.CharField(max_length=50, verbose_name='ISBN')
    # contributor = models.CharField(max_length=50, verbose_name='Author')
    # email_contributor = models.EmailField(verbose_name='Author"s email')
    # title = models.CharField(max_length=50, verbose_name='Title')
    # isbn_received = models.DateField(null=False, verbose_name='ISBN received')
    # publication_date = models.DateField(null=False, verbose_name='Publicate on')
    # isbn_due = models.DateField(null=False, verbose_name='COPIES to CNC')
    # price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Price, €')
    # pages = models.IntegerField(blank=True, null=True, verbose_name='Pages')
    # book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES, verbose_name='Book type')
    # print_partner = models.PositiveSmallIntegerField(choices=PRINTING_PARTNER, default=1)