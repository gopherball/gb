.. image:: https://gb.readthedocs.io/en/latest/_static/logo-readme.png
    :width: 950px
    :align: center

gb
##

.. image:: https://travis-ci.org/supakeen/gb.svg?branch=master
    :target: https://travis-ci.org/supakeen/gb

.. image:: https://readthedocs.org/projects/gb/badge/?version=latest
    :target: https://gb.readthedocs.io/en/latest/

.. image:: https://gb.readthedocs.io/en/latest/_static/license.svg
    :target: https://github.com/supakeen/gb/blob/master/LICENSE

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black


About
=====

``gb`` or gopherball is a gopher server written in Python with the main goals of
ease of use and integration. The name gopherball is inspired by a recurring
theme in the Calvin & Hobbes comicbooks and a tongue in cheek reference of an
alternative to the World Wide Web as we know it today.

Examples
========
Quick examples to get you running.

``gb --mode=implicit .`` will start a gopher server on ``127.0.0.1`` port ``7070`` serving
a recursive index of files starting from the current directory.

``gb --mode=explicit /home/user/explicit.json`` will start a gopher server on 
``127.0.0.1`` port ``7070`` with an index generated from the passed configuration
file. For the format of this file see ``gb``'s documentation.

``gb --mode=implicit --magic .`` will start ``gb`` in magic-mode on ``127.0.0.1`` port
``7070``. Magic mode will make ``gb`` guess at filetypes and parse .gb files as
templates. For more information on magic mode see ``gb``'s documentation.

``gb --mode=implicit --host="127.1.1.1" --port 1025 .`` will start ``gb`` in implicit
mode on the chosen ip and port. Note that using ports under 1024 requires
superuser permissions!

Technology
==========
``gb`` is written with the help of Python 3.5 and higher and the Tornado
framework for its networking.

Modes
=====
``gb`` has two main modes of operation that are commonly used. Each has its
appeal for differing usecases.

implicit
--------
Implicit mode serves a directory recursively. Indexes are automatically
generated and text files are served to the client. Data files are also
supported.

explicit
--------
Explicit mode requires a configuration which maps each path to a certain
asset. This mode will generate indexes not based on the file system but based
on a configuration file.

Magic
=====
``gb`` will serve all non-directories as type 9 files, these are non-readable
files and most clients will prompt for download. Turning on magic with
``--magic`` will let ``gb`` try to determine the correct filetypes.

Turning on magic will also start templating special ``.gb`` files. See
documentation for what you can do with templating.

Contributing
============
The source code for ``gb`` lives on GitHub where you can also submit issues and
pull requests. It mostly needs help by people with the ability to test in
various clients and libraries that might still support the gopher protocol.

Typing
======
An often asked question is why ``gb`` does not use any of Python 3.6+'s type
annotations. The answer is quite simply that ``gb`` wants to support ``pypy`` as
well as CPython. When ``pypy`` catches up to 3.6 type annotations will be added.

``gb`` loves to run on ``pypy`` so give it a whirl!
