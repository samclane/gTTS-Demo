# gTTS-Demo

<img align="right" width="196" height="196" title="RedBot" src="./hello/static/red_favicon_196.png">

A testing utility for the `gTTS` Python Module. 

## Screenshot

![](./hello/static/screenshot.png)

## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/heroku/gTTS-demo.git
$ cd python-getting-started

$ python3 -m venv gTTS-demo
$ pip install -r requirements.txt

$ createdb gTTS-demo

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
