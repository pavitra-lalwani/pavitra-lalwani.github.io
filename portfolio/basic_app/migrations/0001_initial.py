# Generated by Django 4.1 on 2022-08-27 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('description1', models.TextField(blank=True, null=True)),
                ('description2', models.TextField(blank=True, null=True)),
                ('about_avatar', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('msg', models.TextField(blank=True, max_length=100, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('image', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('avatar', models.URLField(blank=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv')),
                ('github', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('leetcode', models.URLField(blank=True, null=True)),
                ('mycv', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('skill', models.TextField(blank=True, max_length=230, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('image', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(blank=True, max_length=50, null=True)),
                ('num', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]