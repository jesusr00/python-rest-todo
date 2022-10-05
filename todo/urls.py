from rest_framework import routers
from .viewsets import TodoViewSets

router = routers.DefaultRouter()

router.register('todo', TodoViewSets, 'todo')

urlpatterns = router.urls
