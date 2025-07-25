# Generated by Django 4.2 on 2025-07-07 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('author', models.CharField(max_length=140)),
                ('lang', models.CharField(max_length=140)),
                ('publisher', models.CharField(max_length=140)),
                ('isbn', models.CharField(max_length=140)),
                ('published_date', models.CharField(max_length=140)),
            ],
        ),
    ]
