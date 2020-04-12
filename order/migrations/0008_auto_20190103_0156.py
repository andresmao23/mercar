# Generated by Django 2.0.2 on 2019-01-03 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20190103_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.Order', verbose_name='Id del pedido'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.Product', verbose_name='Id del producto'),
        ),
    ]
