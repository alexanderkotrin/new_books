# Generated by Django 3.1.3 on 2020-11-15 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('publication_date', models.DateField(null=True, verbose_name='Publicate on')),
                ('author', models.CharField(blank=True, max_length=30, verbose_name='Author')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('pages', models.IntegerField(blank=True, null=True, verbose_name='Pages')),
                ('book_type', models.PositiveSmallIntegerField(choices=[(1, 'Hardcover'), (2, 'Paperback'), (3, 'E-book')], verbose_name='Book type')),
            ],
        ),
    ]