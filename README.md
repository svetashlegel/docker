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

## Running
To run the project, enter the `python manage.py runserver` command in the terminal.