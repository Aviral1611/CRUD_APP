from django.shortcuts import render,redirect
from .forms import CreateUserForm, LoginForm, AddRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Customer

def home(request):

    return render(request,'app/index.html')


#- Register a User


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('my-login')

    context = {'form':form}

    return render(request, 'app/register.html',context=context)


# login a user

def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data = request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context = {'form2':form}

    return render(request, 'app/my-login.html', context = context)


# -- dashboard

@login_required(login_url='my-login')
def dashboard(request):

    my_customer = Customer.objects.all()

    context = {'records': my_customer}

    return render(request, 'app/dashboard.html',context=context)


# CREATE A RECORD --

@login_required(login_url='my-login')
def create_record(request):

    form = AddRecordForm()

    if request.method == "POST":
        form = AddRecordForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect ('dashboard')
        
    context = {'form3':form}

    return render(request,'app/create-record.html',context=context)

#Update record

@login_required(login_url='my-login')
def update_record(request,pk):

    record = Customer.objects.get(id=pk)

    form = UpdateRecordForm(instance = record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST,instance = record)

    if form.is_valid():
        form.save()

        return redirect('dashboard')
    
    context = {'form4':form}

    return render(request,'app/update-record.html',context=context)

# view a record
@login_required(login_url='my-login')
def one_record(request,pk):

    all_records = Customer.objects.get(id=pk)

    context = {'record' :all_records}

    return render(request,'app/view-record.html',context = context)











# user logout

def user_logout(request):
    auth.logout(request)

    return redirect('my-login')

            