from django.shortcuts import render,redirect
from django.contrib import messages
from users.forms import UserRegistrationForm
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
