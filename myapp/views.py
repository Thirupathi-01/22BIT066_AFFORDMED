from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import decorators
import random
# Create your views here.

def get_even(request, *args, **kwargs):
    if request.method != 'GET':
        return HttpResponse("Method not allowed", status=405)
    else:
        even_numbers = [i for i in range(101) if i % 2 == 0]
        return HttpResponse(f"Even numbers from 0 to 100: {even_numbers}")
    
def prime(request,*args, **kwargs):
    if request.method != 'GET':
        return HttpResponse("Method not allowed", status=405)
    else:
        l=[]
        for i in range(10):
            n=random.randint(1,100)
            flag=False
            for i in range(2,n/2):
                if n%i==0:
                    flag=True
                    break
            if flag:
                l.append(n)
        return HttpResponse(f"Prime numbers list:{l}")

def rand(request,*args,**kwargs):
    n=int(input())
    l=[]
    for i in range(n):
        ele=random.randint(0,100)
        l.append(ele)
    
    return HttpResponse(f"Random numbers:{l}")

def fibo(request,*args,**kwargs):
    if request.method != 'GET':
        return HttpResponse("Method not allowed", status=405)
    
    n = int(request.GET.get('n', 10))
    l = []
    a, b = 0, 1
    for _ in range(n):
        l.append(a)
        a, b = b, a + b
    return HttpResponse(f"fibonacci series: {l}")






