# Gro - drf


#### DEPLOYED BACKEND API [LINK]()
#### DEPLOYED FRONTEND [LINK - LIVE SITE]()
#### DEPLOYED FRONTEND [REPOSITORY]()

## CONTENTS

* [Project Structure](#project-structure)
  * [Agile workflow](#agile-workflow)
  * [User Stories](#user-stories)
* [Database Design](#databasedesign)
  * [Models](#models)
  * [ERD](#erd)
* [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Frameworks and software](#frameworks-and-software)
  * [Libraries](#libraries)
* [Testing](#testing)
* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)
* [Testing](#testing)
* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)


# **Project Structure**
The overall structure of the project was modelled on the [drf-api](https://github.com/Code-Institute-Solutions/drf-api) walkthrough due to time constraints. The walkthrough project includes most of the assetments requirements for project 5.

I've tried to customize the walkthrough where possible to fit the scope for my own project. I also added a custom contact model.

## Agile Workflow
I built this API using Agile principles right from the start by creating user stories for the developer/superuser to follow.

## User Stories
I have included links to the [GitHub Issues](https://github.com/malinpalo/gro/issues) for this project, as well as the [KANBAN board](https://github.com/malinpalo/gro/milestones).

# **Database Design**

## Models
The following models was created by me for the Gro drf:
 * User 
 * Profile (automatically created when a user Is created)
 * Posts (A post by a user with gardening ideas)
 * Comment (To make a comment on a post)
 * Likes (To indicate if a user likes an post)
 * Follow (For users to follow other users of the site)
 * Contact (To send an message to the admin of the site)


## Entity relationship diagram
The relationship between all of the above models is summarized in the following diagram
[ERD](https://res.cloudinary.com/dz0w8vqzx/image/upload/v1686515958/ERD_qrhzwo.png).

# **Technologies Used**

## Languages
 * [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality for the DRF backend framework.

## Frameworks and Software

* [Django Rest Framework](https://www.django-rest-framework.org/) - A framework for building web API's
* [PEP8 Validation](https://pypi.org/project/pep8/) - pep8 is a tool to check your Python code against some of the style conventions in PEP 8.
* [Github](https://github.com/) - Used to host the repository, store the commit history and manage the project board containing user stories and bug reports.
* [Heroku](https://en.wikipedia.org/wiki/Heroku) - A cloud platform that the application is deployed to.
* [Cloudinary](https://cloudinary.com/) - A service that hosts image files in the project.

## Libraries
* [asgiref](https://pypi.org/project/asgiref/)
* [cloudinary](https://pypi.org/project/cloudinary/) 
* [dj-database-url](https://pypi.org/project/dj-database-url/0.5.0/) 
* [dj-rest-auth](https://pypi.org/project/dj-rest-auth/) 
* [Django](https://pypi.org/project/Django/) 
* [django-allauth](https://pypi.org/project/django-allauth/)
* [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) 
* [django-cors-headers](https://pypi.org/project/django-cors-headers/)
* [django-filter](https://pypi.org/project/django-filter/)
* [django-rest-framework](https://pypi.org/project/djangorestframework/)
* [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/)
* [gunicorn](https://pypi.org/project/gunicorn/)
* [oauthlib](https://pypi.org/project/oauthlib/) 
* [pillow](https://pypi.org/project/Pillow/8.2.0/) 
* [psycopg2](https://pypi.org/project/psycopg2/)
* [PyJWT](https://pypi.org/project/PyJWT/) 
* [python3-openid](https://pypi.org/project/python3-openid/) 
* [pytz](https://pypi.org/project/pytz/) 
* [requests-oauhlib](https://pypi.org/project/requests-oauthlib/) 
* [sqlparse](https://pypi.org/project/sqlparse/)

# **Testing**
Please click [**_here_**](TESTING.md) to read more information about testing Gro-drf.