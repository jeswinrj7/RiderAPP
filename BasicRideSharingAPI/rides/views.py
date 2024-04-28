from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Ride
from .serializers import RideSerializer,RideIdSerializer, RideStatusUpdateSerializer
from rest_framework.generics import ListCreateAPIView, get_object_or_404
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class RideCreateAPIView(ListCreateAPIView):
    queryset =[]
    serializer_class = RideSerializer

    def post(self, request, *args, **kwargs):
        rider_id = request.data.get('rider')
        rider = get_object_or_404(CustomUser, id=rider_id)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Ride created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RideDetailsByIdListView(ListCreateAPIView):
    queryset = []
    serializer_class = RideIdSerializer

    def post(self, request):
        ride_id = request.data.get('id')
        try:
            ride = Ride.objects.get(id=ride_id)
            ride_data = {
                'id': ride.id,
                'rider': ride.rider_id,
                'driver': ride.driver_id,
                'pickup_location': ride.pickup_location,
                'dropoff_location': ride.dropoff_location,
                'status': ride.status,
                'created_at': ride.created_at,
                'updated_at': ride.updated_at
            }
            return Response(ride_data)
        except Ride.DoesNotExist:
            return Response({'error': 'Ride not found'}, status=status.HTTP_404_NOT_FOUND)

class RidesFullDetailsView(APIView):
    def get(self, request):
        rides = Ride.objects.all()
        serializer = RideSerializer(rides, many=True)
        return Response(serializer.data)

    def post(self, request):
        return self.get(request)

class UpdateRideStatusAPIView(ListCreateAPIView):
    queryset = []
    serializer_class = RideStatusUpdateSerializer

    def post(self, request, *args, **kwargs):
        ride_id = request.data.get('ride_id')
        new_status = request.data.get('new_status')
        try:
            ride = Ride.objects.get(id=ride_id)
            ride.status = new_status
            ride.save()
            return Response({'message': 'Updated successfully'}, status=status.HTTP_200_OK)
        except Ride.DoesNotExist:
            return Response({'error': 'Ride not found'}, status=status.HTTP_404_NOT_FOUND)