from django.shortcuts import render,redirect

# Create your views here.
from managerapp.forms import LoginForm, UserRegistrationForm, CreateTaskForm
from django.contrib.auth import login, authenticate



# Create your views here.
def index(request):
    return render(request,'main/index.html')




def account(request):

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        form = LoginForm(request.POST)
        
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('managerapp:account')
        # Note: You can use 'elif' instead of 'if' here
        elif form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])  # Fix password retrieval
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('managerapp:index')
                else:
                    return render(request, 'main/indexstart.html', {'form': form})
            else:
                return render(request, 'main/indexstart.html', {'form': form})
    else:
        user_form = UserRegistrationForm()
        form = LoginForm()
            
    return render(request,'main/indexstart.html', {'user_form': user_form, 'form': form})  # Pass both forms to the template

    #return render(request,'main/indexstart.html')


 #  ---------CreateTask------
def CreateTask(request):
    form = CreateTaskForm()

    if request.method == 'POST': 
       form = CreateTaskForm(request.POST)

       if form.is_valid():
           form.save()

           return redirect('')
    context = {'form': form}

    return render(request, 'main/tasks_list.html', context=context)
 