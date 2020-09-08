from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import *


def home(request):
	o = Order.objects.all()
	c = Customers.objects.all()
	total_customers = c.count()
	total_orders = o.count()
	Delevered = o.filter(status='delevery').count()
	Pending = o.filter(status='pending').count()
	context = {'o':o,'c':c,'total_customers':total_customers,'total_orders':total_orders,'Delevered':Delevered,'Pending':Pending}
	return render(request, 'accounts/dashboard.html',context)

def products(request):
	p = Products.objects.all()

	return render(request, 'accounts/products.html', {'p':p})

def customers(request,pk_test):
	c = Customers.objects.get(id=pk_test)
	orders = c.order_set.all()
	order_count = orders.count()
	context={'c':c,'orders':orders,'orders_count':order_count}
	return render(request, 'accounts/customers.html',context)

def createOrder(request):
	c = Customers
	f = OrderForm()
	if request.method == "POST":
		f = OrderForm(request.POST)
		if f.is_valid():
			f.save()
			return redirect('/')
	context ={'f':f}
	return render(request,'accounts/order_form.html',context)


def updateOrder(request,pk):
	order = Order.objects.get(id=pk)
	f = OrderForm(instance=order)
	if request.method=="POST":
		f = OrderForm(request.POST,instance=order)
		if f.is_valid():
			f.save()
			return redirect('/')
	context={'f':f}
	return render(request,'accounts/order_form.html',context)

def delete(request,pk):
	item =  Order.objects.get(id=pk)
	if request.method == "POST":
		item.delete()
		return redirect('/')
	context={'item':item}
	return render(request,'accounts/delete.html',context)