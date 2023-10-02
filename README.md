# Online-learning platform

## Description
The trend towards online learning is developing around the world. Therefore, anyone can post their useful materials or courses on our platform.


## Set Up your personal settings
Create a `.env` configuration file with your personal settings in the root of the project, according to the sample, specified in `.env.sample`. Fill out the file according to your personal data. 

Create a database in postgresql. The name of the database must match the name specified in the file.

## Fill DB
Run migrations using the command `python manage.py migrate`. 
Now you can fill the database with initial data using the commands:
- `python manage.py fill_courses`
- `python manage.py fill_lessons`
- `python manage.py fill_payments`

Or you can create it by yourself!

## Create users
To create users use the following commands:
- `python manage.py create_user`
- `python manage.py create_moderator`

User can create, edit, delete and view only his own lessons and courses. The moderator has the rights to view and edit any courses, but cannot delete or create them.

## Running
To run the project, enter the `python manage.py runserver` command in the terminal.