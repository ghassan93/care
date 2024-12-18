# Generated by Django 3.2.12 on 2022-09-07 03:57

import activatedapp.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django_countries.fields
import django_resized.forms
import phonenumber_field.modelfields
import re
import tinymce.models
import utils.upload


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='متاح')),
                ('activated_at', models.DateTimeField(null=True, verbose_name='تاريخ التفعيل')),
                ('disabled_at', models.DateTimeField(null=True, verbose_name='تاريخ إلغاء التفعيل')),
                ('name', models.CharField(error_messages={'unique': 'إسم المدينة موجود مسبقاً'}, max_length=255, unique=True, verbose_name='المدينة')),
                ('code', models.CharField(error_messages={'unique': 'الكود موجود مسبقاً'}, max_length=155, unique=True, validators=[django.core.validators.RegexValidator(message='يسمح فقط بإدخال احرف انجليزية.', regex='^[a-zA-Z_-]+$'), django.core.validators.MinLengthValidator(2)], verbose_name='الكود')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, null=True, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-\\w]+\\Z'), 'Enter a valid “slug” consisting of Unicode letters, numbers, underscores, or hyphens.', 'invalid')], verbose_name='الرابط')),
                ('country', django_countries.fields.CountryField(default='SA', max_length=2)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل')),
            ],
            options={
                'verbose_name': 'المدينة',
                'verbose_name_plural': 'المدن',
                'ordering': ['-id'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('activated', activatedapp.models.ActivatedManager()),
                ('archived', activatedapp.models.ArchivedManager()),
            ],
        ),
        migrations.CreateModel(
            name='Policies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='متاح')),
                ('activated_at', models.DateTimeField(null=True, verbose_name='تاريخ التفعيل')),
                ('disabled_at', models.DateTimeField(null=True, verbose_name='تاريخ إلغاء التفعيل')),
                ('title', models.CharField(max_length=255, verbose_name='العنوان')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, null=True, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-\\w]+\\Z'), 'Enter a valid “slug” consisting of Unicode letters, numbers, underscores, or hyphens.', 'invalid')], verbose_name='الرابط')),
                ('content', tinymce.models.HTMLField()),
                ('content_ar', tinymce.models.HTMLField(null=True)),
                ('content_en', tinymce.models.HTMLField(null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل')),
            ],
            options={
                'verbose_name': 'صفحات سياسة الخصوصية',
                'verbose_name_plural': 'صفحات سياسات الخصوصية',
                'ordering': ['-id'],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('activated', activatedapp.models.ActivatedManager()),
                ('archived', activatedapp.models.ArchivedManager()),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_type', models.CharField(choices=[('PP', 'صورة الملف الشخصي'), ('CP', 'صورة الغلاف'), ('VW', 'صورة العرض')], default='VW', max_length=2, verbose_name='نوع الصورة')),
                ('picture_file', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=95, size=[1920, 1080], upload_to=utils.upload.image_folder)),
                ('object_id', models.PositiveBigIntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'الصورة',
                'verbose_name_plural': 'الصور',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('phone_type', models.CharField(choices=[('H', 'رقم المنزل'), ('W', 'رقم العمل'), ('M', 'رقم الهاتف'), ('F', 'رقم الفاكس')], default='M', max_length=1, verbose_name='نوع الهاتف')),
                ('object_id', models.PositiveBigIntegerField()),
                ('verified', models.BooleanField(default=False, verbose_name='التحقق')),
                ('primary', models.BooleanField(default=False, verbose_name='أساسي')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'رقم الهاتف',
                'verbose_name_plural': 'ارقام الهواتف',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=utils.upload.file_folder, validators=[django.core.validators.FileExtensionValidator(['pdf', 'png', 'jpg', 'jpeg'])], verbose_name='الملف')),
                ('object_id', models.PositiveBigIntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاريخ التعديل')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'الملف',
                'verbose_name_plural': 'الملفات',
                'ordering': ['-id'],
            },
        ),
    ]
