# Generated by Django 5.1.2 on 2024-10-22 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('profile_picture', models.ImageField(upload_to='profile_pictures')),
                ('age', models.PositiveSmallIntegerField()),
                ('phone_number', models.CharField(max_length=200)),
                ('questions', models.ManyToManyField(blank=True, to='polls.question')),
            ],
        ),
    ]
