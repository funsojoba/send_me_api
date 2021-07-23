# send_me_api

API Service backing client interfaces

## Technologies

* [Python 3.9](https://python.org) : Base programming language for development
* [Django Framework](https://www.djangoproject.com/) : Development framework used for the application
* [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development

## Description
There are four main endpoints for this api,
- The first endpoint `http://127.0.0.1:8000/api/auth/register/`, this endpoint takes a POST request for user registration with the following expected values
```
{
  "first_name":”John”,
  "last_name":"Doe",
  "email":"johndoe@email.com",
  “password”:"johney123456$$##"
}
```
the endpoint takes user data and stores it in the database
Expected response
```
{
    "data": {
        "first_name": "john",
        "last_name": "doe",
        "email": "johndoe@email.com"
    },
    "message": "success"
}
```

- The second endpoint `http://127.0.0.1:8000/api/auth/login/`, this endpoint handles user login. A post request with the following data is expected

```
{
    "email":"johndoe@email.com",
    "password":"johney123456$$##"
}
```

If the provided information are correct, a user token is generated for user to be passed in the request header for subsequent requests.
```
{
    "token": "29d7682bdf3f2226ec8db00213bf94c525c04d04"
}
```

- The third endpoint `http://127.0.0.1:8000/api/transact/receive/`. This endpoint allows user update their account with incoming amount. It takes a post request and returns the total amount after adding the initial to what was in the database

- The fourth endpoint `http://127.0.0.1:8000/api/transact/send/`. This endpoint checks if there is enough money in the user's database before carrying out any deduction from the database. If there is not enough, an error message is returned, else, the tansaction is performed.
## Getting Started

Getting started with this project is very simple, all you need is to have Git installed on your machine. Then open up your terminal and run this command `git clone https://github.com/funsojoba/send_me_api.git` to clone the project repository.

Change directory into the project folder `cd send-me-api`.

Enable your virtual environment and activate your virtual environment. For Mac OS, run `python3 -m venv venv` and then run `source venv/bin/activate`

Run `pip install -r requirements.txt` to install all the necessary dependencies

Run this command `python manage.py makemigrations` for creating new migrations based on the models defined and also run `python manage.py migrate` to apply migrations.

And finally, run `python manage.py runserver` to spin up the server, after which the app should be running on `http://127.0.0.1:8000`, defualt port is `8000`, if your port is busy at the time you can change it by running `python manage.py runserver <any other port number you like>`

In summary, these are the lists of commands to run in listed order, to start up the project.

```docker
1. git clone https://github.com/funsojoba/send_me_api.git
2. cd send-me-api
3. python3 -m venv venv
4. source venv/bin/activate  (for MacOS)
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py runserver
8. use ctrl+c to quit server
```

## Running Tests

Currently, truthy tests has been provided in each of the application defined in the project, before running the tests with the following command make sure that your api service is up and running.

Run 
```
python manage.py test
```

## License

The MIT License 
