from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.models import Group, User #, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from user_app.models import Product, Category, Report, Offer
# from .models import CustomUser
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from user_app.models import Address
from django.http import Http404
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
        user = request.user
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
            categories = Category.objects.all()
            # custom_user = User.objects.get(id=user)
            # consumer = Consumer.objects.get(custom_user=custom_user)
            # consumer = custom_user.get_all_registered_consumer.all()

            context = {
                'categories': categories,
            }
            return render(request, 'my-product_detail.html', context) #, context
        else:
            return redirect("user_app:login_view")

    def post(self,request):
        user = request.user
        #categories = user.category_set.all()
        # categories = None

        if request.method == 'POST':
            product_name = request.POST.get('product_name')
            description = request.POST.get('description')
            category = request.POST.get('category')
            # images = request.FILES.getlist('images')
            #Category.objects.filter(name=category)

            if len(request.FILES) != 0 and category is not None:
                images = request.FILES.get('images')
                categories = Category.objects.get(name=category)

                # for image in images:
                #     product = Product.objects.create(
                #         user=user,
                #         product_name=product_name,
                #         image=image,
                #         description=description,
                #         category=categories
                #     )
                # product.save()

                product = Product.objects.create(
                            user=user,
                            product_name=product_name,
                            image=images,
                            description=description,
                            category=categories
                        )

            product.save()
            messages.success(request, "Product Added Successfully!")

            return redirect('user_app:search_product_view')
        else:
            return HttpResponse('Invalid!') #form.errors

        # context = {
        #     'categories': categories,
        # }

        # return render(request, 'products.html', context)
        # username = request.POST.get('username')
        # first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        # email = request.POST.get('email')
        # password = request.POST.get('password')
        # User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        # # form = UserForm(request.POST)
        # # if form.is_valid():
        # #     custom_user = form.save(commit=False)
        # #     custom_user.user_id = user
        # #     custom_user.save()     
        # return redirect('user_app:login_view')
        # else:
        #     return HttpResponse(form.errors)

class SearchProductView(View):

    def get(self, request):
        if not request.user.is_staff:
            user = request.user
            products = Product.objects.all()
            # product_category = products.filter(user=user)
            # product_category = products.get_category.all()
            categories = Category.objects.all()
            # categories = Category.objects.get(id=product_category)
            # product_category = Category.get_category.all()
            # categories = Category.objects.get(id=product_category) #get_category.all()
            # custom_user = User.objects.get(id=user)
            # consumer = Consumer.objects.get(custom_user=custom_user)
            # consumer = custom_user.get_all_registered_consumer.all()
            # category = request.GET.get('category')
            # if category == None:
            #     product = Product.objects.filter(category=category)
            # else:
            #     product = Product.objects.filter(
            #         name=categories.name, category=category)

            # categories = Category.objects.filter(user=user.get_category.all)

            context = {
                'products': products,
                # 'product': product,
                'categories': categories,
            }
            return render(request, 'products.html', context) #, context
        else:
            return redirect("user_app:login_view")

class GalleryView(View):

    def gallery(self,request):
        if not request.user.is_staff:
            user = request.user
            category = request.GET.get('category')
            if category == None:
                photos = Product.objects.filter(category__user=user)
            else:
                photos = Product.objects.filter(
                    category__name=category, category__user=user)

            categories = Category.objects.filter(user=user)
            context = {'categories': categories, 'photos': photos}
            return render(request, 'product.html', context)
        else:
            return redirect("user_app:login_view")

class ProfileView(View):

    def get(self,request):
        users = User.objects.all()
        user = request.user
        address = user.get_user_address.all
        context ={
            'users':user,
            'addresses':address
        }

        return render(request, 'profile.html', context)


class EditProfileView(View):

       
    def get(self,request):
        user = User.objects.all()
        address= Address.objects.all()
       
        context ={
            'users':user,
            'address':address
        }
        return render(request, 'edit-profile.html', context)
    
    def post(self,request):
        # return render(request, 'Registration_page.html', context)
        cid = request.POST.get("user-id")
        username = request.POST.get('username')
        first_name = request.POST.get('user-first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email_address')
        address = request.POST.get('address')
        street = request.POST.get('street')
        brgy = request.POST.get('brgy')
        cityprovince = request.POST.get('cityprovince')
        zipcode = request.POST.get('zipcode')
        user = request.user
        User.objects.filter(id = cid).update(username=username,first_name=first_name,last_name=last_name,email=email)
        Address.objects.create(user=user, street=street, brgy=brgy,cityprovince=cityprovince,zipcode=zipcode)
        # form = UserForm(request.POST)
        # if form.is_valid():
        #     custom_user = form.save(commit=False)
        #     custom_user.user_id = user
        #     custom_user.save()     
        return redirect('user_app:profile_view')
        # else:
        #     return HttpResponse(form.errors)

class ReportView(View):

    def get(self, request):
        if not request.user.is_staff:
            user = request.user
            return render(request, 'report.html')
        else:
            return redirect("user_app:login_view")

    def post(self,request):
        email = request.POST.get('email')
        message = request.POST.get('message')
        user = request.user
        Report.objects.create(name=email,message=message,user=user)
        return redirect('user_app:user_report_view')

class UserReportView(View):

    def get(self, request):
        if not request.user.is_staff:
            user = request.user
            report = user.get_all_users_report.all
            context = {
                'reports': report,
            }
            return render(request, 'user_report.html', context)
        else:
            return redirect("user_app:login_view")

class OfferView(View):
    
    def get(self, request):
        if not request.user.is_staff:
            user = request.user
            return render(request, 'Offers.html')
        else:
            return redirect("user_app:login_view")

class ProductDetailView(View):

    def get(self, request): # , pk
        if not request.user.is_staff:
            user = request.user
            product = Product.objects.all() # get(id=pk)
            categories = Category.objects.all()
            context = {
                'product': product,
                'categories': categories,
            }
            return render(request, 'product_detail.html', context) #, context
        else:
            return redirect("user_app:login_view")

class TradeView(View):

    def get(self, request):
        if not request.user.is_staff:
            user = request.user
            # context = {
            #     'reports': report,
            # }
            return render(request, 'trade_detail.html') #, context
        else:
            return redirect("user_app:login_view")

class SearchMyProductView(View):

    def get(self, request):
        if not request.user.is_staff:
            user = request.user
            products = user.get_all_users_product.all # Product.objects.all()
            product = Product.objects.filter(user=user).values('category')
            # products = Product.objects.filter(user=user).get(category=)
            # for p in products:
            #     print(p)
            print(product)
            # categ = Category.objects.filter(id=product)
            # for c in categ:
            #     categs = c.name
            #     print(categs)
            category = Category.objects.all() 
            # for categ in product:
            #     # get_name = categ.
            #     print(categ)
            # categ = Category.objects.filter(id=product).values('name') 
            # print(categ)
            # product_cat = product.filter(category=category.id)
            # print(product_cat)
            # categories = Category.objects.get(id=product_cat)
            # categories = Category.category_set.all
            # categories = user.cate
            for cat in category:
                categories = cat.get_category.all()
                
                print("Category:",categories)
                # for cats in categories:
                #     print(cats)
            # products = Product.objects.get(category=cate)
            # print(products)
            # print(categories)
            new = product.union(categories)
            print(new)

            context = {
                'products': products,
                'product': product,
                'categories': categories,
            }
            return render(request, 'my-products.html', context) #, context
        else:
            return redirect("user_app:login_view")

class AddUserView(View):
    def get(self,request):
        return render(request, 'add_newuser.html')
    
    # register user [1]
    def post(self,request):
        # return render(request, 'Registration_page.html', context)
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = request.user
        User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        # form = UserForm(request.POST)
        # if form.is_valid():
        #     custom_user = form.save(commit=False)
        #     custom_user.user_id = user
        #     custom_user.save()     
        return redirect('user_app:admin_table')
        # else:
        #     return HttpResponse(form.errors)

class AddOfferView(View):

    def get(self, request):
        if not request.user.is_staff:
            user = request.user

            # context = {
            #     'categories': categories,
            # }
            return render(request, 'add_offer.html') #, context
        else:
            return redirect("user_app:login_view")

    def post(self,request):
        user = request.user

        if request.method == 'POST':
            offer_name = request.POST.get('offer_name')
            description = request.POST.get('description')
            images = request.FILES.get('images')
            product = Product.objects.get(id=11)

            offer = Offer.objects.create(
                        user=user,
                        product = product,
                        offer_name=offer_name,
                        image=images,
                        description=description,
                    )

            offer.save()
            messages.success(request, "Offer Added Successfully!")

            return redirect('user_app:search_myproduct_view')
        else:
            return HttpResponse('Invalid!') #form.errors

class MyProductDetailView(View):

    def get(self, request,pk):
        if not request.user.is_staff:
            user = request.user
            product = Product.objects.get(id=pk)
            categories = Category.objects.all()
            context = {
                'product': product,
                'categories': categories,
            }
            return render(request, 'my-product_detail.html', context) #, context
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
                return redirect("user_app:admin_table")
            elif 'btnDelete' in request.POST:
                cid = request.POST.get("user-id")
                user = User.objects.filter(id = cid).delete()
                print('recorded deleted')
                return redirect("user_app:admin_table")
                

    
        return HttpResponse('not valid')
        
class EditProductView(View):

    def get(self, request):
        if not request.user.is_staff:
            user = request.user
            product = Product.objects.first()
            categories = Category.objects.all()
            context = {
                'product': product,
                'categories': categories,
            }
            # custom_user = User.objects.get(id=user)
            # consumer = Consumer.objects.get(custom_user=custom_user)
            # consumer = custom_user.get_all_registered_consumer.all()

            return render(request, 'my-product_detail.html', context) #, context
        else:
            return redirect("user_app:login_view")

    def post(self,request):
        if request.method == 'POST':
            # if 'updateProduct' in request.POST:
            product_id = request.POST.get('product_id')
            product_name = request.POST.get('product_name')
            description = request.POST.get('description')
            category = request.POST.get('category')
            # images = request.FILES.getlist('images')
            #Category.objects.filter(name=category)

            # if len(request.FILES) != 0 and category is not None:
            images = request.FILES.get('images')
            categories = Category.objects.get(name=category)
            print(categories.id)

            product = Product.objects.filter(id=product_id).update(
                        product_name=product_name,
                        image=images,
                        description=description,
                        category=categories.id
                    )
                
            print(product)
            print(product_id)
            print(product_name)  
            print(images)
            print(description)
            print("updated")
            messages.success(request, "Product Added Successfully!")

            return redirect('user_app:search_product_view')
        else:
            return HttpResponse('Invalid!') #form.errors