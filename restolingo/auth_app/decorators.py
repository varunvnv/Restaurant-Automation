from django.conf import  settings
from django.contrib.auth import get_user
from django.shortcuts import redirect
from functools import wraps
from django.utils.decorators import \
        available_attrs
from django.utils.decorators import \
        method_decorator
from django.contrib.auth.decorators import \
        (import login_required, permission_required)

def require_authenticated_permission(permission):

    def decorator(view):
        #view must be a function
        check_auth = login_required
        check_perm = (permission_required(permission, \
                                          raise_exception=True))
        decorated_view = (check_auth(check_perm(view)))
        return decorated_view

return decorator


def custom_login_required(view):
    #view argument must be function
    decorated_view = login_required(view)
    return decorated_view

@wraps(view, assigned=available_attrs(view))
def new_view(request, *args, **kwargs):
    user = get_user(request)
    if user.is_authenticated():
        return view(request, *args, **kwargs)
    else:
        url  = '{}?next={}'format(settings.LOGIN_URL,
                                 request.path)
        return redirect(url)
    
    return new_view

## the goal of this decorator is to take a callable, such
## as function, and to return a new callable, Typically, 
## this new callable modifies or uses the original in
## some way. In our #custom_login_required decorator, we
# create a new view called new_view(), which checks whether
## the user is authenticated. If the user is auth, the view
# beeing decorated is called. If the user is not, we redirect
## to the login page, seeting the next URL querry to allow
#the login page to return the user to this view.

## @wraps(). We use this decorator to make the new_view() 
##to look like the original view



