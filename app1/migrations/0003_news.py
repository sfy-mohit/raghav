# Generated by Django 4.1 on 2023-08-17 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_image', models.ImageField(upload_to='app1/media/news')),
                ('news_title', models.CharField(max_length=50)),
                ('news_des', models.TextField()),
            ],
        ),
    ]
