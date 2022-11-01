from django.urls import path
from apis import views

urlpatterns = [
    path('login/', views.loginViewSet.as_view(), name="login"),
    path('employee/', views.EmployeeManagement.as_view(), name="employee"),
    path('employee/create/', views.EmployeesViewSet.as_view(),
         name="Create Employee"),
    path("view/", views.ListProductsAPIView.as_view(), name="view_product"),
    path("quantity/", views.quantityAPIView.as_view(),
         name="Quantity product"),
    path("viewcategories/", views.ListProductscategoriesAPIView.as_view(),
         name="view_product"),
    path("categories/", views.ViewCategories.as_view(), name="view_categories"),
    path("categories/create/", views.CreateCategories.as_view(),
         name="create_categories/"),
    path("suppliers/", views.ViewSuppliers.as_view(),
         name="view_suppliers"),
    #     delete_all_items DeleteProductsAPIView
    #################################################################

    path("invoice/create/", views.CreateInvoice.as_view(),
         name="create invoice"),

    ###################################################################

    path("suppliers/create/", views.CreateSuppliers.as_view(),
         name="create_suppliers"),
    path("exchangerate/create/", views.CreateExchangeCurrency.as_view(),
         name="Create Exchangerate"),
    path("views/", views.update_all_items,         name="view_product1"),
    path("update/suppliers/", views.update_suppliers_items,
         name="Update Suppliers"),

    #########################################################

    path("update/invoice/", views.update_invoice_status_add,
         name="Update Invoice"),
    path("update/sales/", views.update_sales_reference_add,
         name="Update Sales"),

    #########################################################

    path("update/employee/", views.update_employee_items,
         name="Update Employee"),
    path("update/exchangerate/", views.update_exchangerate_items,
         name="Update Stock product1"),
    path("add/stock/", views.update_all_items_add, name="Add Stock product1"),
    path("sales/", views.ListSalesAPICreate.as_view(), name="sales"),
    path("view/sales/", views.ListSalesAPIView.as_view(), name="view sales"),
    path("create/", views.CreateProductsAPIView.as_view(), name="create_product"),
    path("rate/", views.Ratesviews.as_view(), name="rates"),
    path("zwl/rate/", views.RatesviewsZWL.as_view(), name="ZWL rates"),
    path("rate/create/", views.RatesCreateviews.as_view(), name="rate_create"),
    path("update/", views.update_all_items, name="update_product"),
    path("delete/", views.delete_all_items, name="delete_product"),
    path("update/categories/", views.update_categories_items,
         name="Update Categories"),
    path("allproducts/", views.ListProducts1APIView.as_view(), name="rate_create"),
]
