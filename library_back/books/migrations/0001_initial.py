# Generated by Django 4.1 on 2022-08-15 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('release_year', models.PositiveIntegerField()),
                ('is_rented', models.BooleanField(default=False)),
                ('renter', models.ForeignKey(blank=True, default=None, null=True,
                 on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.UniqueConstraint(
                fields=('title', 'author', 'release_year'), name='unique_together_book_keys'),
        ),
    ]
