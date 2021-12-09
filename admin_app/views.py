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

class AdminUserTableView(View):
    def get(self,request):
        user = User.objects.all()
        context ={
            'users':user,   
        }   
        return render(request, 'admin_table.html', context)
    def post(self,request):
        if request.method == 'POST':
            if 'btnUpdate' in request.POST:
                print('update button clicked')
                cid = request.POST.get("user-id")
                username = request.POST.get('username')
                first_name = request.POST.get('firstname')
                last_name = request.POST.get('lastname')
                email = request.POST.get('email')
                update = User.objects.filter(id = cid).update(username=username,first_name=first_name,last_name=last_name,email=email)
                # form = UserForm(request.POST)
                # if form.is_valid():
                #     custom_user = form.save(commit=False)
                #     custom_user.user_id = user
                #     custom_user.save()   
                print(update)  
                print("updated")  
                return redirect("admin_app:admin_table")
            elif 'btnDelete' in request.POST:
                cid = request.POST.get("user-id")
                user = User.objects.filter(id = cid).delete()
                print('recorded deleted')
                return redirect("admin_app:admin_table")
                

    
        return HttpResponse('not valid')