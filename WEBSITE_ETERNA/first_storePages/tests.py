from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from .models import Users, Roles
from django.test.utils import override_settings
from django.test.runner import DiscoverRunner

class NoMigrationTestRunner(DiscoverRunner):
    """A test runner to test without migrations"""
    def setup_databases(self, **kwargs):
        # Override the setup_databases to not create a test database
        return None

    def teardown_databases(self, old_config, **kwargs):
        # Override the teardown_databases to not destroy the test database
        pass

@override_settings(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'test_restaurant_equipment_sales_system',
            'USER': 'root',
            'PASSWORD': '012053aA',
            'HOST': '127.0.0.1',
            'PORT': '3305',
        }
    },
    TEST_RUNNER='APPs.store.tests.NoMigrationTestRunner'
)
class LoginTest(TestCase):
    def setUp(self):
        # Create a test role
        self.role = Roles.objects.create(
            rol_id=1,
            rol_name='user'
        )
        
        # Create a test user
        self.user = Users.objects.create(
            usr_id=1,
            rol=self.role,
            username='testuser',
            email='testuser@example.com',
            password=make_password('Test@123')
        )
        
        self.client = Client()
        self.login_url = reverse('first_storePages:login')
        self.home_url = reverse('first_storePages:home')

    def test_login_page_loads(self):
        """Test that login page loads correctly"""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_login.html')

    def test_login_with_username(self):
        """Test login with valid username and password"""
        response = self.client.post(self.login_url, {
            'identifier': 'testuser',
            'password': 'Test@123'
        })
        self.assertRedirects(response, self.home_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_with_email(self):
        """Test login with valid email and password"""
        response = self.client.post(self.login_url, {
            'identifier': 'testuser@example.com',
            'password': 'Test@123'
        })
        self.assertRedirects(response, self.home_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_with_invalid_password(self):
        """Test login with invalid password"""
        response = self.client.post(self.login_url, {
            'identifier': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username/email or password')

    def test_login_with_nonexistent_user(self):
        """Test login with non-existent user"""
        response = self.client.post(self.login_url, {
            'identifier': 'nonexistentuser',
            'password': 'anypassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'User not found')

    def test_login_with_empty_fields(self):
        """Test login with empty fields"""
        response = self.client.post(self.login_url, {
            'identifier': '',
            'password': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'identifier', 'This field is required.')
        self.assertFormError(response, 'form', 'password', 'This field is required.')

    def test_session_persistence(self):
        """Test that login session persists across pages"""
        # Login first
        self.client.post(self.login_url, {
            'identifier': 'testuser',
            'password': 'Test@123'
        })
        
        # Test accessing protected pages
        protected_urls = [
            reverse('first_storePages:cart'),
            reverse('first_storePages:wishlist'),
            reverse('first_storePages:orders'),
            reverse('first_storePages:checkout')
        ]
        
        for url in protected_urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_logout(self):
        """Test logout functionality"""
        # Login first
        self.client.post(self.login_url, {
            'identifier': 'testuser',
            'password': 'Test@123'
        })
        
        # Then logout
        response = self.client.get(reverse('first_storePages:logout'))
        self.assertRedirects(response, self.login_url)
        
        # Verify user is logged out
        response = self.client.get(reverse('first_storePages:cart'))
        self.assertRedirects(response, f'{self.login_url}?next={reverse("first_storePages:cart")}')


class RegistrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('first_storePages:register')
        self.role = Roles.objects.create(rol_id=1, rol_name='user')

    def test_register_page_loads(self):
        """Test that registration page loads correctly"""
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_register.html')

    def test_successful_registration(self):
        """Test successful user registration"""
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'Test@123',
            'confirm_password': 'Test@123'
        })
        self.assertRedirects(response, reverse('first_storePages:login'))
        self.assertTrue(Users.objects.filter(username='newuser').exists())

    def test_registration_with_existing_username(self):
        """Test registration with existing username"""
        Users.objects.create(
            username='existinguser',
            email='existing@example.com',
            password=make_password('Test@123'),
            rol=self.role
        )
        response = self.client.post(self.register_url, {
            'username': 'existinguser',
            'email': 'new@example.com',
            'password': 'Test@123',
            'confirm_password': 'Test@123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username already exists')


class ProfileUpdateTest(TestCase):
    def setUp(self):
        self.role = Roles.objects.create(rol_id=1, rol_name='user')
        self.user = Users.objects.create(
            username='testuser',
            email='testuser@example.com',
            password=make_password('Test@123'),
            rol=self.role
        )
        self.client = Client()
        self.update_url = reverse('first_storePages:update')
        self.client.login(username='testuser', password='Test@123')

    def test_update_profile_page_requires_login(self):
        """Test that profile update page requires login"""
        self.client.logout()
        response = self.client.get(self.update_url)
        self.assertRedirects(response, f"{reverse('first_storePages:login')}?next={self.update_url}")

    def test_successful_profile_update(self):
        """Test successful profile update"""
        response = self.client.post(self.update_url, {
            'name': 'updateduser',
            'email': 'updated@example.com',
            'old_pass': 'Test@123',
            'new_pass': 'NewTest@123',
            'cpass': 'NewTest@123'
        })
        self.assertRedirects(response, reverse('first_storePages:home'))
        updated_user = Users.objects.get(id=self.user.id)
        self.assertEqual(updated_user.username, 'updateduser')
        self.assertEqual(updated_user.email, 'updated@example.com')


class ProtectedRoutesTest(TestCase):
    def setUp(self):
        self.role = Roles.objects.create(rol_id=1, rol_name='user')
        self.user = Users.objects.create(
            username='testuser',
            email='testuser@example.com',
            password=make_password('Test@123'),
            rol=self.role
        )
        self.client = Client()

    def test_protected_routes_redirect_to_login(self):
        """Test that protected routes redirect to login for unauthenticated users"""
        protected_urls = [
            reverse('first_storePages:orders'),
            reverse('first_storePages:wishlist'),
            reverse('first_storePages:cart'),
            reverse('first_storePages:checkout'),
            reverse('first_storePages:update')
        ]
        for url in protected_urls:
            response = self.client.get(url)
            self.assertRedirects(response, f"{reverse('first_storePages:login')}?next={url}")

    def test_protected_routes_accessible_after_login(self):
        """Test that protected routes are accessible after login"""
        self.client.login(username='testuser', password='Test@123')
        protected_urls = [
            reverse('first_storePages:orders'),
            reverse('first_storePages:wishlist'),
            reverse('first_storePages:cart'),
            reverse('first_storePages:checkout'),
            reverse('first_storePages:update')
        ]
        for url in protected_urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)


class BasicPageLoadTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_public_pages_load(self):
        """Test that public pages load correctly"""
        public_urls = [
            reverse('first_storePages:home'),
            reverse('first_storePages:search'),
            reverse('first_storePages:contact'),
            reverse('first_storePages:shop'),
            reverse('first_storePages:about'),
            reverse('first_storePages:category'),
            reverse('first_storePages:quick_view')
        ]
        for url in public_urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)