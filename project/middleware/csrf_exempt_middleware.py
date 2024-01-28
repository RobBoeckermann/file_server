from django.views.decorators.csrf import csrf_exempt

class CsrfExemptMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Apply the csrf_exempt decorator to all views.
        request.csrf_processing_done = True
        response = self.get_response(request)
        return response
