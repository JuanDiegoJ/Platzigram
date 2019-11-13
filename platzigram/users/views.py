"""users views"""

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from django.db.utils import IntegrityError
from users.forms import ProfileForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
    return render(request, 'users/login.html')

def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
            
            return redirect('update_profile')
    else:
        form = ProfileForm()

    return render(
        request = request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )
    
    

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        #Datos de entrada
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']
        #Valida la contraseña
        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error':'Password confirmation does not match'})
        #Ejecuta la excepción si el usuario ya está creado en la BD
        try:
            user = User.objects.create_user(username=username, password = passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error':'User is already user'})
        
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        #Siempre guardar el usuario
        user.save()
        #Se crea un perfil pero no se ingresan los datos del perfil
        profile = Profile(user=user)
        profile.save()

        return redirect('login')
    return render(request, 'users/signup.html')
