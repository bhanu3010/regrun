regrun
=========

A minimalist client to launch regressions on web sockets.

Features
--------

-   Launches requested test suites in background.
-   Provides real-time updates of each test to browser on web-sockets.
-   Provides a tests status reporting dashboard.
-   Real-time updates to all connected clients irrespective of requester.
-   Works independent of browser support to websockets.


Demo
-----

![Imgur](https://i.imgur.com/tynYdZq.gif)

Installation
------------

Code is tested on 2.7.13 & Python 3.5. Older versions of Python including 2.7 are expected to work.

Steps to setup the environment:

Create a virtual environment and install the requirements with pip.

``` {.sourceCode .bash}
virtualenv venv
. venv/bin/activate
cd venv
git clone https://github.com/bhanu3010/regrun.git
cd regrun
pip install -r requirements.txt
```

-   Install latest mongodb version for DB transactions.

``` {.sourceCode .bash}
cd $(VIRTUALENV_PROJECT_DIR); python manage.py runserver -h '0.0.0.0' -p 5000 -r
```

Note: Entire application is tested on debian-wheezy platform.

TODO
----

-   Retry failed tests from UI.
-   Enable TLS + authentication/authorization layer.

