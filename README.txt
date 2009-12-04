Paste Call
==========

It is a `paste script`_ plugin that makes it possible to run custom commands from console. Example:

    ``$ paster call my.package:callable``

Optionally it can take a WSGI application config file and load that application

    ``$ paster call my.package:callable --with-config=../production.cfg``

Note that entry points will only be found if:

    - the config file is provided and/or
    - the project has been registered in the environment with
        ``$ python setup.py develop/install/etc``

Mercurial repository can be found at bitbucket.org_

.. _paste script: http://pythonpaste.org/script
.. _bitbucket.org: http://bitbucket.org/kaukas/pastecall

