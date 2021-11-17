from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path('',views.LandingView.as_view(), name="landing_view"),
    path('home',views.HomeView.as_view(), name="home_view"),
    path('login',views.LoginView.as_view(), name="login_view"),
    path('logout',views.LogoutView.as_view(), name="logout_view"),
    path('register',views.RegisterView.as_view(), name="register_view"),
    path('contact-us',views.ContactUsView.as_view(), name="contact_view"),
    path('about-us',views.AboutUsView.as_view(), name="about_view"),
    path('product/add',views.AddProductView.as_view(), name="add_product_view"),
    path('product/search',views.SearchProductView.as_view(), name="search_product_view"),
    path('profile',views.ProfileView.as_view(), name="profile_view"),
    path('profile/edit',views.EditProfileView.as_view(), name="edit_profile_view")
    # path('overview',views.Overview.as_view(), name="overview_view"),
    # path('history',views.HistoryView.as_view(), name="history_view"),
    # path('pay-bills',views.PaybillsView.as_view(), name="pay_view"),
]