from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from app.forms import UserAuthenticationForm
# Create your views here.


"""Renders the registration form page."""
def registerView(request, title=None, year=None):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Votre compte a été créé avec succès. Vous pouvez désormais vous connecter.")
            return redirect('login')
        else:
            # Récupérer les erreurs de UserCreationForm
            user_creation_form_errors = form['password1'].errors + form['password2'].errors
            # Supprimer les erreurs de UserCreationForm du formulaire principal
            form.errors.pop('password1', None)
            form.errors.pop('password2', None)
            
            context = {
                'registration_form': form,
                'user_creation_form_errors': user_creation_form_errors,
                'title': title,
                'year':year
            }
            return render(request, 'users/register.html', context)
    else:
        form = UserRegistrationForm()
        
    context = {'registration_form':form,'title': title,'year':year}
    return render(request, 'users/register.html', context)


def loginView(request,title=None,year=None):
    messages.get_messages(request)
    form = UserAuthenticationForm()
    username = ''
        
    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
            
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(f"username:{username}, user:{user}")
            
        if user is not None:
            login(request, user)
            return redirect('home')  # Remplacez 'accueil' par le nom de votre vue d'accueil
        else:
            error_message = 'Identifiants invalides. Veuillez réessayer.'
            context = {'form':form,'error':error_message,'title': title,'year':year}
            return render(request, 'app/login.html', context)
    else:
        error_message = ''
        context = {'form':form,'error_message':error_message,'title': title,'year':year}
    return render(request, 'app/login.html', context)
    
# @login_required
# def profileView(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(
#             request.POST, request.FILES, instance=request.user.profile)

#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, "Your account has been updated!")
#             return redirect('profile')

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#     return render(request, 'users/profile.html', context)