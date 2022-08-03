from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    with open(settings.BUS_STATION_CSV, newline='',
        encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        all_station_list = []
        [all_station_list.append(
            {
            "Name": row['Name'],
            "Street": row['Street'],
            "District": row['District']
            }
            )
            for row in reader]
    paginator = Paginator(all_station_list, 10)
    page = paginator.get_page(page_number)
    stations_for_list = []
    [stations_for_list.append(position) for position in page]
    context = {'bus_stations': stations_for_list, 'page': page}
    return render(request, 'stations/index.html', context)

