from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
#from first_app.models import AccessRecord,Topic,Webpage
from first_app.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
# def index(request):
#     webpages_list = AccessRecord.objects.order_by('date')
#     date_dict = {'access_records':webpages_list}
#     return render(request,'first_app/index.html',context=date_dict)
#
# def help(request):
#     return render(request,'first_app/help.html')

def index(request):
    return render(request,'first_app/index.html')

# def form_name_view(request):
#     form = forms.FormName()
#     return render(request,'first_app/form_page.html',{'form':form})

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile_user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'first_app/register.html',
                            {'user_form':user_form,
                              'profile_form':profile_form,
                              'registered':registered})

@login_required
def special(request):
    return HttpResponse('Your logged in')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("someone tried to login and falied")
            print("username {} and password {}".format(username,password))
            return HttpResponse("Invalid login credentials")

    else:
        return render(request,'first_app/login.html',{} )
