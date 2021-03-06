from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.decorators import list_route
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from crisiscleanup.calls.api.serializers.user import UserSerializer
from crisiscleanup.calls.models import User
from crisiscleanup.calls.models import Article
from crisiscleanup.calls.models import TrainingModule
from crisiscleanup.taskapp.celery import debug_task

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ()
    filter_fields = ("willing_to_be_call_center_support",)
    lookup_field = 'cc_id'

    @list_route()
    def test_celery(self, request):
        resp = {
            'task_id': debug_task.delay().id
        }
        return Response(resp, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        #Allow partial updates
        kwargs['partial'] = True
        return super(UserViewSet, self).update(request, *args, **kwargs)

    @detail_route(methods=['post'])
    def set_read_articles(self, request, cc_id=None):
        user = self.get_object()
        #Expects a list of guids ["article1.Id","article2.Id"]
        user.read_articles = request.data
        user.save()
        return Response({'status': 'read_articles set'})

    @detail_route(methods=['post'])
    def set_completed_training(self, request, cc_id=None):
        user = self.get_object()
        if(isinstance(request.data, list)):
            #Expects a list of guids ["trainingModule1.Id","trainingModule2.Id"]
            user.training_completed = request.data
        elif(not user.training_completed.filter(pk=request.data).exists()):
            #Add the training if they haven't already completed it
            user.training_completed.add(request.data)
        user.save()
        return Response({'status': 'training_completed set'})

    @detail_route(methods=['get'])
    def get_detail(self, request, cc_id=None):
        user = self.get_object()
        serializedData = self.get_serializer(user).data;
        #Calculate whether or not the user's training and read articles are up-to-date
        isUpToDate = Article.objects.count() == user.read_articles.count();
        trainingCompleted = TrainingModule.objects.count() == user.training_completed.count();
        serializedData["is_up_to_date"] = isUpToDate;
        serializedData["is_training_completed"] = trainingCompleted;
        return Response(serializedData)
