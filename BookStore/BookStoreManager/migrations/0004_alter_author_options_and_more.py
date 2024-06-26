# Generated by Django 5.0.4 on 2024-04-09 13:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookStoreManager', '0003_book_boobkcover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='publication_year',
            new_name='publicationYear',
        ),
        migrations.RemoveField(
            model_name='borrowing',
            name='borrow_date',
        ),
        migrations.RemoveField(
            model_name='borrowing',
            name='return_date',
        ),
        migrations.AddField(
            model_name='borrowing',
            name='borrowDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='borrowing',
            name='returnDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
