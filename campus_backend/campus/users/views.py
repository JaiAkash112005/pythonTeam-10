from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Register user
@csrf_exempt
def register_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        return JsonResponse({
            "message": "User registered successfully",
            "data": data
        })
    
    return JsonResponse({"error": "POST request required"}, status=400)


# Login user
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        return JsonResponse({
            "message": "Login successful",
            "data": data
        })

    return JsonResponse({"error": "POST request required"}, status=400)
