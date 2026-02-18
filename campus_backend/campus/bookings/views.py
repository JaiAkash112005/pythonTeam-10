from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Booking
import json


@csrf_exempt
def booking_api(request, booking_id=None):

    # 👉 GET all bookings
    if request.method == "GET":

        if booking_id:
            try:
                booking = Booking.objects.get(id=booking_id)

                data = {
                    "id": booking.id,
                    "user_name": booking.user_name,
                    "room": booking.room,
                    "date": str(booking.date),
                }

                return JsonResponse(data)

            except Booking.DoesNotExist:
                return JsonResponse({"error": "Booking not found"}, status=404)

        bookings = Booking.objects.all()

        data = list(bookings.values())

        return JsonResponse(data, safe=False)

    # 👉 CREATE booking
    if request.method == "POST":
        data = json.loads(request.body)

        booking = Booking.objects.create(
            user_name=data["user_name"],
            room=data["room"],
            date=data["date"],
        )

        return JsonResponse({
            "message": "Booking created",
            "id": booking.id
        })

    # 👉 UPDATE booking
    if request.method == "PUT":
        if not booking_id:
            return JsonResponse({"error": "Booking ID required"}, status=400)

        try:
            booking = Booking.objects.get(id=booking_id)
            data = json.loads(request.body)

            booking.user_name = data.get("user_name", booking.user_name)
            booking.room = data.get("room", booking.room)
            booking.date = data.get("date", booking.date)

            booking.save()

            return JsonResponse({"message": "Booking updated"})

        except Booking.DoesNotExist:
            return JsonResponse({"error": "Booking not found"}, status=404)

    # 👉 DELETE booking
    if request.method == "DELETE":
        if not booking_id:
            return JsonResponse({"error": "Booking ID required"}, status=400)

        try:
            booking = Booking.objects.get(id=booking_id)
            booking.delete()

            return JsonResponse({"message": "Booking deleted"})

        except Booking.DoesNotExist:
            return JsonResponse({"error": "Booking not found"}, status=404)

    return JsonResponse({"error": "Invalid request"}, status=400)
