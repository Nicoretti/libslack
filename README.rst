
libslack
========
.. image:: https://travis-ci.org/Nicoretti/libslack.svg?branch=master
    :target: https://travis-ci.org/Nicoretti/libslack

.. image:: https://coveralls.io/repos/Nicoretti/libslack/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/Nicoretti/libslack?branch=master

.. image:: https://readthedocs.org/projects/libslack/badge/?version=latest
    :target: http://libslack.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status


libslack is a lightweight python wrapper around the `Slack-Web-Api <https://api.slack.com/web>`_.
As part of libslack a small tool called scmd.py which provides a command line interface for the slack api.


Slack API
---------

.. code-block:: python

        slack_api = slackapi.SlackApi(authentication_token=auth_token)
        response = slack_api.call(args['API_COMMAND'], parameters=args['<params>'])

Slack CMD
---------

.. code-block:: console

    User@Host ~ $ scmd auth.test --auth-token xoxb-xxxxxxxxxx-yyyyyyyyyyyyyyyyyyyyyyyy
    {'user_id': 'UXXXXXXXX', 'url': 'https://teamname.slack.com/', 'team': 'Teamname', 'user': 'username', 'team_id': 'TXXXXXXXX', 'ok': True}


* for further details check the documentation.

Dependencies
------------

* `docopt <http://docopt.org/>`_

.. note::
    the dependecy is only required for the provided command line tool.

Installation
------------

.. attention::
    Requires Python >= 3.4


.. code-block:: console

   pip install git+https://github.com/Nicoretti/libslack.git

Author: Nicola Coretti (nicola.coretti@gmail.com)


