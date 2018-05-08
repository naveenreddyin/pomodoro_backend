This project is built in Django framework.

This is the backend application for Pomodoro Timer app


## Getting started with this project


### `Clone this repo`

```
git clone https://github.com/naveenreddyin/pomodoro_backend.git
```

Than,
```
cd pomodoro_backend
```

### `Install packages`

Run the following command:
```
pip install -r requirements.txt
```

### `Run project on development mode`

```
python manage.py runserver
```


### `Run tests`

```
python manage.py test
```

Or, if you have Coverage installed, than,

```
coverage run manage.py test
```


## Comments
* This project is hosted on Heroku.
* This task could be acessed via production: https://pomodorobackend.herokuapp.com/admin/, with username/password being sent in email.
* This project runs on Python2.
* This project uses postgres on production, but on localhost it will use sqlite, so no extra settings for that.
* After logging into the admin site, You can update Pomodoro table with the desired timer settings. The default settings picked up by the app is the first one, so update that in
order to apply the settings.
* One more table which will appear will be Task, in Django admin, you can update tasks there as well.
