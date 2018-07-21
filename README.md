# MagnumPi

A simple web application to manage Raspberry PI GPIO.

Actually work in progress...

## Available features

The following feature are already available

- **/lcd**: a sample page to send a text to I2C LCD display

## In development features

- **/gpio**

## Deployment

To deploy this web application, follow the following steps.

Clone the repository:

```
git clone git@github.com:BubiDevs/MagnumPi.py
cd MagnumPi
```

Create the virtual environment and populate it with all the package dependencies:

```
$ python3 -m venv --system-site-packages venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

(The option *--system-site-packages* is necessary to use Raspberry Pi system package as RPi.GPIO or smbus).

Install gunicorn as production web server:

```
(venv) $ pip install gunicorn
```

To start MagnumPi under gunicorn:

```
(venv) $ gunicorn -b localhost:8000 -w 4 magnumpi:app
```

**Note**: If you need to access to web application from outside the deployment machine, you'll need to change *localhost* with the IP of the target machine.


## References

* [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux)
* [How to setup an I2C LCD on the Raspberry Pi](http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/)
* [Raspberry Pi Pinout](https://it.pinout.xyz)