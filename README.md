# Personal-web

This is a personal-blog-themed website designed for training purposes, and my former personal site.

## Demo

<img src="https://github.com/marcelovicentegc/Personal-web/blob/master/Personal-web.gif" width="640" height="360" />

## Directions

1. Clone this repo: `git clone https://github.com/marcelovicentegc/Personal-web.git`
2. Create virtual environment: `virtualenv venv_personalweb`
3. Change directories and activate the virtual environment: `cd venv_personalweb/Scripts; .\activate`
4. Change directories and install requirements: `cd ../../Personal-web/mysite; pip install -r base.txt`
5. Change directories and make migrations: `cd ../../; python manage.py makemigrations`
6. Migrate: `python manage.py migrate`
7. Create a super user: `python manage.py createsuperuser`
8. Run the application and play with it: `python manage.py runserver`

