from django.db import models


class employees(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="OFFLINE")
    lastname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    employee_status = models.CharField(max_length=100, default="ACTIVE")
    supervisorcode = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, default="TELLER")
    username = models.CharField(max_length=100)


class invoices(models.Model):
    id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(auto_now_add=True, blank=False)
    status = models.CharField(max_length=100, null=True, blank=True)
    amount = models.BigIntegerField(blank=True, null=True)
    vat = models.BigIntegerField(blank=True, null=True)
    currency = models.CharField(max_length=100, null=True, blank=True)
    reference = models.CharField(max_length=100, null=True, blank=True)
    channel = models.CharField(max_length=100, null=True, blank=True)
    employeeId = models.BigIntegerField()


class rates(models.Model):
    id = models.AutoField(primary_key=True)
    baseCurrency = models.CharField(max_length=10)
    foreignCurrency = models.CharField(max_length=10)
    rate = models.BigIntegerField()


class sales(models.Model):
    id = models.AutoField(primary_key=True)
    base_currency = models.CharField(max_length=100, blank=True)
    channel = models.CharField(max_length=100, blank=True)
    cost_price = models.BigIntegerField(null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    employeeId = models.BigIntegerField(null=True)
    product = models.CharField(max_length=100)
    price = models.BigIntegerField(null=True)
    description = models.CharField(max_length=100, blank=True)
    employee = models.CharField(max_length=100, blank=True)
    foreign_currency = models.CharField(max_length=100, blank=True)
    imei = models.CharField(max_length=100, null=True, blank=True)
    invoiceId = models.BigIntegerField(null=True)
    pan = models.CharField(max_length=100, null=True, blank=True)
    productId = models.BigIntegerField(null=True)
    quantity = models.BigIntegerField(null=True)
    rate = models.BigIntegerField(null=True)
    reference = models.CharField(max_length=100, null=True, blank=True)
    rrn = models.CharField(max_length=100, null=True, blank=True)
    shop_name = models.CharField(max_length=100, blank=True)
    tax = models.BigIntegerField(null=True)
    total = models.BigIntegerField(null=True)


class suppliers(models.Model):
    id = models.AutoField(primary_key=True)
    suppliers_name = models.CharField(max_length=100)
    suppliers_phone = models.CharField(max_length=100)
    suppliers_id = models.IntegerField(default=1)
    suppliers_address = models.CharField(max_length=100)


class categories(models.Model):
    id = models.AutoField(primary_key=True)
    categories_id = models.IntegerField(default=1)
    categories_type = models.CharField(max_length=100)
    categories_description = models.CharField(max_length=100)

    def __str__(self):
        return self.categories_type


class products(models.Model):
    id = models.AutoField(primary_key=True)
    barcode = models.CharField(max_length=100, null=True, blank=True)
    cost = models.BigIntegerField(null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.BigIntegerField(null=True, blank=True)
    quantity = models.BigIntegerField(null=True, blank=True)
    tax = models.BigIntegerField(null=True, blank=True)
    categories_id = models.ForeignKey(
        categories, on_delete=models.CASCADE, default=1, null=True, blank=True)
    suppliers_id = models.ForeignKey(
        suppliers, on_delete=models.CASCADE, default=1, null=True, blank=True)


class orders(models.Model):
    id = models.AutoField(primary_key=True)
    createed_at = models.DateTimeField(auto_now_add=True)
    barcode = models.CharField(max_length=100)
    categoryId = models.BigIntegerField()
    cost = models.BigIntegerField()
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.BigIntegerField()
    quantity = models.BigIntegerField()
    supplierId = models.BigIntegerField()
    tax = models.BigIntegerField()
    categories_id = models.ForeignKey(
        categories, on_delete=models.CASCADE, default=1)
    suppliers_id = models.ForeignKey(
        suppliers, on_delete=models.CASCADE, default=1)


class ordersandproducts(models.Model):
    id = models.AutoField(primary_key=True)
    barcode = models.CharField(max_length=100)
    categoryId = models.BigIntegerField()
    cost = models.BigIntegerField()
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.BigIntegerField()
    quantity = models.BigIntegerField()
    supplierId = models.BigIntegerField()
    tax = models.BigIntegerField()
    categories_id = models.ForeignKey(
        categories, on_delete=models.CASCADE, default=3)
    suppliers_id = models.ForeignKey(
        suppliers, on_delete=models.CASCADE, default=3)
