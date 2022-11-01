from dataclasses import fields
from rest_framework import serializers
from apis.models import employees, invoices, products, rates, sales, suppliers, categories


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = "__all__"


class Employees2Serializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = ['id', 'firstname', 'lastname',
                  'phone', 'email', "role", 'status', "username", "employee_status"]


class Employees1Serializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = ['id', 'username', 'email', 'status',
                  'supervisorcode']


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ["id", "barcode", "cost", "description", "name", "price", "quantity",
                  "tax", "categories_id", "suppliers_id"]


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = ('username', 'password')


class Products2Serializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ['id', 'barcode', 'name', 'price', 'quantity',
                  'cost', 'tax']


# class ProductsnewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = products
#         fields = ['id', 'barcode', 'name', 'price', 'quantity',
#                   'cost', 'tax']

class ProductsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ['quantity']


class RatesUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = rates
        fields = ('__all__')


class RatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = rates
        fields = ['id', 'baseCurrency', 'foreignCurrency', 'rate']


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = sales
        fields = ('__all__')


class ViewSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = sales
        fields = ('__all__')


class ViewSuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = suppliers
        fields = ('__all__')


class ViewCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = ('__all__')

##################################################################


class Products222Serializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = "__all__"


class Suppliers222Serializer(serializers.ModelSerializer):
    class Meta:
        model = suppliers
        fields = "__all__"


class ProductsanCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'
    categories_id = Products222Serializer(many=False)
    suppliers_id = Suppliers222Serializer(many=False)


class InvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = invoices
        fields = ['id', 'datetime', 'status', 'reference', 'channel',
                  'amount', 'vat', 'currency', 'employeeId']
