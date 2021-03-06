# Minimalistic WSGI compliant web framework

This is an example of almost minimum functionality required to build a web framework around WSGI protocol and uWSGI app particularly.

It supports working with HTTP methods, headers, query string parameters, and body

## Requirements
The framework and example application are intended to work under UNIX-like operating systems and only tested with Fedora 26. Everything below is applicable to Fedora 26, but *should* also work with other UNIX-like OSs.
 
You will need `uwsgi` application installed to run your web server
You can install it with 

```pip install uwsgi```

## Run example
The example application can be run with uwsgi app from root directory:

```uwsgi --socket 0.0.0.0:8080 --protocol=http -w example```

## Debug
The debug capability for PyCharm IDE is present. It is done via remote debug facility of the IDE.
### Requirements
- Put `pycharm-debug-py3k.egg` file into the framework folder. The file can be found in PyCharm installation directory, typically in "debug-eggs" folder
- Set `PYCHARM_DEBUG` environment variable to `True`
### Running debug
- Start remote debug in PyCharm, configured to listen to `localhost` and port `4444`
- Run application as shown in **"Run example"** section
