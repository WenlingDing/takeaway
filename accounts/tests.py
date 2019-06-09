from django.test import TestCase

# Create your tests here.
from .forms import LoginForm,RegisterUserForm

class TestLoginForm(TestCase):

    def test_can_login_with_just_username(self):
        form = LoginForm({'username': 'Create Tests'})
        self.assertFalse(form.is_valid())
    
    def test_correct_message_for_missing_username(self):
        form = LoginForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])
        
    def test_can_login_with_just_password(self):
        form = LoginForm({'password': '99990000'})
        self.assertFalse(form.is_valid())
    
    def test_correct_message_for_missing_password(self):
        form = LoginForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [u'This field is required.'])
        
 
class TestRegisterUserForm(TestCase):

    def test_can_register_with_just_username(self):
        form = RegisterUserForm({'username': 'Create Tests'})
        self.assertFalse(form.is_valid())
    
    def test_correct_message_for_missing_username(self):
        form =RegisterUserForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])
        
    def test_can_register_with_just_password1(self):
        form = RegisterUserForm({'password1': '99990000'})
        self.assertFalse(form.is_valid())
    
    def test_correct_message_for_missing_password1(self):
        form = RegisterUserForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password1'], [u'This field is required.'])
        
    def test_can_register_with_just_password2(self):
        form = RegisterUserForm({'password1': '99990000'})
        self.assertFalse(form.is_valid())
    
    def test_correct_message_for_missing_password2(self):
        form = RegisterUserForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'This field is required.'])
        
    def test_can_register_with_just_email(self):
        form = RegisterUserForm({'email': 'dwl@dwl.com'})
        self.assertFalse(form.is_valid())
    
    def test_correct_message_for_missing_email(self):
        form = RegisterUserForm({'form': ''})
        self.assertFalse(form.is_valid())
       