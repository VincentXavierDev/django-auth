# This project use custom user model not use built-in django fields
# Setting
    - Python version 3.9.10
# Step by step to create a newspaper app

1. Setting
1.1 Create environment
    - python -m venv .venv
1.2 Active this env
    - .venv\Scripts\activate
1.3 Install django (Current version of django: 4.1.7)
    - pip install django

2. Start project
2.1 Create app with name's config
    - django-admin startproject config .
2.2 Create account app
    - python manage.py startapp accounts

3. Custom user model 
3.1 update config/setting.py
    - All line has comment #3.1
3.2 update accounts/models
    - All line has comment #3.2
3.3 create form.py within accounts to custom : UserCreationForm and UserChangeForm
    - All line has comment #3.3
3.4 update admin.py after custom user model
    - All line has comment #3.4

4. Migrate to database
4.1 Config to use MySQL database
4.1.1 instal require lib
    - pip install mysql-connector-python
    - pip install mysqlclient
4.1.2 update config/settings.py
    - All line has comment #4.1.2

5. Create superuser to confirm that everything is working as expected
    - python manage.py createsuperuser
    - account: xuanvinh|09092000|vinhdao992000@gmail.com
5.1 As view has many fields on admin dashboard 
    - All line has comment #5.1
    - To config display fields and editable it we use
    list_display: to allow fields display
    fieldsets: to allow editable in admin dashboard
6. Create a templates
    - mkdir templates/templates
    - mkdir templates/templates/registration 
6.1 Tell django this template dir in config/settings.py
    - All line has comment #6.1
7. Declare url redirect after login or logout
    - All line has comment #7
    - create templates UI  templates/base.html, templates/home.html, templates/registration/login.html, templates/registration/signup.html

8. Update config/urls.py
    - All line has comment #8

# Notes: If you want to custom auth template django built-in. Only change UI within html files has name below in registration folder. Django will auto overwrite

registration/login.html: This template is used for the login page.
registration/logged_out.html: This template is used after the user has logged out.
registration/password_change_form.html: This template is used for the password change form.
registration/password_change_done.html: This template is used after the user has changed their password.
registration/password_reset_form.html: This template is used for the password reset form.
registration/password_reset_email.html: This template is used for the email that is sent to the user when they request a password reset.
registration/password_reset_done.html: This template is used after the email has been sent to the user.
registration/password_reset_confirm.html: This template is used for the password reset confirmation page.
registration/password_reset_complete.html: This template is used after the password has been reset.

# The built-in function CRUD in django We can overwrite:

# CreateView
model: The model that the view will be used to create instances of. You can override this to use a different model.
form_class: The form class that the view will use to validate and save data. You can override this to use a different form class.
template_name: The name of the template that the view will use to render the form. You can override this to use a different template.
success_url: The URL that the view will redirect to after a successful submission. You can override this to use a different URL.
form_valid(form): A method that is called when the form is valid. You can override this to customize the behavior of the view when the form is valid.
# UpdateView
model: The model that the view will be used to update instances of. You can override this to use a different model.
form_class: The form class that the view will use to validate and save data. You can override this to use a different form class.
template_name: The name of the template that the view will use to render the form. You can override this to use a different template.
success_url: The URL that the view will redirect to after a successful submission. You can override this to use a different URL.
form_valid(form): A method that is called when the form is valid. You can override this to customize the behavior of the view when the form is valid.
# DeleteView
model: The model that the view will be used to delete instances of. You can override this to use a different model.
template_name: The name of the template that the view will use to render the confirmation form. You can override this to use a different template.
success_url: The URL that the view will redirect to after a successful deletion. You can override this to use a different URL.
delete(self, request, *args, **kwargs): A method that is called when the deletion is confirmed. You can override this to customize the behavior of the view when the object is deleted.

# Some django built-in popular
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.base import RedirectView
from django.core.paginator import Paginator
from django.db import models
from django import forms