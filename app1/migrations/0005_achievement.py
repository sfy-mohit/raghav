# Generated by Django 4.1 on 2023-08-17 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement_icon', models.ImageField(upload_to='app1/media/achievement')),
                ('achievement_title', models.CharField(max_length=50)),
                ('achievement_des', models.TextField()),
            ],
        ),
    ]
