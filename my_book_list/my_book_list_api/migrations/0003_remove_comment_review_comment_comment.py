# Generated by Django 4.1.3 on 2022-11-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_book_list_api', '0002_remove_book_comment_book_review_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='review',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(default='komentaras', max_length=10000, verbose_name='comment'),
            preserve_default=False,
        ),
    ]
