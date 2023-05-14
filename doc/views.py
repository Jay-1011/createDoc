from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied

from .models import Document
from .serializers import MyModelSerializer
from rest_framework import generics
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

class MyModelListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Document.objects.all()
    serializer_class = MyModelSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            raise PermissionDenied(detail='User authentication failed')


class MyModelRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MyModelSerializer
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        print(self.request.user)
        return Document.objects.filter(user=self.request.user)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.kwargs.get(self.lookup_url_kwarg))
        self.check_object_permissions(self.request, obj)
        return obj

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Object deleted successfully'})

    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class MyModelListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MyModelSerializer

    def get_queryset(self):
        return Document.objects.filter(user=self.request.user)