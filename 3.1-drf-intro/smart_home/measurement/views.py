from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer,\
    MeasurementAllSerializer


class SensorView(ListCreateAPIView):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all().order_by('id')


class SensorUnitView(RetrieveUpdateAPIView):
    serializer_class = SensorDetailSerializer
    queryset = Sensor.objects.all()


class MeasurementView(ListCreateAPIView):
    serializer_class = MeasurementAllSerializer
    queryset = Measurement.objects.all()




