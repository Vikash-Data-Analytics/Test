
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from .models import users

from django.views import View


class user(View):
    def get(self, request):
        return render (request, 'user.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        department = postData.get ('department')
        ctc = postData.get('CTC')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
            'department':department,
            'ctc':ctc
        }
        error_message = "Enter Correct Inputs."

        user = users (first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             department=department,
                             ctc = ctc)
        error_message = self.validateCustomer (user)

        if not error_message:
            print (first_name, last_name, phone, email, department, ctc)
            user.register ()
            return redirect ('user')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'user.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "Please Enter your First Name !!"
        elif len (customer.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not customer.last_name:
            error_message = 'Please Enter your Last Name'
        elif len (customer.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not customer.phone:
            error_message = 'Enter your Phone Number'
        elif len (customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len (customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists ():
            error_message = 'Email Address Already Registered..'
        return error_message


