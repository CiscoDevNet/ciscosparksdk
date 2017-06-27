=============
ciscosparksdk
=============

*Batteries added, community developed Python SDK for Cisco Spark*

.. image:: https://img.shields.io/pypi/v/ciscosparksdk.svg
    :target: https://pypi.python.org/pypi/ciscosparksdk
.. image:: https://readthedocs.org/projects/ciscosparksdk/badge/?version=latest
    :target: http://ciscosparksdk.readthedocs.io/en/latest/?badge=latest

-------------------------------------------------------------------------------

**ciscosparksdk** is a *community developed* Python Software Development Kit
for working with the `Cisco Spark`_ cloud collaboration platform.  It extends
the capabilities of the `ciscosparkapi`_ API wrapper to include additional
tools and methods that make working with Cisco Spark via Python even more
enjoyable!


Project & Package Status
------------------------

**Alpha!**  Tread lightly.  😃

This project is currently under initial alpha-level development.  Expect the
package APIs to change.  Expect bugs.  Help us squash them and add features!


Features
--------

ciscosparksdk enhances your developer experience by providing:

+ Convenience objects and methods that make interacting with Cisco Spark a
  python-native and natural experience.  For example:

  + Access your Spark rooms using builtin "rooms list" convenience objects.

  + Instead of having to locate and pass around object IDs, like when you want
    to create a message in room and you have to find and then provide the
    room's ID to the create-message API, why not just have a ``create_message``
    convenience method available underneath your room object so you can simply
    say ``room.create_message()`` or ``room.add_person()``?  We do that.  😎

+ We also provide a community framework for capturing and contributing
  solutions to common needs that often arise when working with Cisco Spark.

Community Development
---------------------

Want to find a room by name?  Why should all of us write the same functions
over and over again?  Let's do it once, iterate the solutions if they can be
improved, and save all of us time and effort while contributing and increasing
the quality of the code we all use.

Installation
------------

Installing and upgrading ciscosparksdk is easy:

**Install via PIP**

.. code-block:: bash

    $ pip install ciscosparksdk

**Upgrading to the latest Version**

.. code-block:: bash

    $ pip install ciscosparksdk --upgrade


Documentation
-------------

User documentation is being built simultaneously alongside the development of
the ciscosparksdk package.  Check it out at http://ciscosparksdk.readthedocs.io .

Your feedback and contributions to the documentation are also most welcome!


Examples
--------

We are going to need some... 🙂  Have a good example script you would like to
share?  Your `contribution`__ is most welcome!

__ Contribution_


Release Notes
-------------

Please see the releases_ page for release notes on the incremental
functionality and bug fixes incorporated into the published releases.

**Note:**  The package APIs may change, while the package is in under
development.


Support
-------

This is a *community developed* and *community supported* project.  If you
experience any issues using this package, please report them using the
issues_ log.


Contribution & Community Code of Conduct
----------------------------------------

Please the the `CONTRIBUTING`_ and `CODE_OF_CONDUCT`_ files for information on
how to contribute to this project and our expectations-of and commitment-to
open and professional conduct in the community surrounding this project.


*Copyright (c) 2017 Cisco Systems, Inc.*

.. _Cisco Spark: https://ciscospark.com
.. _ciscosparkapi: https://github.com/CiscoDevNet/ciscosparksdk
.. _ciscosparksdk: https://github.com/CiscoDevNet/ciscosparksdk
.. _ciscosparksdk.readthedocs.io: https://ciscosparksdk.readthedocs.io
.. _issues: https://github.com/CiscoDevNet/ciscosparksdk/issues
.. _releases: https://github.com/CiscoDevNet/ciscosparksdk/releases
.. _CONTRIBUTING: https://github.com/CiscoDevNet/ciscosparksdk/tree/master/CONTRIBUTING.rst
.. _CODE_OF_CONDUCT: https://github.com/CiscoDevNet/ciscosparksdk/tree/master/CODE_OF_CONDUCT.md
