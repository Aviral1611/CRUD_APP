from django.shortcuts import render,redirect

from .forms import CreateUserForm, LoginForm

# Create your views here.



def home(request):
    # return HttpResponse("Hello, world. You're at the home page.")

    return render(request,'app/index.html')




#- Register a User



def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            # return redirect('')

    context = {'form':form}

    return render(request, 'app/register.html',context=context)