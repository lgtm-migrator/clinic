# ambulatory care clinic

# Requirements

- **Pip** - a python package manager
- **virtualenv** - python virtual environments

# Setup 

* Clone project 
	
	```sh
	git clone https://github.com/duyetdev/clinic
	```

* Active virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/
* Install dependencies.

	```sh
	pip install -r requirements.txt
	```

* Initialize the local database
	
	```sh
	python manage.py migrate
	```
* Create admin user
	
	```sh
	python manage.py createsuperuser
	```

* Start the development server.
	
	```sh
	python manage.py runserver
	```

-------------------------------

* Import data 

	```sh
	python manage.py loaddata initial-data.yaml
	```