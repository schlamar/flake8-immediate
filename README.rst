Flake8 immediate output
=======================

This module adds immediate output option for ``flake8``, the Python code
checker.

Usually, ``flake8`` delays the output until a file is completely
processed. With the *immediate* option, ``flake8`` prints the errors
directly without any delay. So this option provides the possibility to
get a streaming pipe from a ``flake8`` subprocess. A real world use case
is represented by https://github.com/schlamar/SublimeStreamingLinter.

This has the drawback that the output is not sorted across the various
checkers.


Installation
------------

You can install or upgrade ``flake8-immediate`` with these commands::

  $ pip install flake8-immediate
  $ pip install --upgrade flake8-immediate


Plugin for Flake8
-----------------

When both ``flake8 2.0`` and ``flake8-immediate`` are installed, the plugin is
available in ``flake8``::

    $ flake8 --version
    2.0 (pep8: 1.4.5, mccabe: 0.2, flake8-immediate: 0.1, pyflakes: 0.6.1)


Usage
-----

Just pass the ``--immediate`` option to ``flake8``::

    $ flake8 --help
    Usage: flake8 [options] input ...

    Options:
      ...
      --immediate           don't cache the error output until EOF
      ...


Changes
-------


0.2 - 2013-04-03
````````````````
* Fixed setup for Python 3.



0.1 - 2013-03-27
````````````````
* First release
