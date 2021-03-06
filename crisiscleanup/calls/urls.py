from rest_framework import routers
from django.conf.urls import url
from . import views

from crisiscleanup.calls.api.call import CallViewSet
from crisiscleanup.calls.api.user import UserViewSet
from crisiscleanup.calls.api.caller import CallerViewSet
from crisiscleanup.calls.api.gateway import GatewayViewSet
from crisiscleanup.calls.api.article import ArticleViewSet
from crisiscleanup.calls.api.trainingModule import TrainingModuleViewSet
from crisiscleanup.calls.api.trainingQuestion import TrainingQuestionViewSet
from crisiscleanup.calls.api.language import LanguageViewSet

router = routers.SimpleRouter()
router.register(r'calls', CallViewSet)
router.register(r'call-users', UserViewSet)
router.register(r'callers', CallerViewSet)
router.register(r'gateways', GatewayViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'trainingModules', TrainingModuleViewSet)
router.register(r'trainingQuestions', TrainingQuestionViewSet)
router.register(r'languages', LanguageViewSet)

urlpatterns = [
    url(r'^connect-first/inbound$', views.connect_first_inbound, name="connect-first-inbound"), 
]
