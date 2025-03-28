from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from .models import ScreenPermission

class ScreenPermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not getattr(settings, 'PERMISSION_CHECK_ENABLED', True):
            return self.get_response(request)
        
        if request.path == '/permissions/no-permission/':
            return self.get_response(request)



        if request.user.is_authenticated:
            path = request.path
            permission = ScreenPermission.objects.filter(
                user=request.user,
                screen_name = path,
                can_access=True
            ).exists()
            if not permission:
                return redirect(reverse('permissions:no_permission'))
        
        response = self.get_response(request)
        return response