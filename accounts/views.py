from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):
    if(request.method == 'POST'):
      user_name = request.POST['user_name']
      password1 = request.POST['password1']
      password2 = request.POST['password2']
      if(password1 == password2):
        if(User.objects.filter(username=user_name).exists()):
          messages.info(request,'Username Taken')
          return render(request,'login.html')
        else:
          user = User.objects.create_user(username=user_name,password=password1)
          user.save()
          print("User Created")
          return render(request,'index.html')
      else:
        messages.info(request,'passwords doesnot match')
        return render(request,'login.html')
    else:
      return render(request, 'login.html')
    
def login(request):
  if(request.method == 'POST'):
    user_name = request.POST['user_name']
    password = request.POST['password']
    user = auth.authenticate(username = user_name,password = password)
    if user is not None:
      auth.login(request,user)
      return redirect('/')
    else:
      messages.info(request,'invalid credentials')
      return redirect('/login')
  else:
    return render(request,'login.html')

def logout(request):
  auth.logout(request)
  return render(request,'index.html')