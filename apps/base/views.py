"""Views for base app."""

from django.http import JsonResponse
from django.views import View
from django.utils import timezone
from django.conf import settings

class HelloView(View):
    """A simple view that returns a standardized JSON response."""

    def get(self, request, *args, **kwargs):
        """Handle GET requests and return a standardized JSON response."""
        response = {
            "success": True,
            "timestamp": timezone.now().isoformat(),
            "timezone": str(settings.TIME_ZONE),
            "data": {
                "message": "Welcome to roneha.dev. Your request was successful.",
                "version": "1.0.1",
                "main_url": "https://ridwaanhall.com"
            },
            "meta": {
                "code": 200,
                "request_id": request.META.get("HTTP_X_REQUEST_ID", None)
            }
        }
        return JsonResponse(response, status=200)
