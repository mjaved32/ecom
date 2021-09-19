# Generated by Django 3.2.6 on 2021-08-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_cart_checkout_contact_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='note',
        ),
        migrations.RemoveField(
            model_name='product',
            name='xxl',
        ),
        migrations.AddField(
            model_name='checkout',
            name='notes',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='checkout',
            name='phone',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='address1',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='address2',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='uname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cart',
            name='color',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='address1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='address2',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='email',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='name',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='state',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='basePrice',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='finalPrice',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='accountNumber',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='bankName',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='ifscCode',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='seller',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='uname',
            field=models.CharField(max_length=20),
        ),
    ]
