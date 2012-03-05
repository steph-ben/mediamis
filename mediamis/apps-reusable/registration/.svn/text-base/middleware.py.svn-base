from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

class LoginFormMiddleware(object):
    def process_request(self, request):
        # if the top login form has been posted
        if request.method == 'POST' and \
           'username' in request.POST and \
           'password' in request.POST:
            # validate the form
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                # log the user in
                login(request, form.get_user())
        else:
            form = AuthenticationForm(request)
        # attach the form to the request so it can be accessed within the templates
        request.auth_form = form
