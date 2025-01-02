from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse

def login_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if not request.session.get('user_id'):
            # Store the requested URL in session
            request.session['next'] = request.get_full_path()
            return redirect('first_storePages:login')
        return function(request, *args, **kwargs)
    return wrap
