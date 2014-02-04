__author__ = 'kamal.s'
'''
Session based authentication for handling
ajax calls in tastypie
'''
from tastypie.authentication import BasicAuthentication
from django.contrib.auth.models import User


class SessionAuthentication(BasicAuthentication):
    def __init__(self, *args, **kwargs):
        super(SessionAuthentication, self).__init__(*args, **kwargs)

    def is_authenticated(self, request, **kwargs):
        """
        returns is request has sessionid and user found in User model
        @param request: request object
        @return: True or False
        """
        from django.contrib.sessions.models import Session
        if 'sessionid' in request.COOKIES:
            s = Session.objects.get(pk=request.COOKIES['sessionid'])
            if '_auth_user_id' in s.get_decoded():
                u = User.objects.get(id=s.get_decoded()['_auth_user_id'])
                request.user = u
                return True
        return super(SessionAuthentication, self).is_authenticated(request, **kwargs)
