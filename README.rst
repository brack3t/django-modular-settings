=======================
django-modular-settings
=======================

Inspired during DjangoCon 2011. After creating six projects to test during the talks, I realized that setting up the ``settings.py`` file to be more modular was a real pain. I wrote this little script to automate the process.

Quick Overview
==============

Django's default way of doing settings kind of sucks. Adding::

  try:
    from local_settings import *
  except ImportError:
    pass

to the bottom of the ``settings.py`` works, but it doesn't allow you to extend settings. So, for example, you can't add ``django-debug-toolbar`` to just your local development without overriding the entire ``INSTALLED_APPS`` tuple.

What this script does:

1. Read in your current settings.
2. Creates a new folder named ``settings`` within the project directory.
3. Writes your current settings to ``base.py`` within the new settings package.
4. Creates a basic ``__init__.py`` file which imports ``base.py`` and looks for ``local.py``
5. Creates an empty ``local.py`` for your dev environment.
6. Deletes the default ``settings.py`` (and ``settings.pyc``, should it exist).

What You Get
============

Now you can edit ``local.py`` for you dev environment and extend things like ``INSTALLED_APPS`` but just for you. ::

  INSTALLED_APPS += (
    'debug-toolbar',
  )


Installation
============

This is a simple script that does not need to be installed or compiled. It's a run once and discard project. You will want to ``curl`` or ``wget`` the ``modular_settings.py`` file to your project directory. Specifically to the directory where the default Django ``settings.py`` file resides. ::

  curl -O https://raw.github.com/chrisjones-brack3t/django-modular-settings/master/modular_settings.py

Or, if you prefer wget::

  wget https://raw.github.com/chrisjones-brack3t/django-modular-settings/master/modular_settings.py

Usage
=====

After downloading the file, from your project directory, run the script. ::

  python modular_settings.py

Assuming everything goes as planned, you should see a message saying your settings are now a little more awesome.

Finally
=======

Delete the ``modular_settings.py`` file.