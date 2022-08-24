from django.contrib import admin

from pixida.todo.models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    pass


admin.site.register(ToDo, ToDoAdmin)
