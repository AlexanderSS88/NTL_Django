from django_filters import rest_framework as filters, \
    DateFromToRangeFilter
from advertisements.models import Advertisement


class CharFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class FilterByNameAndDate(filters.FilterSet):
    created_at = DateFromToRangeFilter()
    status = CharFilter()
    id = CharFilter()
    creator = CharFilter(
        field_name='creator__username',
        lookup_expr='in')
    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at', 'status', 'id']
