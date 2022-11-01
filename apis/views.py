from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from email import message
from rest_framework.views import APIView, Response
from apis.serializers import (Employees2Serializer, ViewSalesSerializer, ProductsanCategoriesSerializer,
                              ProductsSerializer, SalesSerializer, Products2Serializer,
                              RatesSerializer, RatesUpdateSerializer, InvoicesSerializer,
                              ViewSuppliersSerializer, ViewCategoriesSerializer,
                              ProductsUpdateSerializer, Employees1Serializer, EmployeesSerializer)
from apis.models import categories, invoices, products, employees, rates, sales, suppliers
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q


class ViewSuppliers(ListAPIView):
    def get(self, format=None):
        emdata = suppliers.objects.all()
        if len(emdata) == 0:
            return Response({"status_code": 400, "err_message": "no suppliers found"})
        else:
            serializer = ViewSuppliersSerializer(emdata, many=True)
            return Response({"status": 200, "message": "Success", "suppliers": serializer.data})


class CreateSuppliers(CreateAPIView):
    queryset = suppliers.objects.all()
    serializer_class = ViewSuppliersSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"status": 200, "message": "Success", "suppliers": serializer.data}, status=status.HTTP_201_CREATED, headers=headers)


class CreateExchangeCurrency(CreateAPIView):
    queryset = rates.objects.all()
    serializer_class = RatesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"status": 200, "message": "Success", "suppliers": serializer.data}, status=status.HTTP_201_CREATED, headers=headers)


class ViewCategories(ListAPIView):
    def get(self, format=None):
        emdata = categories.objects.all()
        if len(emdata) == 0:
            return Response({"status_code": 400, "err_message": "no categories found"})
        else:
            serializer = ViewCategoriesSerializer(emdata, many=True)
            return Response({"status": 200, "message": "Success", "categories": serializer.data})


class CreateCategories(CreateAPIView):
    queryset = categories.objects.all()
    serializer_class = ViewCategoriesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"status": 200, "message": "Success", "categories": serializer.data}, status=status.HTTP_201_CREATED, headers=headers)


class EmployeeManagement(ListAPIView):
    queryset = employees.objects.all()
    serializer_class = Employees2Serializer


class loginViewSet(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        emdata = employees.objects.filter(
            Q(firstname__icontains=username) & Q(password__icontains=password))
        if len(emdata) == 0:
            return Response({"status_code": 400, "err_message": "Invalid User Credidentials"})
        else:
            serializer = Employees1Serializer(emdata, many=True)
            return Response({"status_code": 200, "message": "Success", "user": serializer.data})


class ListSalesAPIView(APIView):
    def post(self, request, format=None):
        startdate = request.data.get('startdate')
        enddate = request.data.get('enddate')
        emdata = sales.objects.raw(
            'SELECT * FROM apis_sales WHERE datetime >= "'+startdate+'" AND datetime < "'+enddate+'"')
        if len(emdata) == 0:
            return Response({"status_code": 400, "err_message": "No Sales"})
        else:
            serializer = ViewSalesSerializer(emdata, many=True)
            return Response({"status_code": 200, "message": "Success", "sales": serializer.data})


class quantityAPIView(APIView):
    def get(self, request, format=None):
        emdata = products.objects.raw(
            'select id, quantity from apis_products')
        if len(emdata) == 0:
            return Response({"status_code": 400, "err_message": "No Sales"})
        else:
            serializer = ProductsUpdateSerializer(emdata, many=True)
            return Response({"status_code": 200, "message": "Success", "data": serializer.data})


class Ratesviews(ListAPIView):
    def get(self, format=None):
        emdata = rates.objects.all()
        if len(emdata) == 0:
            return Response({"status_code": 400, "err_message": "no rates found"})
        else:
            serializer = RatesSerializer(emdata, many=True)
            return Response({"status": 200, "message": "Success", "rates": serializer.data})


class RatesviewsZWL(ListAPIView):
    def get(self, format=None):
        emdata = rates.objects.raw(
            'SELECT * FROM apis_rates WHERE foreignCurrency = "ZWL"')
        if len(emdata) == 0:
            return Response({"status_code": 400, "err_message": "no rates found"})
        else:
            serializer = RatesSerializer(emdata, many=True)
            return Response({"status": 200, "message": "Success", "rates": serializer.data})


class RatesCreateviews(CreateAPIView):
    queryset = rates.objects.all()
    serializer_class = RatesUpdateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ListSalesAPICreate(CreateAPIView):
    queryset = sales.objects.all()
    serializer_class = SalesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['POST'])
def update_all_items(request):
    data = request.data
    for i in data:
        id = i.get('id')
        quantity = i.get('quantity')
        update = products.objects.get(id=id)
        update.quantity -= quantity
        update.save()
    return Response({"message": "Success"})


@api_view(['POST'])
def update_categories_items(request):
    data = request.data
    for i in data:
        id = i.get('id')
        categories_type = i.get('categories_type')
        categories_description = i.get('categories_description')
        update = categories.objects.get(id=id)
        update.categories_type = categories_type
        update.categories_description = categories_description
        update.save()
    return Response({"message": "Success"})


@api_view(['POST'])
def update_suppliers_items(request):
    data = request.data
    for i in data:
        id = i.get('id')
        suppliers_name = i.get('suppliers_name')
        suppliers_phone = i.get('suppliers_phone')
        suppliers_address = i.get('suppliers_address')
        update = suppliers.objects.get(id=id)
        update.suppliers_name = suppliers_name
        update.suppliers_phone = suppliers_phone
        update.suppliers_address = suppliers_address
        update.save()
    return Response({"message": "Success"})

# CreateSuppliers

@api_view(['POST'])
def update_exchangerate_items(request):
    data = request.data
    for i in data:
        id = i.get('id')
        baseCurrency = i.get('baseCurrency')
        foreignCurrency = i.get('foreignCurrency')
        rate = i.get('rate')
        update = rates.objects.get(id=id)
        update.baseCurrency = baseCurrency
        update.foreignCurrency = foreignCurrency
        update.rate = rate
        update.save()
    return Response({"message": "Success"})


@api_view(['POST'])
def update_employee_items(request):
    data = request.data
    for i in data:
        id = i.get('id')
        firstname = i.get('firstname')
        lastname = i.get('lastname')
        phone = i.get('phone')
        email = i.get('email')
        role = i.get('role')
        employee_status = i.get('employee_status')
        phone = i.get('phone')
        update = employees.objects.get(id=id)
        update.firstname = firstname
        update.lastname = lastname
        update.phone = phone
        update.email = email
        update.role = role
        update.employee_status = employee_status
        update.save()
    return Response({"message": "Success"})


@api_view(['POST'])
def update_all_items_add(request):
    data = request.data
    for i in data:
        id = i.get('id')
        quantity = i.get('quantity')
        update = products.objects.get(id=id)
        update.quantity += quantity
        update.save()
    return Response({"message": "Success"})


@ api_view(['DELETE'])
def delete_all_items(request):
    products.objects.all().delete()
    return Response(status=status.HTTP_200_OK)


class ListProductsAPIView(ListAPIView):
    def get(self, format=None):
        emdata = products.objects.all()
        if len(emdata) == 0:
            return Response({"status_code": 400, "err_message": "no products"})
        else:
            serializer = Products2Serializer(emdata, many=True)
            return Response({"status": 200, "message": "Success", "product": serializer.data})


class ListProductscategoriesAPIView(ListAPIView):
    def get(self, format=None):
        emdata = categories.objects.all()
        if len(emdata) == 0:
            return Response({"status_code": 400, "err_message": "no products"})
        else:
            serializer = ProductsanCategoriesSerializer(emdata, many=True)
            return Response({"status": 200, "message": "Success", "product": serializer.data})


class checkingValue(ListAPIView):
    queryset = products.objects.all()
    serializer_class = ProductsSerializer


class ListProducts1APIView(generics.ListAPIView):
    serializer_class = ProductsanCategoriesSerializer
    queryset = products.objects.all()


class CreateProductsAPIView(CreateAPIView):
    queryset = products.objects.all()
    serializer_class = ProductsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# delete_all_items
class DeleteProductsAPIView(DestroyAPIView):
    queryset = products.objects.all()
    serializer_class = ProductsSerializer


class EmployeesViewSet(CreateAPIView):
    queryset = employees.objects.all()
    serializer_class = EmployeesSerializer


class CreateInvoice(CreateAPIView):
    queryset = invoices.objects.all()
    serializer_class = InvoicesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"status": 200, "message": "Success", "data": serializer.data}, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['POST'])
def update_invoice_status_add(request):
    data = request.data
    for i in data:
        id = i.get('id')
        status = i.get('status')
        reference = i.get('reference')
        update = invoices.objects.get(id=id)
        update.status = status
        update.reference = reference
        update.save()
    return Response({"message": "Success"})


@api_view(['POST'])
def update_sales_reference_add(request):
    data = request.data
    for i in data:
        id = i.get('id')
        reference = i.get('reference')
        update = sales.objects.get(id=id)
        update.reference = reference
        update.save()
    return Response({"message": "Success"})


# ListProductsAPIView


