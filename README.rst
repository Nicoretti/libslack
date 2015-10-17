libslack
========

libslack is a lightweight python wrapper around the `Slack-Web-Api <https://api.slack.com/web>`_.

.. note::
    Requires Python 3.x

* for an example see scmd.py which provides a command line interface for the slack api.

    .. code-block:: console

        User@Host ~ $ scmd auth.test --auth-token xoxb-xxxxxxxxxx-yyyyyyyyyyyyyyyyyyyyyyyy
        {'user_id': 'UXXXXXXXX', 'url': 'https://teamname.slack.com/', 'team': 'Teamname', 'user': 'username', 'team_id': 'TXXXXXXXX', 'ok': True}


* for further details check the documentation.

Dependencies
++++++++++++

* `docopt <http://docopt.org/>`_

.. note::
    the dependecy is only required for the provided command line tool.

Installation
++++++++++++

.. code-block:: console

   pip install git+https://github.com/Nicoretti/libslack.git



Author: Nicola Coretti (nicola.coretti@gmail.com)

