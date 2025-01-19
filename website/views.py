from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


def home(request):
    records = Record.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You've been logged in")
            return redirect("home")
        else:
            messages.warning(request, "A mistake occured, Try one more time")
            return redirect("home")
    else:
        return render(request, "home.html", {"records": records})


def logout_user(request):
    logout(request)
    messages.success(request, "You logged out")
    return redirect("home")


def register_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You've been registered in")
            return redirect("home")
        else:
            messages.error(request, "An error occured during registration")

    return render(request, "register.html", {"form": form})


def record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        return render(request, "record.html", {"record": record})
    else:
        messages.error(request, "You have to login")
        return redirect("home")


def delete_record(request, pk):
    if request.user.is_authenticated:
        del_record = Record.objects.get(id=pk)
        del_record.delete()
        messages.success(request, "You deleted the record")
        return redirect("home")
    else:
        messages.error(request, "You have to login")
        return redirect("home")


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            add_record = form.save()
            messages.success(request, f"Record {add_record.first_name} was added")
            return redirect("home")
        return render(request, "add_record.html", {"form": form})
    else:
        messages.error(request, "You have to login")
        return redirect("home")


def update_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=record)
        if form.is_valid():
            updated_record = form.save()
            messages.success(request, f"Record '{updated_record.first_name}' was added")
            return redirect("home")
        return render(request, "update_record.html", {"form": form})
    else:
        messages.error(request, "You have to login")
        return redirect("home") 

from django.shortcuts import render, get_object_or_404
from .models import Customer, Product, Order, Employee, Supplier

# Views for Customer
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer_detail.html', {'customer': customer})

# Views for Product
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

# Views for Order
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order_detail.html', {'order': order})

# Views for Employee
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})

# Views for Supplier
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_list.html', {'suppliers': suppliers})

def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request, 'supplier_detail.html', {'supplier': supplier})
