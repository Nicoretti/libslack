Tools
=====

Slack CMD
---------
Command line tool to interact with the slack web api.

Usage
++++++

.. code-block:: console

    Usage:

    scmd (API_COMMAND | -h | -v ) [<params>] [--auth-token=<token>]

    Options:
      -h                    Show this screen.
      -v                    Show version.
      --auth-token=<token>  The authentication token which will be used to access
                            the slack api.
                            As an alternative you can specify it in the .slackrc
                            or set the $SLACK_API_TOKEN environment variable.


Example
++++++++

.. code-block:: console

    User@Host ~ $ scmd auth.test --auth-token xoxb-xxxxxxxxxx-yyyyyyyyyyyyyyyyyyyyyyyy
    {'user_id': 'UXXXXXXXX', 'url': 'https://teamname.slack.com/', 'team': 'Teamname', 'user': 'username', 'team_id': 'TXXXXXXXX', 'ok': True}

