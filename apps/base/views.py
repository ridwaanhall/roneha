"""Views for base app."""
from django.http import JsonResponse
from django.views import View

class HelloView(View):
    """A simple view that returns a JSON response with a welcome message."""

    def get(self, request, *args, **kwargs):
        """Handle GET requests and return a JSON response."""
        return JsonResponse({
            "code": 200,
            "status": "success",
            "data": {
                "message": "Welcome to roneha.dev. Your request was successful.",
                "version": "1.0.0",
                "main_url": "https://ridwaanhall.com"
            }
        })
