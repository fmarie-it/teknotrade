from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from django.http import HttpResponse
from user_app.models import Product, User
# Create your views here.

class AdminDashboard(View):

    def get(self, request):
        if request.user.is_staff:
            user = request.user
            # custom_user = User.objects.get(id=user)
            # admin = custom_user.user_id.first_name
            # invoice = Invoice.objects.all()
            # consumer = Consumer.objects.all()

            context = {
                'full_name': user.first_name + " " + user.last_name,
            }
            return render(request, 'admin_dashboard.html', context)
        else:
            return redirect("user_app:login_view")

    # def post(self, request):
    #     desc = request.POST.get('desc')
    #     invoice_date = request.POST.get('invoice_date')
    #     due_date = request.POST.get('due_date')
    #     current_bill = request.POST.get('current_bill')
    #     balance = request.POST.get('balance')
    #     status = request.POST.get('status')
    #     user = request.POST.get('consumer')
    #     consumer = Consumer.objects.get(id=user)
    #     Invoice.objects.create(desc=desc,invoice_date=invoice_date,due_date=due_date,current_bill=current_bill,
    #                             balance=balance,status=status,consumer_id=consumer)    
    #     return redirect('app_admin:admin_view')

class ListProductView(View):

    def get(self, request):
        if request.user.is_staff:
            products = Product.objects.exclude(admin_status="pending")
            context = {
                'products': products,
            }
            return render(request, 'list_product.html', context)
        else:
            return redirect("user_app:login_view")

class ProductRequestView(View):

    def get(self, request):
        if request.user.is_staff:
            products = Product.objects.all()
            context = {
                'products': products,
            }
            return render(request, 'product_request.html', context)
        else:
            return redirect("user_app:login_view")

    def post(self, request, *args, **kwargs):
        if request.user.is_staff:
            id = kwargs["id"]
            product = get_object_or_404(Product, pk=id)
            product.admin_status = request.POST['status']
            product.save()
            return redirect("admin_app:product_request_view")
        else:
            return redirect("user_app:login_view")