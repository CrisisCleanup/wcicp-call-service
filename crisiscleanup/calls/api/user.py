from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.decorators import list_route
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from crisiscleanup.calls.api.serializers.user import UserSerializer
from crisiscleanup.calls.models import User
from crisiscleanup.taskapp.celery import debug_task


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ()
    filter_fields = ()

    @list_route()
    def test_celery(self, request):
        resp = {
            'task_id': debug_task.delay().id
        }
        return Response(resp, status=status.HTTP_200_OK)

    @detail_route(methods=['post'])
    def set_read_articles(self, request, pk=None):
        user = self.get_object()
        #Expects a list of guids ["article1.Id","article2.Id"]
        user.read_articles = request.data;
        user.save()
        return Response({'status': 'read_articles set'})
