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
    path('my-product/search',views.SearchMyProductView.as_view(), name="search_myproduct_view"),
    path('profile',views.ProfileView.as_view(), name="profile_view"),
    path('profile/edit',views.EditProfileView.as_view(), name="edit_profile_view"),
    path('report',views.ReportView.as_view(), name="report_view"),
    path('user-report',views.UserReportView.as_view(), name="user_report_view"),
    path('product/offer',views.OfferView.as_view(), name="offer_view"),
    path('my-offer',views.OfferView.as_view(), name="my-offer_view"),
    path('my-trade',views.TradeView.as_view(), name="trade_view"),
    path('product/detail',views.ProductDetailView.as_view(), name="product_detail_view"),
    path('my-product/detail',views.MyProductDetailView.as_view(), name="myproduct_detail_view"),
    path('add-user',views.AddUserView.as_view(), name="add_new_user"),
    path('product/addoffer',views.AddOfferView.as_view(), name="add_offer_view"),
    path('admin-user-table',views.AdminUserTableView.as_view(), name='admin_table')
    # path('overview',views.Overview.as_view(), name="overview_view"),
    # path('history',views.HistoryView.as_view(), name="history_view"),
    # path('pay-bills',views.PaybillsView.as_view(), name="pay_view"),
]