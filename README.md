# ToDo API

## Requirements
- Python 3.9
- Django 4.1
- PostgreSQL 14

## Docker requirements
- Docker 20.10.17
- docker-compose 2.7.0

## Other dependencies
This project is using Terraform (v1.2.7) to build the needed infrastructure in AWS.

## Running the project locally
You can run the project locally with docker and docker-compose with the command
    
    docker-compose up --build

Or having Python 3.9, run (into a virtual environment)

    pip install -r requirements-dev.txt

Without Docker you will need to have PostgreSQL v14 running and set the database variables on the local environment.

## API link

ToDo API is running on AWS lambda with API Gateway and can be accessed with the link below

[API link](https://llq5oyhty7.execute-api.us-east-1.amazonaws.com/production/v1/todo/)

The API has the following endpoints

    [GET]    /todo/ -> list all ToDos
    [GET]    /todo/{todo_id} -> get one specific ToDo
    [PUT]    /todo/ -> create a new ToDo
    [PUT]    /todo/{todo_id} -> update one ToDo
    [DELETE] /todo/{todo_id} -> delete one ToDo


## API docs

[API docs](https://llq5oyhty7.execute-api.us-east-1.amazonaws.com/production/docs/)

  * Note about the docs: On the swagger documentation we have a POST method but the new ToDos creations are happening through a PUT request, as the task challenge docs asked to do. On the docs it's like a POST because I wasn't able to override the drf-yasg dependency correctly to have the PUT documentation to create new ToDos.