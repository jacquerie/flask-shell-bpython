=====================
 Flask-Shell-BPython
=====================

.. image:: https://travis-ci.org/jacquerie/flask-shell-bpython.svg?branch=master
    :target: https://travis-ci.org/jacquerie/flask-shell-bpython


About
=====

Replace the default ``flask shell`` command with a similar one running BPython.
Inspired by `flask-shell-ipython`_ by `@ei-grad`_.

.. _`flask-shell-ipython`: https://github.com/ei-grad/flask-shell-ipython
.. _`@ei-grad`: https://github.com/ei-grad


Install
=======

``flask-shell-bpython`` is on PyPI, so all you have to do is:

.. code-block:: console

    $ pip install flask-shell-bpython


Usage
=====

``flask-shell-bpython`` hooks itself into Flask through an entry point, so all
you have to do is:

.. code-block:: console

    $ flask shell


Alternatives
============

If you prefer IPython you can use `flask-shell-ipython`_, while if you prefer
PTPython you can use `flask-shell-ptpython`_.

.. _`flask-shell-ptpython`: https://github.com/jacquerie/flask-shell-ptpython


Author
======

Jacopo Notarstefano (`@Jaconotar`_)

.. _`@Jaconotar`: https://twitter.com/Jaconotar


License
=======

MIT
