from django.http import HttpResponseRedirect
from google.appengine.api import users
from django.core.urlresolvers import reverse

def login(request):
    """Redirects to the Google App Engine authentication page."""

    url = users.create_login_url(dest_url=request.GET.get('next'))
    return HttpResponseRedirect(url)

def logout(requesr):
    """Redirects to the homepage after logging the user out."""

    url = users.create_logout_url(reverse('index'))
    return HttpResponseRedirect(url)
