from django.shortcuts import render

# Create your views here.



def home(request):
    # return HttpResponse("Hello, world. You're at the home page.")

    return render(request,'app/index.html')