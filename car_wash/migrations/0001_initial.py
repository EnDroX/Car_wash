# Generated by Django 3.0.3 on 2020-04-22 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ajustment',
            fields=[
                ('ajid', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('appby', models.CharField(blank=True, default='admin', max_length=255)),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('catid', models.BigAutoField(primary_key=True, serialize=False)),
                ('catname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cid', models.BigAutoField(primary_key=True, serialize=False)),
                ('cphonenumber', models.CharField(max_length=10)),
                ('count', models.IntegerField(blank=True, default='1')),
                ('lastdate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('exid', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('appby', models.CharField(blank=True, default='admin', max_length=255)),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expensetype',
            fields=[
                ('extypeid', models.BigAutoField(primary_key=True, serialize=False)),
                ('extypename', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Import',
            fields=[
                ('importid', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('discount_total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('grand_total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.CharField(blank=True, max_length=255)),
                ('billno', models.CharField(blank=True, max_length=30)),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('sellid', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('vat', models.DecimalField(blank=True, decimal_places=2, max_digits=8)),
                ('discount_total', models.DecimalField(blank=True, decimal_places=2, max_digits=8)),
                ('grant_total', models.DecimalField(blank=True, decimal_places=2, max_digits=8)),
                ('status', models.CharField(max_length=20)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_wash.Customer')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('suppid', models.BigAutoField(primary_key=True, serialize=False)),
                ('supptel', models.CharField(max_length=255)),
                ('suppname', models.CharField(max_length=255)),
                ('suppaddress', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('productid', models.BigAutoField(primary_key=True, serialize=False)),
                ('productname', models.CharField(max_length=255)),
                ('qty', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('unitprice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('onhand', models.IntegerField(blank=True)),
                ('reorder', models.IntegerField(blank=True)),
                ('vat', models.DecimalField(decimal_places=2, max_digits=3)),
                ('catid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_wash.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Selldetail',
            fields=[
                ('selldetailid', models.BigAutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_wash.Stock')),
                ('sellid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_wash.Sell')),
            ],
        ),
        migrations.CreateModel(
            name='Importdetail',
            fields=[
                ('importdetailid', models.BigAutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.CharField(max_length=255)),
                ('importid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_wash.Import')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_wash.Stock')),
            ],
        ),
        migrations.AddField(
            model_name='import',
            name='suppid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_wash.Supplier'),
        ),
        migrations.CreateModel(
            name='Expensedetail',
            fields=[
                ('exdid', models.BigAutoField(primary_key=True, serialize=False)),
                ('desciption', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('qty', models.IntegerField()),
                ('exid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_wash.Expense')),
                ('extypeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_wash.Expensetype')),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('couponid', models.BigAutoField(primary_key=True, serialize=False)),
                ('coupondescription', models.CharField(blank=True, max_length=255)),
                ('couponexpire', models.DateField(blank=True, null=True)),
                ('count', models.IntegerField()),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_wash.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Ajustmentdetal',
            fields=[
                ('ajdid', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('qty', models.IntegerField(default=0)),
                ('brokenprice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('ajid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_wash.Ajustment')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_wash.Stock')),
            ],
        ),
    ]
