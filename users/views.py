from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
       if request.method  == 'POST':
              form = UserRegisterForm(request.POST)
              if form.is_valid():
                     form.save()
                     username = form.cleaned_data.get('username')
                     message.success(request, f'Account created for {username}!')
                     return redirect('blog-home')
       else:
              form = UserRegisterationtionForm()
              return render(request, 'users/register.html', {'form':form})           
        