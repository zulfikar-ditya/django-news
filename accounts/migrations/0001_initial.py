# Generated by Django 3.1.2 on 2020-10-12 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=70, unique=True)),
                ('email', models.EmailField(default='', max_length=254)),
                ('full_name', models.CharField(default='', max_length=75)),
                ('phone', models.IntegerField(default=0)),
                ('address', models.CharField(default='', max_length=95)),
                ('avatar', models.ImageField(default='static/img/avatar/default.jpg', upload_to='static/img/avatar/')),
                ('gender', models.BooleanField(default=True)),
                ('date_join', models.DateField(auto_now_add=True)),
                ('date_of_birth', models.DateField(default='2000-01-01')),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_reporter', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
