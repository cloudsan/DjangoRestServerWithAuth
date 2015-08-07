from django.http import HttpResponse
from django.contrib.auth import login
from rest_framework import generics
from social.apps.django_app.utils import psa
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from .tools import get_access_token
from django.views.decorators.csrf import csrf_exempt

# When we send a third party access token to that view
# as a GET request with access_token parameter,
# python social auth communicate with
# the third party and request the user info to register or
# sign in the user. Magic. Yeah.


@csrf_exempt
@psa('social:complete')
def register_by_access_token(request, backend):

    token = request.POST.get('access_token')
    # here comes the magic
    user = request.backend.do_auth(token)

    if user:
        login(request, user)

        # that function will return our own
        # OAuth2 token as JSON
        response = get_access_token(user)
        response['access-control-allow-origin'] = '*'
        return response
    else:
        response = HttpResponse("error")
        response['access-control-allow-origin'] = '*'
        # If there was an error... you decide what you do here
        return response


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
