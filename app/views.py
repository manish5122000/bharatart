from django.shortcuts import redirect, render
from .models import Support_User_Sponser_detail
from .forms import RegistrationForm, Sponser_id_form

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def Sponser_id(request):
    return render(request, 'app/sponser_id.html')  

def Signup(request):
    if request.method == 'POST':
        r_form = RegistrationForm(request.POST)
        s_form = Sponser_id_form(request.POST)
        if r_form.is_valid() and s_form.is_valid():
            user = r_form.save()
            user.is_active = True
            s_form.instance.user = user
            s_form.save()
            return redirect('/')
    else:
        r_form = RegistrationForm()
        s_form = Sponser_id_form()
    return render(request, 'app/register.html',{'r_form': r_form, 's_form': s_form})

def Login(request):
    return render(request, 'app/login.html')

def Profile(request):
    p_form = Support_User_Sponser_detail.objects.filter(user=request.user)
    return render(request, 'app/profile.html',{'p_form':p_form})

def Logout(request):
    return render(request, 'app/logout.html')