from django.urls import path
from . import views

app_name = 'admin_app'

urlpatterns = [
    # path('admin',views.HomeView.as_view(), name="home_view"),
    path('dashboard',views.AdminDashboard.as_view(), name="admin_view"),
    # path('invoices',views.InvoiceView.as_view(), name="invoice_view"),
    # path('queries',views.QueriesView.as_view(), name="queries_view"),
    # path('billing',views.BillingView.as_view(), name="billing_view"),
    # path('add-user',views.AddUserView.as_view(), name="add_user_view"),
    # path('add-consumer',views.AddConsumerView.as_view(), name="add_consumer_view"),
]