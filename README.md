# UserApp - A simple user data application to do CRUD operations with DJango Rest Framework

## Requirements
- Python 3.10.4
- Django 4.0.6
- Django Rest Framework

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation. You can do this by running the command
```
python3 -m venv venv

```
After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt

```
## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our 
application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized 
around collections and elements, both of which are resources.

All the endpoints start with `http://127.0.0.1:8000/`. The endpoints are given below-

| EndPoint  | HTTP Method | CRUD Method  | Result |
| ------------- | ------------- | ------------- | ------------- |
| api/v1/parent/  | GET  | READ  | Get list of parents  |
| api/v1/parent/  | POST  | CREATE  | Create a new parent  |
| api/v1/children/  | GET  | READ  | Get list of children  |
| api/v1/children/  | POST  | CREATE  | Create new children  |
| api/v1/parent/<int:id>  | GET  | READ  | Get a parent  |
| api/v1/parent/<int:id>  | PUT  | UPDATE  | Update a parent  |
| api/v1/parent/<int:id>  | DELETE  | DELETE  | Delete a parent  |
| api/v1/child/<int:id>  | GET  | READ  | Get a child  |
| api/v1/child/<int:id>  | PUT  | UPDATE  | Update a child  |
| api/v1/child/<int:id>  | DELETE  | DELETE  | Delete a child  |

## Running the server
To run the server user the commands below -
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Testing
To test the endponts we can run the custom test cases by running the command below -
```
python manage.py test
```

