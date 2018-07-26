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

### start manually

`uwsgi demo/uwsgi.ini`.

It will open a http socket on 127.0.0.1:8000 and a monitoring port on 8001.

### start docker

```
docker run -d -p 8000:8000 a504082002/echo-server-drf
```

### test

You can try using GET method:

```
http://127.0.0.1:8000/echo/?number=123
```

