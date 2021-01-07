from django.shortcuts import render
from django.http import JsonResponse

def employee_view(request):
    emp = {
        'id': 123,
        'name': 'Roger',
        'salary': 1000
    }
    return JsonResponse(emp)
