# Generated by Django 4.2.6 on 2023-10-17 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_alter_imgrecord_options_imgrecord_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgrecord',
            name='content',
            field=models.CharField(blank=True, max_length=30, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='imgrecord',
            name='file_name',
            field=models.CharField(max_length=30, verbose_name='File name'),
        ),
    ]
