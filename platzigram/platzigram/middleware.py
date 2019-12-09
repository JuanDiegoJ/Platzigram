from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    #Método de inicialización
    def __init__(self, get_response):
        self.get_response = get_response
    #Método que valida que el usuario en dado caso de no tener una foto de perfil no lo
    #deje irse a otra página

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('update_profile'), reverse('logout')]:
                        return redirect('update_profile')

        response = self.get_response(request)
        return response