from django import forms
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from .models import Users

class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'box', 'autocomplete': 'new-password'}),
        label="",
        required=True,
    )

    class Meta:
        model = Users
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'box'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'box'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'box', 'autocomplete': 'new-password'}),
        }
        labels = {
            'username': '',
            'email': '',
            'password': '',
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Users.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Users.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
    
class SignInForm(forms.Form):
    identifier = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'اسم المستخدم أو البريد الإلكتروني',
            'id': 'identifier',
            'name': 'identifier'
        }),
        label="",
        required=True,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'كلمة المرور',
            'id': 'password',
            'name': 'password',
            'autocomplete': 'current-password'
        }),
        label="",
        required=True,
    )

    def clean(self):
        cleaned_data = super().clean()
        identifier = cleaned_data.get("identifier")
        password = cleaned_data.get("password")

        if identifier and password:
            # Try to find user by username or email
            user = Users.objects.filter(username=identifier).first() or Users.objects.filter(email=identifier).first()
            
            if user is None:
                raise forms.ValidationError("لا يوجد حساب بهذا الاسم أو البريد الإلكتروني")
            
            if not check_password(password, user.password):
                raise forms.ValidationError("كلمة المرور غير صحيحة")
            
            # Store the user object for the view to use
            cleaned_data['user'] = user
            
        return cleaned_data

class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={'class': 'box', 'placeholder': 'أدخل بريدك الإلكتروني'})
    )

class SetPasswordForm(forms.Form):
    new_password = forms.CharField(
        label='كلمة المرور الجديدة',
        widget=forms.PasswordInput(attrs={'class': 'box', 'placeholder': 'أدخل كلمة المرور الجديدة'}),
        min_length=8
    )
    confirm_password = forms.CharField(
        label='تأكيد كلمة المرور',
        widget=forms.PasswordInput(attrs={'class': 'box', 'placeholder': 'أكد كلمة المرور الجديدة'})
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password and confirm_password:
            if new_password != confirm_password:
                raise ValidationError('كلمات المرور غير متطابقة')

        # Password validation
        if new_password:
            if not any(char.isupper() for char in new_password):
                raise ValidationError('يجب أن تحتوي كلمة المرور على حرف كبير واحد على الأقل')
            if not any(char.islower() for char in new_password):
                raise ValidationError('يجب أن تحتوي كلمة المرور على حرف صغير واحد على الأقل')
            if not any(char.isdigit() for char in new_password):
                raise ValidationError('يجب أن تحتوي كلمة المرور على رقم واحد على الأقل')
            if not any(char in '!@#$%^&*()' for char in new_password):
                raise ValidationError('يجب أن تحتوي كلمة المرور على رمز خاص واحد على الأقل (!@#$%^&*())')

        return cleaned_data

class UpdateProfileForm(forms.ModelForm):
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'كلمة المرور الحالية',
        }),
        required=False
    )
    
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'كلمة المرور الجديدة',
        }),
        required=False,
        help_text='يجب أن تحتوي كلمة المرور على 8 أحرف على الأقل، وحرف كبير، ورقم، ورمز خاص'
    )
    
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'تأكيد كلمة المرور الجديدة',
        }),
        required=False
    )

    class Meta:
        model = Users
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'اسم المستخدم'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'البريد الإلكتروني'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data.get('current_password')
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        
        # Only validate password if user is trying to change it
        if new_password or current_password or confirm_password:
            if not current_password:
                raise forms.ValidationError('يجب إدخال كلمة المرور الحالية لتغيير كلمة المرور')
            
            if not new_password:
                raise forms.ValidationError('يجب إدخال كلمة المرور الجديدة')
            
            if not confirm_password:
                raise forms.ValidationError('يجب تأكيد كلمة المرور الجديدة')
            
            if new_password != confirm_password:
                raise forms.ValidationError('كلمة المرور الجديدة غير متطابقة')
            
            # Password validation
            if len(new_password) < 8:
                raise forms.ValidationError('يجب أن تحتوي كلمة المرور على 8 أحرف على الأقل')
            
            if not any(char.isupper() for char in new_password):
                raise forms.ValidationError('يجب أن تحتوي كلمة المرور على حرف كبير واحد على الأقل')
            
            if not any(char.isdigit() for char in new_password):
                raise forms.ValidationError('يجب أن تحتوي كلمة المرور على رقم واحد على الأقل')
            
            if not any(char in '!@#$%^&*()' for char in new_password):
                raise forms.ValidationError('يجب أن تحتوي كلمة المرور على رمز خاص واحد على الأقل (!@#$%^&*())')
        
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username != self.instance.username and Users.objects.filter(username=username).exists():
            raise forms.ValidationError('اسم المستخدم مستخدم بالفعل')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email != self.instance.email and Users.objects.filter(email=email).exists():
            raise forms.ValidationError('البريد الإلكتروني مستخدم بالفعل')
        return email