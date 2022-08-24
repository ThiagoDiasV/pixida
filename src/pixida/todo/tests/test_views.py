from unittest.mock import patch

import pytest
from rest_framework.test import APIClient
from rest_framework.reverse import reverse

from pixida.todo.tests.factories import ToDoFactory
from pixida.todo.models import ToDo


class TestToDoViewSet:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()

    @pytest.mark.django_db
    def test_list_todos(self):
        todos_amount = 12
        ToDoFactory.create_batch(todos_amount)
        url = reverse("todo-list")
        response = self.client.get(url, format="json")
        assert response.status_code == 200
        assert len(response.json()) == todos_amount

    @pytest.mark.django_db
    @patch("pixida.todo.views.ToDoViewSet.list")
    def test_list_todos_exception(self, mock_list):
        mock_list.side_effect = Exception
        url = reverse("todo-list")
        with pytest.raises(Exception):
            response = self.client.get(url, format="json")
            assert response.json() == {
                "error": "There was an error loading the To-Do objects."
            }

    @pytest.mark.django_db
    def test_retrieve_todo(self):
        todos_amount = 12
        todos = ToDoFactory.create_batch(todos_amount)
        todo = todos.pop()
        todo_id = todo.id
        url = reverse("todo-detail", kwargs={"pk": todo_id})
        response = self.client.get(url, format="json")
        response_data = response.json()
        assert response.status_code == 200
        assert todo.id.__str__() == response_data["id"]
        assert todo.title == response_data["title"]
        assert todo.description == response_data["description"]

    @pytest.mark.django_db
    @patch("pixida.todo.views.ToDoViewSet.retrieve")
    def test_retrieve_todos_exception(self, mock_retrieve):
        mock_retrieve.side_effect = Exception
        todo = ToDoFactory()
        url = reverse("todo-detail", kwargs={"pk": todo.id})
        with pytest.raises(Exception):
            response = self.client.get(url, format="json")
            assert response.json() == {
                "error": "There was an error loading the To-Do object."
            }

    @pytest.mark.django_db
    def test_create_todo(self):
        data = {"title": "my awesome title", "description": "my awesome description"}
        url = reverse("todo-list")
        response = self.client.post(url, format="json", data=data)
        response_data = response.json()
        assert response.status_code == 201
        assert response_data["message"] == "To-Do object created successfully."
        assert response_data["todo"]["title"] == data["title"]
        assert response_data["todo"]["description"] == data["description"]

        todo = ToDo.objects.filter(
            title="my awesome title", description="my awesome description"
        )
        assert todo.count() == 1

    @pytest.mark.django_db
    @patch("pixida.todo.views.ToDoViewSet.create")
    def test_create_todos_exception(self, mock_create):
        mock_create.side_effect = Exception
        url = reverse("todo-list")
        with pytest.raises(Exception):
            response = self.client.post(url, format="json", data={})
            assert response.json() == {
                "error": "There was an error while creating a new To-Do object."
            }

    @pytest.mark.django_db
    def test_update_todo(self):
        todo = ToDoFactory()
        url = reverse("todo-detail", kwargs={"pk": todo.id})
        new_data = {"title": "my new title", "description": "my new description"}
        response = self.client.put(url, format="json", data=new_data)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["todo"]["title"] == new_data["title"]
        assert response_data["todo"]["description"] == new_data["description"]
        assert response_data["message"] == "To-Do object updated successfully."

    @pytest.mark.django_db
    @patch("pixida.todo.views.ToDoViewSet.update")
    def test_update_todos_exception(self, mock_update):
        mock_update.side_effect = Exception
        todo = ToDoFactory()
        url = reverse("todo-detail", kwargs={"pk": todo.id})
        with pytest.raises(Exception):
            response = self.client.put(url, format="json", data={})
            assert response.json() == {
                "error": "There was an error while updating the To-Do object."
            }

    @pytest.mark.django_db
    def test_destroy_todo(self):
        todo = ToDoFactory()
        todo_id = todo.id
        url = reverse("todo-detail", kwargs={"pk": todo_id})
        response = self.client.delete(url, format="json")
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["message"] == "To-Do object deleted successfully."

        with pytest.raises(ToDo.DoesNotExist):
            ToDo.objects.get(id=todo_id)

    @pytest.mark.django_db
    @patch("pixida.todo.views.ToDoViewSet.destroy")
    def test_destroy_todos_exception(self, mock_destroy):
        mock_destroy.side_effect = Exception
        todo = ToDoFactory()
        url = reverse("todo-detail", kwargs={"pk": todo.id})
        with pytest.raises(Exception):
            response = self.client.delete(url, format="json", data={})
            assert response.json() == {
                "error": "There has been an error while deleting the To-Do object."
            }
