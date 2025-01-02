from django.urls import path
from . import views

app_name = 'first_storePages'

# templates وربطها بملفات ال urls مسار عناوين ال 
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('update/', views.update, name='update'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('orders/', views.orders, name='orders'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('cart/', views.cart, name='cart'),
    path('category/', views.category, name='category'),
    path('quick-view/', views.quick_view, name='quick_view'),
    path('checkout/', views.checkout, name='checkout'),
    path('profile/', views.profile, name='profile'),
    path('password-reset/', views.password_reset_request, name='password_reset'),
    path('password-reset-confirm/<str:uidb64>/<str:token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('test-email/', views.test_email, name='test_email'),
]
