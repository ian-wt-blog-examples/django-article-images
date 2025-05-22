# django-article-images
A simple Django app that allows for images to be used with blog posts

Check out my article [How Do You Embed Images in a Django Blog From a WYSIWYG Editor?](https://ianwaldron.com/blog/how-do-you-embed-images-in-a-django-blog-from-a-wysiwyg-editor/) for more information.

## Setup

Once you've cloned a local copy of the repo, first create a virtual environment.

```shell
python3 -m venv env
```

This operation might take a few seconds. Once installed, activate the virtual environment.

```shell
source env/bin/activate
```

Next, install the requirements (Django, etc.)

```shell
pip install -r requirements.txt
```

## Migrate Database

The migrations for the three models (Category, Tag, & Article) have already been created. All you need to do is migrate the database.

```shell
python manage.py migrate
```
## Admin

You're almost ready to access the admin portal to begin creating and working with data. First, you need a user account with admin privileges (is_staff=True).

I've created a fixture that will produce a default user so you can get up and running right away. To user this user account, load the fixture into the database.

```shell
python manage.py loaddata users
```

Now start the application on a development server to access the admin portal.

```shell
python manage.py runserver
```

Navigate to the admin login page running on the development server exposed at port 8000.

[admin login](http://127.0.0.1:8000/admin/login)

You may now login with the default user's credentials:
* username: "example"
* password: "not-secure"

From here, you can now create and update objects.

Alternatively, you can load dummy data if you don't wish to do so manually.

```shell
python manage.py loaddata categories tags articles
```

Note: the order the fixtures are in when they're loaded matters due to dependencies.