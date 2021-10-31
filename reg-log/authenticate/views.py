from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def home(request):
    return render(request, 'authenticate/form.html')

# Here is some bug and i followed a tutorial django version 2.0 for this reason it's missmatching
def login_user(request):
    if request.method == 'POST':
        if request.method == "POST":
            username = request.POST['username']
            print(username)
            password = request.POST['password']
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('login')
            else:
                return redirect('form')
    else:
        return render(request,'authenticate/form.html')
