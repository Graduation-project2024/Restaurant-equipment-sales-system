from django.db import models
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Categories(models.Model):
    cate_id = models.AutoField(primary_key=True)
    categoryname = models.CharField(db_column='CategoryName', max_length=20)

    class Meta:
        managed = False
        db_table = 'categories'


class Customers(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=20)
    cust_email = models.CharField(unique=True, max_length=20)
    cust_phone = models.CharField(unique=True, max_length=11)
    cust_address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'customers'


class Inventory(models.Model):
    inve_id = models.AutoField(primary_key=True)
    prod = models.ForeignKey('Products', models.DO_NOTHING)
    quantityinstock = models.IntegerField(db_column='QuantityInStock')

    class Meta:
        managed = False
        db_table = 'inventory'


class InventoryHistory(models.Model):
    hist_id = models.AutoField(primary_key=True)
    prod = models.ForeignKey('Products', models.DO_NOTHING)
    change_date = models.DateTimeField()
    change_qty = models.IntegerField()
    change_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'inventory_history'


class Invoices(models.Model):
    invo_id = models.AutoField(primary_key=True)
    ord = models.ForeignKey('Orders', models.DO_NOTHING)
    invo_date = models.DateTimeField()
    invo_totalamount = models.FloatField(db_column='invo_totalAmount')

    class Meta:
        managed = False
        db_table = 'invoices'


class OrderItem(models.Model):
    ord_item_id = models.AutoField(primary_key=True)
    prod = models.ForeignKey('Products', models.DO_NOTHING)
    ord = models.ForeignKey('Orders', models.DO_NOTHING)
    qty = models.IntegerField(db_column='QTY')

    class Meta:
        managed = False
        db_table = 'order_item'


class Orders(models.Model):
    ord_id = models.AutoField(primary_key=True)
    cust = models.ForeignKey(Customers, models.DO_NOTHING)
    ord_date = models.DateTimeField()
    qty = models.IntegerField(db_column='QTY')

    class Meta:
        managed = False
        db_table = 'orders'


class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    ord = models.ForeignKey(Orders, models.DO_NOTHING)
    pay_method = models.CharField(max_length=15)
    pay_date = models.DateTimeField()
    pay_amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'payment'


class ProductSupplier(models.Model):
    prod_supp_id = models.AutoField(primary_key=True)
    prod = models.ForeignKey('Products', models.DO_NOTHING)
    supp = models.ForeignKey('Supplier', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_supplier'


class Products(models.Model):
    prod_id = models.AutoField(primary_key=True)
    cate = models.ForeignKey(Categories, models.DO_NOTHING)
    prod_name = models.CharField(db_column='prod_Name', max_length=20)
    prod_image = models.CharField(max_length=255, blank=True, null=True)
    prod_price = models.FloatField(db_column='prod_Price')
    description_field = models.TextField(db_column='description_', blank=True, null=True)
    prod_status = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'products'


class Reports(models.Model):
    rep_id = models.AutoField(primary_key=True)
    usr = models.ForeignKey('Users', models.DO_NOTHING)
    rep_content = models.TextField(db_column='rep_Content')
    rep_createddate = models.DateTimeField(db_column='rep_CreatedDate')
    report_type = models.CharField(max_length=17)
    report_status = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'reports'


class Reviews(models.Model):
    rev_id = models.AutoField(primary_key=True)
    prod = models.ForeignKey(Products, models.DO_NOTHING)
    cust = models.ForeignKey(Customers, models.DO_NOTHING)
    rev_rating = models.FloatField(blank=True, null=True)
    rev_comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'


class Roles(models.Model):
    rol_id = models.AutoField(primary_key=True)
    rol_name = models.CharField(db_column='rol_Name', max_length=8)

    class Meta:
        managed = False
        db_table = 'roles'


class Shipping(models.Model):
    shi_id = models.AutoField(primary_key=True)
    ord = models.ForeignKey(Orders, models.DO_NOTHING)
    shi_address = models.CharField(max_length=50)
    shi_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'shipping'


class Supplier(models.Model):
    supp_id = models.AutoField(primary_key=True)
    supp_name = models.CharField(max_length=25)
    supp_address = models.CharField(max_length=50)
    supp_phone = models.CharField(unique=True, max_length=11)
    supp_email = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'supplier'


class Users(models.Model):
    usr_id = models.AutoField(primary_key=True)
    rol = models.ForeignKey(Roles, models.DO_NOTHING)
    usr_username = models.CharField(db_column='usr_UserName', unique=True, max_length=30)
    usr_password = models.CharField(db_column='usr_Password', max_length=15)
    usr_email = models.CharField(db_column='usr_Email', unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'users'
