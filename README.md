# ambulatory care clinic

# Requirements

- **Pip** - a python package manager
- **virtualenv** - python virtual environments
- http://tutorial.djangogirls.org/en/django_installation/index.html

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

* Gettext (i18n) from template 
	
	```sh
	python manage.py makemessages -l jp
	```

(If get an ugly error that says that we don’t have the [GNU gettext](https://www.gnu.org/software/gettext/) installed)	

Now go to the `home/locale` folder. There is a folder named `jp` with a folder named `LC_MESSAGES` inside. Inspect another file named `django.po` file with your editor.

* Build `mo` translation file from gettext `po`

	```sh
	python manage.py compilemessages -l jp
	```
