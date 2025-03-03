import json
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

class ValidateRequest(MiddlewareMixin):
    def process_request(self, request):
        if request.method in ["POST", "PUT", "DELETE"]:
            if request.content_type != "application/json":
                return JsonResponse({"error": "Invalid Content-Type, must be application/json"}, status=400)
            
            try:
                json.loads(request.body)
            except:
                return JsonResponse({"error": "Error while parsing json body."}, status=400)
            
    # def process_response(self, request, response):
    #     ...
