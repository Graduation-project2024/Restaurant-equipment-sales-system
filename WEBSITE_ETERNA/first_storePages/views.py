from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from .forms import SignUpForm, SignInForm, PasswordResetForm, SetPasswordForm, UpdateProfileForm
from .models import Roles, Users
from django.core.cache import cache
from datetime import datetime, timedelta
from .decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

# Create your views here.

def home(request):
    # Pass user to template context
    return render(request, 'home.html', {'user': request.user})

def search(request):
    return render(request, 'search_page.html')

def register(request):
    if request.method == 'POST':
        # إنشاء نموذج وتعبئته بالبيانات القادمة من الطلب
        form = SignUpForm(request.POST)
        if form.is_valid():  # التحقق من صحة البيانات
            # حفظ المستخدم في قاعدة البيانات
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            try:
                user.rol = Roles.objects.get(rol_id=1)  # Assign the default role
            except Roles.DoesNotExist:
                messages.error(request, 'Default role does not exist. Please contact the administrator.')
                return redirect('first_storePages:register')
            user.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('first_storePages:login')
        else:
            # إذا لم تكن البيانات صحيحة، عرض الأخطاء
            messages.error(request, 'There was an error in your registration. Please correct the errors below.')
    else:
        #إنشئ نموذج فارغ, GET إذا كان الطلب 
        form = SignUpForm()

    return render(request, 'user_register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            # The form's clean method has already validated the credentials
            user = form.cleaned_data['user']
            # Create a session for the user
            request.session['user_id'] = user.usr_id
            request.session['username'] = user.username
            
            messages.success(request, f'مرحباً {user.username}!')
            
            # Redirect to next URL if it exists
            next_url = request.session.get('next')
            if next_url:
                del request.session['next']
                return redirect(next_url)
            return redirect('first_storePages:home')
    else:
        form = SignInForm()

    return render(request, 'user_login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    messages.success(request, 'تم تسجيل الخروج بنجاح!')
    return redirect('first_storePages:home')

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
            return redirect('first_storePages:update')
            
        if new_password and new_password != confirm_password:
            messages.error(request, 'New passwords do not match')
            return redirect('first_storePages:update')
            
        if Users.objects.exclude(id=user.id).filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('first_storePages:update')
            
        if Users.objects.exclude(id=user.id).filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('first_storePages:update')
            
        user.username = username
        user.email = email
        if new_password:
            user.set_password(new_password)
        user.save()
        
        messages.success(request, 'Profile updated successfully')
        if new_password:
            auth_login(request, user)
        return redirect('first_storePages:home')
        
    return render(request, 'update_user.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            current_password = form.cleaned_data.get('current_password')
            new_password = form.cleaned_data.get('new_password')
            
            user = form.instance
            
            # Check if user wants to change password
            if new_password:
                # Verify current password using the raw password
                if not check_password(current_password, user.password):
                    messages.error(request, 'كلمة المرور الحالية غير صحيحة')
                    return render(request, 'profile.html', {'form': form})
                
                # Update password
                user.password = make_password(new_password)
            
            # Save the form
            form.save()
            
            if new_password:
                messages.success(request, 'تم تحديث الملف الشخصي وكلمة المرور بنجاح')
                # Update session to prevent logout
                update_session_auth_hash(request, user)
            else:
                messages.success(request, 'تم تحديث الملف الشخصي بنجاح')
            
            return redirect('first_storePages:profile')
        else:
            # If form is not valid, errors will be shown in the template
            pass
    else:
        form = UpdateProfileForm(instance=request.user)
    
    return render(request, 'profile.html', {'form': form})

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    return render(request, 'shop.html')

def about(request):
    return render(request, 'about.html')

@login_required
def orders(request):
    # Get user's orders
    return render(request, 'orders.html', {'user': request.user})

@login_required
def wishlist(request):
    # Get user's wishlist
    return render(request, 'wishlist.html', {'user': request.user})

@login_required
def cart(request):
    return render(request, 'cart.html')

@login_required
def checkout(request):
    return render(request, 'checkout.html')

def category(request):
    return render(request, 'category.html')

def quick_view(request):
    return render(request, 'quick_view.html')

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = Users.objects.filter(email=email).first()
            if user:
                try:
                    # Generate password reset token
                    token = default_token_generator.make_token(user)
                    uid = urlsafe_base64_encode(force_bytes(user.pk))
                    
                    # Build password reset link
                    reset_url = request.build_absolute_uri(
                        f'/password-reset-confirm/{uid}/{token}/'
                    )
                    
                    # Send email
                    subject = 'إعادة تعيين كلمة المرور'
                    email_template_name = 'password_reset_email.html'
                    context = {
                        'user': user,
                        'reset_url': reset_url,
                    }
                    email_content = render_to_string(email_template_name, context)
                    
                    try:
                        send_mail(
                            subject=subject,
                            message=email_content,
                            from_email=None,  # Will use DEFAULT_FROM_EMAIL from settings
                            recipient_list=[user.email],
                            fail_silently=False,
                        )
                        messages.success(request, 'تم إرسال رابط إعادة تعيين كلمة المرور إلى بريدك الإلكتروني.')
                    except Exception as e:
                        messages.error(request, f'حدث خطأ أثناء إرسال البريد الإلكتروني: {str(e)}')
                        return redirect('first_storePages:password_reset')
                    
                    return redirect('first_storePages:login')
                except Exception as e:
                    messages.error(request, f'حدث خطأ غير متوقع: {str(e)}')
                    return redirect('first_storePages:password_reset')
            else:
                messages.error(request, 'لم يتم العثور على مستخدم بهذا البريد الإلكتروني.')
        else:
            messages.error(request, 'يرجى تصحيح الأخطاء أدناه.')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})

def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Users.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Users.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(request.POST)
            if form.is_valid():
                user.password = make_password(form.cleaned_data['new_password'])
                user.save()
                messages.success(request, 'Password has been reset successfully.')
                return redirect('first_storePages:login')
        else:
            form = SetPasswordForm()
        return render(request, 'password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, 'Password reset link is invalid or has expired.')
        return redirect('first_storePages:login')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def is_rate_limited(request):
    ip = get_client_ip(request)
    key = f'login_attempts_{ip}'
    attempts = cache.get(key, 0)
    return attempts >= 5  # Limit to 5 attempts

def increment_login_attempts(request):
    ip = get_client_ip(request)
    key = f'login_attempts_{ip}'
    attempts = cache.get(key, 0)
    cache.set(key, attempts + 1, 300)  # Reset after 5 minutes

def test_email(request):
    try:
        send_mail(
            subject='Test Email',
            message='This is a test email from your Django application.',
            from_email=None,  # Will use DEFAULT_FROM_EMAIL
            recipient_list=['egyptabdo53@gmail.com'],
            fail_silently=False,
        )
        return HttpResponse('Test email sent successfully!')
    except Exception as e:
        return HttpResponse(f'Error sending email: {str(e)}')