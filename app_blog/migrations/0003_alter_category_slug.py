# Generated by Django 5.1.1 on 2024-10-11 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_alter_category_options_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Слаг'),
        ),
    ]
