from drf_yasg import openapi


list_schema = dict(
    operation_description="To-Do-API-Handler (Get all To-Do objects)",
    responses={
        200: openapi.Response(
            "Successful operation",
            examples={
                "application/json": [
                    {
                        "id": "bb73670b-d5e6-42af-9e5a-ce4797841d3d",
                        "title": "API",
                        "description": "Create an API that meets the requirements",
                    }
                ]
            },
        ),
        400: openapi.Response(
            "Operation not successful",
            examples={
                "application/json": {
                    "error": "There was an error loading the To-Do objects."
                }
            },
        ),
    },
)

create_schema = dict(
    operation_description="To-Do-API-Handler (Create a new To-Do object)",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_STRING, description="id", format="uuid"
            ),
            "title": openapi.Schema(type=openapi.TYPE_STRING, description="The title"),
            "description": openapi.Schema(
                type=openapi.TYPE_STRING, description="The description"
            ),
        },
    ),
    responses={
        200: openapi.Response(
            "Successful operation",
            examples={
                "application/json": {
                    "message": "To-Do object created successfully.",
                    "todo": {
                        "id": "bb73670b-d5e6-42af-9e5a-ce4797841d3d",
                        "title": "API",
                        "description": "Create an API that meets the requirements",
                    },
                }
            },
        ),
        400: openapi.Response(
            "Operation not successful",
            examples={
                "application/json": {
                    "error": "There was an error while creating a new To-Do object."
                }
            },
        ),
    },
)

retrieve_schema = dict(
    operation_description="To-Do-API-Handler (Get a single To-Do object)",
    responses={
        200: openapi.Response(
            "Successful operation",
            examples={
                "application/json": {
                    "id": "bb73670b-d5e6-42af-9e5a-ce4797841d3d",
                    "title": "API",
                    "description": "Create an API that meets the requirements",
                }
            },
        ),
        400: openapi.Response(
            "Operation not successful",
            examples={
                "application/json": {
                    "error": "There was an error loading the To-Do object."
                }
            },
        ),
    },
)

update_schema = dict(
    operation_description="To-Do-API-Handler (Update an existing To-Do object)",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_STRING, description="id", format="uuid"
            ),
            "title": openapi.Schema(type=openapi.TYPE_STRING, description="The title"),
            "description": openapi.Schema(
                type=openapi.TYPE_STRING, description="The description"
            ),
        },
    ),
    responses={
        204: openapi.Response(
            "Successful operation",
            examples={
                "application/json": {"message": "To-Do object updated successfully."}
            },
        ),
        400: openapi.Response(
            "Operation not successful",
            examples={
                "application/json": {
                    "error": "There was an error while updating an existing To-Do object."
                }
            },
        ),
    },
)

destroy_schema = dict(
    operation_description="To-Do-API-Handler (Delete an existing To-Do object)",
    responses={
        204: openapi.Response(
            "Successful operation",
            examples={
                "application/json": {"message": "To-Do object deleted successfully."}
            },
        ),
        400: openapi.Response(
            "Operation not successful",
            examples={
                "application/json": {
                    "error": "There has been an error while deleting the To-Do object."
                }
            },
        ),
    },
)
