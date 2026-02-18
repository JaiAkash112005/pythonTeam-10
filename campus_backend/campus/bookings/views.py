from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# temporary in-memory storage
bookings_data = []

@csrf_exempt
def create_booking(request):
    if request.method == "POST":
        data = json.loads(request.body)
        bookings_data.append(data)

        return JsonResponse({
            "message": "Booking created",
            "data": data
        })

    return JsonResponse({"error": "POST required"}, status=400)


def list_bookings(request):
    return JsonResponse(bookings_data, safe=False)
