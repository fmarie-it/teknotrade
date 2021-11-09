from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from user_app.models import User
# Create your views here.

class AdminDashboard(View):

    def get(self, request):
        if request.user.is_staff:
            user = request.user
            # custom_user = User.objects.get(id=user)
            # admin = custom_user.user_id.first_name
            # invoice = Invoice.objects.all()
            # consumer = Consumer.objects.all()

            # context = {
            #     'admin': admin,
            #     'invoice': invoice,
            #     'consumer': consumer,
            # }
            return render(request, 'admin_dashboard.html') #, context
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