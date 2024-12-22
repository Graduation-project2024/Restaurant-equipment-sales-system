# Generated by Django 5.1.4 on 2024-12-17 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('cate_id', models.AutoField(primary_key=True, serialize=False)),
                ('categoryname', models.CharField(db_column='CategoryName', max_length=20)),
            ],
            options={
                'db_table': 'categories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('cust_id', models.AutoField(primary_key=True, serialize=False)),
                ('cust_name', models.CharField(max_length=20)),
                ('cust_email', models.CharField(max_length=20, unique=True)),
                ('cust_phone', models.CharField(max_length=11, unique=True)),
                ('cust_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inve_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantityinstock', models.IntegerField(db_column='QuantityInStock')),
            ],
            options={
                'db_table': 'inventory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InventoryHistory',
            fields=[
                ('hist_id', models.AutoField(primary_key=True, serialize=False)),
                ('change_date', models.DateTimeField()),
                ('change_qty', models.IntegerField()),
                ('change_type', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'inventory_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('invo_id', models.AutoField(primary_key=True, serialize=False)),
                ('invo_date', models.DateTimeField()),
                ('invo_totalamount', models.FloatField(db_column='invo_totalAmount')),
            ],
            options={
                'db_table': 'invoices',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('ord_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField(db_column='QTY')),
            ],
            options={
                'db_table': 'order_item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('ord_id', models.AutoField(primary_key=True, serialize=False)),
                ('ord_date', models.DateTimeField()),
                ('qty', models.IntegerField(db_column='QTY')),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('pay_id', models.AutoField(primary_key=True, serialize=False)),
                ('pay_method', models.CharField(max_length=15)),
                ('pay_date', models.DateTimeField()),
                ('pay_amount', models.FloatField()),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_name', models.CharField(db_column='prod_Name', max_length=20)),
                ('prod_image', models.CharField(blank=True, max_length=255, null=True)),
                ('prod_price', models.FloatField(db_column='prod_Price')),
                ('description_field', models.TextField(blank=True, db_column='description_', null=True)),
                ('prod_status', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductSupplier',
            fields=[
                ('prod_supp_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'product_supplier',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('rep_id', models.AutoField(primary_key=True, serialize=False)),
                ('rep_content', models.TextField(db_column='rep_Content')),
                ('rep_createddate', models.DateTimeField(db_column='rep_CreatedDate')),
                ('report_type', models.CharField(max_length=17)),
                ('report_status', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'reports',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('rev_id', models.AutoField(primary_key=True, serialize=False)),
                ('rev_rating', models.FloatField(blank=True, null=True)),
                ('rev_comment', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'reviews',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('rol_id', models.AutoField(primary_key=True, serialize=False)),
                ('rol_name', models.CharField(db_column='rol_Name', max_length=8)),
            ],
            options={
                'db_table': 'roles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('shi_id', models.AutoField(primary_key=True, serialize=False)),
                ('shi_address', models.CharField(max_length=50)),
                ('shi_date', models.DateField()),
            ],
            options={
                'db_table': 'shipping',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supp_id', models.AutoField(primary_key=True, serialize=False)),
                ('supp_name', models.CharField(max_length=25)),
                ('supp_address', models.CharField(max_length=50)),
                ('supp_phone', models.CharField(max_length=11, unique=True)),
                ('supp_email', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'supplier',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('usr_id', models.AutoField(primary_key=True, serialize=False)),
                ('usr_username', models.CharField(db_column='usr_UserName', max_length=30, unique=True)),
                ('usr_password', models.CharField(db_column='usr_Password', max_length=15)),
                ('usr_email', models.CharField(db_column='usr_Email', max_length=20, unique=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
