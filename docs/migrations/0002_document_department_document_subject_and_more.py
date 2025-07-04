# Generated by Django 5.2.2 on 2025-06-16 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='department',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='subject',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='image',
            field=models.ImageField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='document',
            name='owner',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='document',
            name='tags',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=700),
        ),
    ]
