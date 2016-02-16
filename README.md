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
* Initialize the local database
	
	```sh
	python manage.py syncdb
	```
* Start the development server.
	
	```sh
	python manage.py runserver
	```

