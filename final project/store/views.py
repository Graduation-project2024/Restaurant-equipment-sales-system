from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
#

def home(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'search_page.html')

def register(request): # صفحة تسجيل حساب جديد
    if request.method == 'POST': # جملة شرطية لتحديد توافق البيانات المسجلة بالمعايير المطلوبة
        username = request.POST['name'] # اسم المستخدم
        email = request.POST['email'] # الايميل
        password = request.POST['pass'] # الباسورد
        confirm_password = request.POST['cpass'] # تأكيد الباسورد
        
        if password != confirm_password: # في حالة عدم تطابق الباسورد مع تأكيد الباسورد
            messages.error(request, 'Passwords do not match') # اظهر رسالة عدم تطابق الباسورد
            return redirect('store:register') # اعد الدخول الى صفحة تسجيل الدخول
            
        if User.objects.filter(username=username).exists(): # لو اسم المستخدم موجود بالفعل 
            messages.error(request, 'Username already exists') # اظهر رسالة بوجود اسم المستخدم بالفعل
            return redirect('store:register')
            
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists') 
            return redirect('store:register')
            
        user = User.objects.create_user(username=username, email=email, password=password) # تسجيل البيانات في الجدول الخاص بالمستخدمين
        auth_login(request, user)
        messages.success(request, 'Registration successful') # اظهار رسالة تسجيل الحساب بنجاح
        return redirect('store:home') # توجيه المستخدم لصفحة البداية
        
    return render(request, 'user_register.html')

def login(request): # صفحة تسجيل الدخول
    if request.method == 'POST': # جملة شرطية للتأكد من وجود الحساب
        email = request.POST['email']
        password = request.POST['pass']
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            return redirect('store:login')
            
        if user.check_password(password):
            auth_login(request, user)
            messages.success(request, 'Login successful')
            return redirect('store:home')
        else:
            messages.error(request, 'Invalid password')
            return redirect('store:login')
            
    return render(request, 'user_login.html')

def logout_view(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('store:home')

@login_required # يتطلب تسجيل الدخول
def update(request):
    if request.method == 'POST':
        user = request.user
        username = request.POST['name']
        email = request.POST['email']
        old_password = request.POST['old_pass']
        new_password = request.POST['new_pass']
        confirm_password = request.POST['cpass']
        
        if not user.check_password(old_password):
            messages.error(request, 'Current password is incorrect')
            return redirect('store:update')
            
        if new_password and new_password != confirm_password:
            messages.error(request, 'New passwords do not match')
            return redirect('store:update')
            
        if User.objects.exclude(id=user.id).filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('store:update')
            
        if User.objects.exclude(id=user.id).filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('store:update')
            
        user.username = username
        user.email = email
        if new_password:
            user.set_password(new_password)
        user.save()
        
        messages.success(request, 'Profile updated successfully')
        if new_password:
            auth_login(request, user)
        return redirect('store:home')
        
    return render(request, 'update_user.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    return render(request, 'shop.html')

def about(request):
    return render(request, 'about.html')

@login_required
def orders(request):
    return render(request, 'orders.html')

@login_required
def wishlist(request):
    return render(request, 'wishlist.html')

@login_required
def cart(request):
    return render(request, 'cart.html')

def category(request):
    return render(request, 'category.html')

def quick_view(request):
    return render(request, 'quick_view.html')

@login_required
def checkout(request):
    return render(request, 'checkout.html')
