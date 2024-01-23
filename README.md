# Django Custom Authentication Backend With Docker and Jenkins cicd in AWS
The application is Developed by following Features:

### Features
## 1. Create a New django restframework authentication project
   * this project is deploy in AWS ec2 instance
   * In Django project, create a custom backend file where Override the `authenticate` method to add logic for email/password 
  * create django project which contain login registration system
  * registration sysytem has proper validation
  * login sysytem authentication user with `django.contrib.auth.backends.ModelBackend`.
  * Used Tocken based Authentication with JWT tocken
  * use Docker and Docker compose for application containerization
  * use CI with jenkins  github integration
  * github webhook used for continuous delivery
  * github ssh key used for jenkins connection
  * finally docker compose used for container build and run
 

## Getting Started in jenkins

```bash
docker-compose up
```


# Getting Started with django App
* create virtual environment
  ### `virtualenv env`
* install all requirement
  ### `python -m pip install -r requirements.txt`
* statrt Project: In the project directory, you can run:
### `python3 manage.py runserver`

**Progress:**
Version 1 completed and hosted

## SCREENSHOTS:**
<h2>Home Page</h2>
<img src="https://github.com/nusratdevo/arena_book_store/blob/main/screen/screen01.png" height="400">
---
 
