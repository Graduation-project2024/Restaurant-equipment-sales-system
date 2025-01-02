from django.shortcuts import redirect
from django.urls import reverse
from .models import Users

class CustomAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if user is authenticated via session
        user_id = request.session.get('user_id')
        
        if user_id:
            try:
                # Get user from database
                user = Users.objects.get(usr_id=user_id)
                # Attach user to request
                request.user = user
                request.user.is_authenticated = True
            except Users.DoesNotExist:
                # Clear invalid session
                request.session.flush()
                request.user = None
        else:
            request.user = None

        response = self.get_response(request)
        return response
