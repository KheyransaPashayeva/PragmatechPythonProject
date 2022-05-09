from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied

class BlackListMiddleWare(MiddlewareMixin):
    ip_black_lists = ['127.0.0.2']

    def process_view(self, request, *args, **kwargs):
        ip = request.META['REMOTE_ADDR']
        if ip in self.ip_black_lists:
            raise PermissionDenied()

