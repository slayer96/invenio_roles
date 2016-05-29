Create database and tables:
.. code-block:: console
   $ cd examples
   $ flask -a app.py db init
   $ flask -a app.py db create
Create some users:
.. code-block:: console
   $ flask -a app.py users create -e info@invenio-software.org -a
   $ flask -a app.py users create -e reader@invenio-software.org -a
   $ flask -a app.py users create -e editor@invenio-software.org -a
   $ flask -a app.py users create -e admin@invenio-software.org -a
Add a role to a user:
.. code-block:: console
   $ flask -a app.py roles create -n admin
   $ flask -a app.py roles add -u info@invenio-software.org -r admin
   $ flask -a app.py roles add -u admin@invenio-software.org -r admin
Assign some allowed actions to this users:
.. code-block:: console
   $ flask -a app.py access allow open -e editor@invenio-software.org
   $ flask -a app.py access deny open -e info@invenio-software.org
   $ flask -a app.py access allow read -e reader@invenio-software.org
   $ flask -a app.py access allow open -r admin
   $ flask -a app.py access allow read -r admin
