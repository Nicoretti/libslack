#!/usr/bin/env python3
#
# Copyright (c) 2015, Nicola Coretti
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys

import docopt

from libslack import slackapi
from libslack.utils import try_to_get_auth_token

__version__ = "0.5.0"
__author__ = 'Nicola Coretti'
__email__ = 'nico.coretti@gmail.com'


def main():
    """
    Usage:
      scmd (API_COMMAND | -h | -v ) [<params>] [--auth-token=<token>]

    Options:
      -h -                  Show this screen.
      -v                    Show version.
      --auth-token=<token>  The authentication token which will be used to access
                            the slack api.
                            As an alternative you can specify it in the .slackrc
                            or set the $SLACK_API_TOKEN environment variable.
    """
    args = docopt.docopt(doc=main.__doc__, version='0.0.1')
    auth_token = None
    if args['API_COMMAND']:
        auth_token = try_to_get_auth_token(args)
        if not auth_token:
            print("Error: No authentication token available!", file=sys.stderr)
            exit(-1)
        slack_api = slackapi.SlackApi(authentication_token=auth_token)
        response = slack_api.call(args['API_COMMAND'], parameters=eval(args['<params>']))
        if response.is_error():
            error_message = "Error occured, details: {0}"
            print(error_message.format(response.get_error_message()), file=sys.stderr)
            exit(-2)
        print(response.data)
        exit(0)


if __name__ == "__main__":
    main()
