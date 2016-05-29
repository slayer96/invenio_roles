Create database and tables:
.. code-block:: console
   $ cd examples
   $ flask -a app.py db init
   $ flask -a app.py db create
Create some users:
.. code-block:: console
   $ flask -a app.py users create  info@invenio-software.org -a
   $ flask -a app.py users create  reader@invenio-software.org -a
   $ flask -a app.py users create  editor@invenio-software.org -a
   $ flask -a app.py users create  admin@invenio-software.org -a
Add a role to a user:
.. code-block:: console
   $ flask -a app.py roles create -n admin
   $ flask -a app.py roles add  info@invenio-software.org admin
   $ flask -a app.py roles add  admin@invenio-software.org  admin
Assign some allowed actions to this users:
.. code-block:: console
   $ flask -a app.py access allow open  editor@invenio-software.org
   $ flask -a app.py access deny open  info@invenio-software.org
   $ flask -a app.py access allow read  reader@invenio-software.org
   $ flask -a app.py access allow open  admin
   $ flask -a app.py access allow read  admin
