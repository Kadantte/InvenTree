# Generated by Django 3.2.14 on 2022-07-09 01:01

from django.db import migrations, models
import order.validators


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0072_alter_salesorder_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='reference',
            field=models.CharField(default=order.validators.generate_next_purchase_order_reference, help_text='Order reference', max_length=64, unique=True, validators=[order.validators.validate_purchase_order_reference], verbose_name='Reference'),
        ),
    ]
