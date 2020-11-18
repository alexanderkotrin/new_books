from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from isbn_field import ISBNField


class Book(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-book'),
    )

    ITBRICKS = 1
    LULU = 2
    AMAZON = 3
    PRINTING_PARTNER = (
        (ITBRICKS, 'ITBRICKS'),
        (LULU, 'LULU'),
        (AMAZON, 'AMAZON'),
    )

    isbn = ISBNField(verbose_name='ISBN', blank=False, null=False)
    contributor = models.CharField(max_length=50, verbose_name='Author', blank=True, null=True)
    email_contributor = models.EmailField(verbose_name='Author"s email', blank=True, null=True)
    title = models.CharField(max_length=50, verbose_name='Title')
    isbn_received = models.DateField(verbose_name='ISBN received', blank=True, null=True)
    publication_date = models.DateField(verbose_name='Publicate on', blank=True, null=True)
    isbn_due = models.DateField(verbose_name='ISBN Due', blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Price, €')
    pages = models.IntegerField(blank=True, null=True, verbose_name='Pages')
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES, verbose_name='Book type')
    print_partner = models.PositiveSmallIntegerField(choices=PRINTING_PARTNER, default=1, verbose_name='Print Partner')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:book-update', kwargs={'pk': self.pk})

    class Meta:
        # db_table = 'books'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Lead(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Book')
    slug = models.SlugField(max_length=255, verbose_name='Slug', unique=True)
    title = models.CharField(max_length=100, verbose_name='Title')
    username = models.CharField(max_length=90, verbose_name='User name')
    email = models.EmailField(verbose_name='email')
    date_sent = models.DateTimeField(blank=True, null=True, verbose_name='Date sent')

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'
        ordering = ['-date_sent']