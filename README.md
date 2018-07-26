# Django RESTful API echo server

Demo a echo server using Django RESTfull framework.

## Install

1. Establish virtual environment first
2. `source <your_virtual_environment>/bin/activate`
3. `pip install -r requirements.txt`

### test uwsgi

```
uwsgi --wsgi-file demo/test-wsgi.py
```

## Configuration

Change your `demo/uwsgi.ini`:

Change `chdir = <this_repo>/demo` to your project directory.

## Usage

Start server by `uwsgi demo/uwsgi.ini`.

It will open a http socket on 127.0.0.1:8080 and a monitoring port on 8181.

You can try using GET method:

```
http://127.0.0.1:8080/echo/?number=123
```

