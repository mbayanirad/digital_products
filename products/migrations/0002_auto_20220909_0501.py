# Generated by Django 3.2 on 2022-09-09 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='fileType',
            field=models.PositiveSmallIntegerField(choices=[(1, 'audio'), (2, 'video'), (3, 'pdf')], default=2, verbose_name='file type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='products.product', verbose_name='products'),
        ),
    ]