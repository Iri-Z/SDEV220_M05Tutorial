Domains:

-You can manage DNS records and provide the hostname, type (cname), 
value pointing towards PythonANywhere domain, and ttl 

-Would need to upgrade PythonANywhere account 

-Copy path to virtual environment and wsgi config file

-Delete old web app and create a new one with the new domain name 
and manually configure for your Python version

-Update the virtual environment path and wsgi config with what was saved earlier

Deploy on Heroku

-Install necessary packages to virtual environment (dj-database-url gunicorn whitenoise)

-Update the requirements file with these packages and add the line :
psycopg2==2.9.3

-Create a file Procfile in base dir and write in the line:
web: gunicorn mysite.wsgi --log-file -

-Create a file runtime.txt and write in version of python like:
python-3.6.4

-Create a local_settings.py file for sqlite3 information

-Edit setting.py file to add information for postgresql and middleware 

-Install Heroku toolbelt and login

-Add local_settings.py to .gitignore file

-Add and commit changes

-Create a heroku name

-Push to heroku

-Test 
    -Run migrate and createsuperuser
        -heroku run python manage.py migrate
        -heroku run python manage.py createsuperuser
    -start:  heroku ps:scale web=1
    -visit: heroku open
