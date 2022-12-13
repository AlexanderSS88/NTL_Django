from django.contrib.auth.models import User
from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from advertisements.filters import FilterByNameAndDate
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrRead, AnyExceptTheOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FilterByNameAndDate

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__)
        if self.request.user.is_superuser:
            queryset = self.queryset.order_by('id')
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.request.user.is_authenticated:
            queryset = self.queryset.filter(
                creator=self.request.user).order_by('id')
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        else:
            queryset = self.queryset.filter(status='OPEN').order_by('id')
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save()

    @action(
        detail=True, methods=['POST'],
        permission_classes=[AnyExceptTheOwner])
    def add_to_favorites(self, request, pk=None):
        adv_to_favor = Advertisement.objects.get(id=pk)
        adv_to_favor.favor_users.add(request.user)
        user_id = request.user.id
        return Response(f'User {request.user} save adv № {pk}')

    @action(
        detail=False, methods=['GET'],
        permission_classes=[AnyExceptTheOwner])
    def get_favorites(self, request):
        favor_data = User.objects.all().get(
            id=request.user.id
            ).favorite_advs.all()
        page = self.paginate_queryset(favor_data)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(favor_data, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ["create"]:
            self.permission_classes = [IsAuthenticated()]
            return [IsAuthenticated()]
        elif self.action in [
            "update",
            "list",
            "retrieve",
            "partial_update",
            "destroy"
            ]:
            self.permission_classes = [IsOwnerOrRead()]
            return [IsOwnerOrRead()]
        return []
