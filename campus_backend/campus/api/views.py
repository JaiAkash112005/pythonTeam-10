from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def resource_api(request):

    if request.method == "GET":
        return JsonResponse({
            "resources": "Resources API working"
        })

    if request.method == "POST":
        try:
            data = json.loads(request.body)

            return JsonResponse({
                "message": "Resource created",
                "data": data
            })

        except:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)
