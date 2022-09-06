# ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import CreateAPIView, ListCreateAPIView,\
    RetrieveUpdateAPIView
from rest_framework.response import Response
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, \
    MeasurementAllSerializer

class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request, *args, **kwargs):
        Sensor.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description')
            )
        return Response({'status': 'Ok'})

class SensorUnitView(RetrieveUpdateAPIView):
    serializer_class = SensorDetailSerializer
    queryset = Sensor.objects.all()

class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementAllSerializer
    def post(self, request, *args, **kwargs):
        Measurement.objects.create(
            id=request.POST.get('id'),
            temperature=request.POST.get('temperature'),
            image=request.POST.get('image')
            )









