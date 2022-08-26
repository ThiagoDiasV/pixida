from sqlite3 import IntegrityError
from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
import structlog

from pixida.todo.models import ToDo
from pixida.todo.serializers import ToDoSerializer
from pixida.todo import docs


logger = structlog.get_logger(__name__)


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    @swagger_auto_schema(**docs.list_schema)
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as exc:  # NOTE: That's not the ideal approach, catching a bare exception. Once we figure out possible exceptions we should catch specific exceptions
            logger.exception(exc)
            return Response(
                {"error": "There was an error loading the To-Do objects."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @swagger_auto_schema(**docs.create_schema)
    def create(self, request, *args, **kwargs):
        pass

    @swagger_auto_schema(**docs.retrieve_schema)
    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception as exc:  # NOTE: That's not the ideal approach, catching a bare exception. Once we figure out possible exceptions we should catch specific exceptions
            logger.exception(exc)
            return Response(
                {"error": "There was an error loading the To-Do object."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @swagger_auto_schema(**docs.update_schema)
    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response(
                {"message": "To-Do object updated successfully.", "todo": response.data}
            )
        except Exception as exc:  # NOTE: That's not the ideal approach, catching a bare exception. Once we figure out possible exceptions we should catch specific exceptions
            logger.exception(exc)
            return Response(
                {"error": "There was an error while updating the To-Do object."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk=None):
        """
        Used to create new todos
        """

        self.kwargs = request.data

        try:
            instance = self.get_object()
        except AssertionError:
            instance = None
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)

        if instance is None:  # Create workflow
            if "id" in self.kwargs:
                self.kwargs["pk"] = self.kwargs["id"]
                del self.kwargs["id"]
            lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
            lookup_value = self.kwargs[lookup_url_kwarg]
            extra_kwargs = {self.lookup_field: lookup_value}
            try:
                serializer.save(**extra_kwargs)
            except IntegrityError as exc:
                logger.exception(exc)
                return Response(
                    {"error": "There was an error while creating a new To-Do object."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                todo = serializer.data
                return Response(
                    {"message": "To-Do object created successfully.", "todo": todo},
                    status=status.HTTP_201_CREATED,
                )

    @swagger_auto_schema(**docs.destroy_schema)
    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)
            return Response(
                {"message": "To-Do object deleted successfully."},
                status=status.HTTP_200_OK,
            )
        except Exception as exc:  # NOTE: That's not the ideal approach, catching a bare exception. Once we figure out possible exceptions we should catch specific exceptions
            logger.exception(exc)
            return Response(
                {"error": "There has been an error while deleting the To-Do object."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        pass
