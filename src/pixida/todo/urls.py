from rest_framework import routers

from pixida.todo.views import ToDoViewSet


router = routers.DefaultRouter()
router.register('todo', ToDoViewSet, basename='todo')

urlpatterns = router.urls
