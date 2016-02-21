1. Install `python3`, `pip`, `posgres`, `virtualenv`

  ```sh
  sudo apt-get install python3 python3-dev python-pip 
  sudo apt-get install libpq-dev libjpeg-dev # fix
  sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
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
  
6. Sync database
  ```sh
  python manage.py syncdb
  ```
