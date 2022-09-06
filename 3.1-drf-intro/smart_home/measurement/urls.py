from django.urls import path

from measurement.views import SensorView, SensorUnitView, MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view(), name='sens'),
    path('sensors/<pk>/', SensorUnitView.as_view(), name='sens_unit'),
    path('measurements/', MeasurementView.as_view(), name='add_meas'),
    ]
