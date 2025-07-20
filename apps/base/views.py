"""Views for the base app."""

import uuid
import time
from django.http import JsonResponse
from django.views import View
from django.utils import timezone
from django.conf import settings

class HelloView(View):
    """A simple view that returns a standardized JSON response."""

    def get(self, request, *args, **kwargs):
        """Handle GET requests and return a standardized JSON response."""
        start_time = time.perf_counter()
        request_id = self._get_request_id(request)
        environment = getattr(settings, "ENVIRONMENT", "production")
        timestamp = timezone.now().isoformat()
        timezone_str = str(settings.TIME_ZONE)
        elapsed_ms = None

        data = {
            "message": "Welcome to roneha.dev. Your request was successful.",
            "version": "1.0.1",
            "main_url": "https://ridwaanhall.com"
        }

        meta = {
            "code": 200,
            "request_id": request_id
        }

        response = self._build_response(
            success=True,
            status="OK",
            timestamp=timestamp,
            timezone=timezone_str,
            environment=environment,
            elapsed_ms=elapsed_ms,
            data=data,
            meta=meta,
            developer_note="Powered by roneha.dev ✨"
        )

        elapsed = (time.perf_counter() - start_time) * 1000  # ms
        response["elapsed_ms"] = f"{elapsed}"

        return JsonResponse(response, status=200)

    @staticmethod
    def _get_request_id(request):
        """Extract or generate a request ID."""
        return request.META.get("HTTP_X_REQUEST_ID") or str(uuid.uuid4())

    @staticmethod
    def _build_response(**kwargs):
        """Build the standardized JSON response."""
        return {
            "success": kwargs.get("success"),
            "status": kwargs.get("status"),
            "timestamp": kwargs.get("timestamp"),
            "timezone": kwargs.get("timezone"),
            "environment": kwargs.get("environment"),
            "elapsed_ms": kwargs.get("elapsed_ms"),
            "data": kwargs.get("data"),
            "meta": kwargs.get("meta"),
            "developer_note": kwargs.get("developer_note"),
        }
