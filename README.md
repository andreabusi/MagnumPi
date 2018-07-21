# MagnumPi

A simple web application to manage Raspberry PI GPIO.

Actually work in progres...

## Features

- /lcd
- /gpio

## Deployment

To deploy this web application, follow the following steps.

Clone the repository:

```
git clone git@github.com:BubiDevs/MagnumPi.py
cd MagnumPi
```

Create the virtual environment and populate it with all the package dependencies:

```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Install gunicorn as production web server:

```
(venv) $ pip install gunicorn
```

To start MagnumPi under gunicorn:

```
(venv) $ gunicorn -b localhost:8000 -w 4 microblog:app
```

**Note**: If you need to access to web application from outside the deployment machine, you'll need to change *localhost* with the IP of the target machine.