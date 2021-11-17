from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.models import Group, User #, auth
from django.contrib.auth import authenticate, login, logout
# from .models import CustomUser
from .forms import UserForm
from django.contrib.auth.decorators import login_required
#import pyrebase

# Create your views here.
#config = {
#    'apiKey': "AIzaSyCMEEQ4rALIOf5lX0YuCvXXFABPk1ZvLjg",
#    'authDomain': "databasedj-45b67.firebaseapp.com",
#    'databaseURL': "https://databasedj-45b67-default-rtdb.firebaseio.com",
#    'projectId': "databasedj-45b67",
#    'storageBucket': "databasedj-45b67.appspot.com",
#    'messagingSenderId': "606108675515",
#    'appId': "1:606108675515:web:df26139a23b59f7f03e89e",
 
#}

#firebase=pyrebase.initialize_app(config)
#authe = firebase.auth()
#database = firebase.database()


class LoginView(View):
    
    def get(self,request):
        # user = request.user
        # custom_user = CustomUser.objects.get(user_id=user)
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        else:
            if not request.user.is_staff:
                return redirect("user_app:home_view")
            else:
                return redirect("admin_app:admin_view")
                          
    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            # print("hello")
            login(request, user)
            if not request.user.is_staff:
                return redirect("user_app:home_view")
            else:
                return redirect("admin_app:admin_view") #user_dashboard_view
        else:
            # print("incorrect")
            return redirect('user_app:login_view')
            # return HttpResponse("Incorrect!")
        
class LogoutView(View):
    
    # logout user [2]
    def get(self,request):
        logout(request)
        return redirect('user_app:login_view')
    
    # logout user [2]
    def post(self,request):
        logout(request)
        return redirect('user_app:login_view')

class RegisterView(View):
    
    def get(self,request):
        return render(request, 'registration.html')
    
    # register user [1]
    def post(self,request):
        # return render(request, 'Registration_page.html', context)
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        # form = UserForm(request.POST)
        # if form.is_valid():
        #     custom_user = form.save(commit=False)
        #     custom_user.user_id = user
        #     custom_user.save()     
        return redirect('user_app:login_view')
        # else:
        #     return HttpResponse(form.errors)

# @login_required
class HomeView(View):
    
    def get(self, request):
        if not request.user.is_staff:
            user = request.user
            # custom_user = User.objects.get(id=user)
            # consumer = Consumer.objects.get(custom_user=custom_user)
            # consumer = custom_user.get_all_registered_consumer.all()

            # context = {
            #     'consumer': consumer,
            # }
            return render(request, 'home.html') #, context
        else:
             return redirect("user_app:login_view")

class LandingView(View):
    
    def get(self, request):
        return render(request, 'landing.html') #, context

class ContactUsView(View):
    
    def get(self, request):
        if not request.user.is_staff:
            user = request.user
            # custom_user = User.objects.get(id=user)
            # consumer = Consumer.objects.get(custom_user=custom_user)
            # consumer = custom_user.get_all_registered_consumer.all()

            # context = {
            #     'consumer': consumer,
            # }
            return render(request, 'contact.html') #, context
        else:
             return redirect("user_app:login_view")

class AboutUsView(View):
    
    def get(self, request):
        if not request.user.is_staff:
            user = request.user
            # custom_user = User.objects.get(id=user)
            # consumer = Consumer.objects.get(custom_user=custom_user)
            # consumer = custom_user.get_all_registered_consumer.all()

            # context = {
            #     'consumer': consumer,
            # }
            return render(request, 'aboutus.html') #, context
        else:
             return redirect("user_app:login_view")

class AddProductView(View):

    def get(self, request):
        if not request.user.is_staff:
            user = request.user
            # custom_user = User.objects.get(id=user)
            # consumer = Consumer.objects.get(custom_user=custom_user)
            # consumer = custom_user.get_all_registered_consumer.all()

            # context = {
            #     'consumer': consumer,
            # }
            return render(request, 'add_product.html') #, context
        else:
            return redirect("user_app:login_view")

class SearchProductView(View):

    def get(self, request):
        if not request.user.is_staff:
            user = request.user
            # custom_user = User.objects.get(id=user)
            # consumer = Consumer.objects.get(custom_user=custom_user)
            # consumer = custom_user.get_all_registered_consumer.all()

            # context = {
            #     'consumer': consumer,
            # }
            return render(request, 'products.html') #, context
        else:
            return redirect("user_app:login_view")

class ProfileView(View):

    def get(self, request):
        if not request.user.is_staff:
            user = request.user
            # custom_user = User.objects.get(id=user)
            # consumer = Consumer.objects.get(custom_user=custom_user)
            # consumer = custom_user.get_all_registered_consumer.all()

            # context = {
            #     'consumer': consumer,
            # }
            return render(request, 'profile.html') #, context
        else:
            return redirect("user_app:login_view")

class ReportView(View):

    def get(self, request):
        if not request.user.is_staff:
            user = request.user
            return render(request, 'report.html')
        else:
            return redirect("user_app:login_view")
