from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from DB.models import Scooter, Polygon, Mission
from .serializers import MissionSerializer

class MissionViewSet(viewsets.ViewSet):
  def create(self, request):
    scooter_id = request.data.get('scooter_id')
    user_id = request.data.get('user_name')
    
    try:
      scooter = Scooter.objects.get(identifier=scooter_id)
      polygons = Polygon.objects.all()
      
      for polygon in polygons:
        if polygon.area.contains(scooter.location):
          mission = Mission(user_id=user_id, scooter=scooter)
          mission.save()
          return Response({'message': 'Mission assigned successfully!', 'prioriti': mission.prioriti}, status=status.HTTP_200_OK)
      return Response({'message': 'Scooter is not in any polygon area.'}, status=status.HTTP_400_BAD_REQUEST)
    
    except Scooter.DoesNotExist:
      return Response({'message': 'Scooter not found.'}, status=status.HTTP_404_NOT_FOUND)
          
  def list(self, request):
    missions = Mission.objects.all()
    serializer = MissionSerializer(missions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
