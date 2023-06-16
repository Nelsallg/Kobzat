from django.shortcuts import render,redirect
from django.contrib import messages
from users.forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, login
# Create your views here.

"""Renders the registration form page."""
def register(request, title=None, year=None):
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


def login_view(request,title=None,year=None):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Remplacez 'accueil' par le nom de votre vue d'accueil
        else:
            error_message = 'Identifiants invalides. Veuillez réessayer.'
            context = {'form':form,'error_message':error_message,'title': title,'year':year}
            return render(request, 'app/login.html', context)
    else:
        form = AuthenticationForm()
        error_message = ''
        context = {'form':form,'error_message':error_message,'title': title,'year':year}
    return render(request, 'app/login.html', context)

