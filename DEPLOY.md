1. Install `python3`, `pip`, `posgres`, `virtualenv`

  ```sh
  sudo apt-get install python3 python3-dev python-pip 
  sudo apt-get install libpq-dev libjpeg-dev build-essential python-dev # fix
  sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
  sudo apt-get install apache2 libapache2-mod-wsgi-py3
  sudo apt-get install postgresql postgresql-contrib
  sudo pip install virtualenv
  ```

2. Start pg

  ```sh
  sudo pg_createcluster 9.3 clinic --start 
  ```
  
3. create a New Role

  ```sh
  sudo -i -u postgres
  createuser --interactive
  ```
  ps: This basically is an interactive shell script that calls the correct Postgres commands to create a user to your specifications. It will only ask you two questions: the name of the role and whether it should be a superuser. You can get more control by passing some additional flags. Check out the options by looking at the man page:
  ```sh
  man createuser
  ```

4. create a new database
 
  You can create the appropriate database by simply calling this command as the postgres user:
  ```sh
  createdb duyetdev
  ```
  
  The way that Postgres is set up by default (authenticating roles that are requested by matching system accounts) also comes with the assumption that a matching database will exist for the role to connect to.
  So if I have a user called `duyetdev`, that role will attempt to connect to a database called `duyetdev` by default.
 
 You can change to the Linux system account by typing:
 
 ```sh
 sudo -i -u duyetdev
 ```

  You can then connect to the test1 database as the test1 Postgres role by typing:
  ```sh
  psql
  ```
  
  If you want your user to connect to a different database, you can do so by specifying the database like this:
  ```sh
  psql -d postgres
  ```

5. Start virtualenv, install package requirement
  Go to project folder. Run:
  
  ```sh
  virtualenv --python=python3.4 venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
  
6. Adjust the Project Settings

  We should do with our newly created project files is adjust the settings. Open the settings file with your text editor:
  
  ```sh
  nano clinic/settings.py
  ```

  ```python
  DEBUG = False # Place to False
  ALLOWED_HOSTS = ['localhost', ] # your host name, domain name here

  # Database
  # https://docs.djangoproject.com/en/1.8/ref/settings/#databases
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'clinic_dev', # Database name
        'USER': 'duyetdev',   # Database user
        'PASSWORD': '123456', # Database password
        'HOST': 'localhost',  # Database hostname
        'PORT': '5432',       # Database port
    }
  }
  ```

7. Sync database (will ask to create default admin account)
  ```sh
  python manage.py syncdb
  python manage.py migrate
  ```

8. Create Another Admin user 

  ```sh
  python manage.py createsuperuser
  ```

9. Import initial data
  
  ```sh
  python manage.py loaddata initial_data.yaml
  ```
10. Test running 

  test your project by starting up the Django development server with:

  ```sh
  python manage.py runserver 0.0.0.0:8000
  ```

  In your web browser, visit your server's domain name or IP address followed by `:8000`

  ```
  http://server_domain_or_IP:8000
  ```

11. We can collect all of the static content into the directory location we configured by typing:

  ```sh
  python manage.py collectstatic
  ```

10. Configure Apache

  Edit the default virtual host file:

  ```sh
  sudo nano /etc/apache2/sites-available/000-default.conf
  ```

  To start, let's configure the project. We will use an alias to tell Apache to map any requests starting with `/static` to the **"static"** directory within our project folder. We collected the static assets there earlier, config path WSGI. We will set up the alias and then grant access to the directory in question with a directory block:

  ```
  <VirtualHost *:80>
      . . .

      Alias /static /home/user/clinic/static
      <Directory /home/user/clinic/static>
          Require all granted
      </Directory>

      <Directory /home/user/clinic/clinicproject>
          <Files wsgi.py>
              Require all granted
          </Files>
      </Directory>

      WSGIDaemonProcess clinicproject python-path=/home/user/clinic:/home/user/clinic/clinicprojectenv/lib/python3.4/site-packages
      WSGIProcessGroup clinicproject
      WSGIScriptAlias / /home/user/clinic/clinicproject/clinic/wsgi.py

  </VirtualHost>
  ```

  Restart Apache by typing:

  ```sh
  sudo service apache2 restart
  ```
  You should now be able to access your Django site by going to your server's domain name or IP address without specifying a port. The regular site and the admin interface should function as expected.
