from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'media' in request.path:
            return self.get_response(request)

        if not request.user.is_anonymous:

            if not request.user.is_staff:

                profile = request.user.profile

                if not profile.picture or not profile.biography:

                    if request.path not in [reverse('users:update'), reverse('users:logout')]:
                        url = reverse('users:update')
                        return redirect(url)

        response = self.get_response(request)

        return response
