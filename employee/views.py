from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import Employee
from django.http import HttpResponse, JsonResponse

# Create your templates here.
def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                employee = form.save()
                return JsonResponse({
                    'success': True,
                    'employee': {
                        'id': employee.id,
                        'name': employee.employee_name,
                        'email': employee.employee_email,
                        'contact': employee.employee_contact,
                    }
                })
            except:
                return JsonResponse({'success': False})
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})

def show(request):
    employees = Employee.objects.all().values()
    # loop
    employee_list = []
    for employee in employees:
        employee_dic = {
            'id': employee['id'],
            'name': employee['employee_name'],
            'email': employee['employee_email'],
            'contact': employee['employee_contact'],
        }
        employee_list.append(employee_dic)
    return JsonResponse({
        'success': True,
        'employee': employee_list
    })

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return JsonResponse({
        'success': True,
        'employee': {
            'id': employee.id,
            'name': employee.employee_name,
            'email': employee.employee_email,
            'contact': employee.employee_contact,
        }
    })
# def checkout(request, id):
#     employees = Employee.objects.get(id=id)
#     return JsonResponse({
#         'success': True,
#         'employee': {
#             'id': employees.id,
#             'name': employees.employee_name,
#             'email': employees.employee_email,
#             'contact': employees.employee_contact,
#         }
#     })
#
#
# def checkoutpay(request, id):
#     shoes = Shoes.objects.get(id=id)
#     if request.method == 'POST':
#         amount = shoes.price
#         phoneNumber = request.POST.get('contact')
#         if not phoneNumber or not phoneNumber.isdigit:
#             return HttpResponse('invalid phone number')
#         if not amount or not amount.isdigit:
#             return HttpResponse('invalid price')
#         cl = MpesaClient()
#         phone_number = int(phoneNumber)
#         amount = int(amount)
#         account_reference = 'SELL SHOES'
#         transaction_desc = 'paying shoes'
#         callback_url = 'https://api.darajambili.com/express-payment'
#         response = cl.stk_push(str(phone_number), amount, account_reference, transaction_desc, callback_url)
#         return HttpResponse(response)
#     else:
#         return render(request, "checkout.html", {"shoes": shoes})
#

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        employee = form.save()
        return JsonResponse({
            'success': True,
            'employee': {
                'id': employee.id,
                'name': employee.employee_name,
                'email': employee.employee_email,
                'contact': employee.employee_contact,
            }
        })

    return JsonResponse({'success': False})

def destory(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return JsonResponse({'success':True, 'message': 'Data has been deleted'})
