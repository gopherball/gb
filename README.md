![gb logo, a gopher in a ball](https://gb.readthedocs.io/en/latest/_static/logo-doc.png)

# gb

![rtd badge](https://readthedocs.org/projects/gb/badge/?version=latest) ![license badge](https://gb.readthedocs.io/en/latest/_static/license.svg) ![black badge](https://img.shields.io/badge/code%20style-black-000000.svg)

## About

`gb` or gopherball is a gopher server written in Python with the main goals of
ease of use and integration. The name gopherball is inspired by a recurring
theme in the Calvin & Hobbes comicbooks and a tongue in cheek reference of an
alternative to the World Wide Web as we know it today.

## Examples
Quick examples to get you running.

`gb --mode=implicit .` will start a gopher server on `127.0.0.1` port `7070` serving
a recursive index of files starting from the current directory.

`gb --mode=implicit --magic .` will start `gb` in magic-mode on `127.0.0.1` port
`7070`. Magic mode will make `gb` guess at filetypes.

`gb --mode=implicit --host="127.1.1.1" --port 1025 .` will start `gb` in implicit
mode on the chosen ip and port. Note that using ports under 1024 requires
superuser permissions!

## Technology
`gb` is written with the help of Python 3.5 and higher and the Tornado
framework for its networking.

## Modes
`gb` has one main mode of operation that is commonly used. More modes are
planned for the future.

### implicit
Implicit mode serves a directory recursively. Indexes are automatically
generated and text files are served to the client. Data files are also
supported.

## Magic
`gb` will serve all non-directories as type 9 files, these are non-readable
files and most clients will prompt for download. Turning on magic with
`--magic` will let `gb` try to determine the correct filetypes.

## Contributing
The source code for `gb` lives on GitHub where you can also submit issues and
pull requests. It mostly needs help by people with the ability to test in
various clients and libraries that might still support the gopher protocol.
