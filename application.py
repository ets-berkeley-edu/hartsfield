"""
Copyright ©2022. The Regents of the University of California (Regents). All Rights Reserved.

Permission to use, copy, modify, and distribute this software and its documentation
for educational, research, and not-for-profit purposes, without fee and without a
signed licensing agreement, is hereby granted, provided that the above copyright
notice, this paragraph and the following two paragraphs appear in all copies,
modifications, and distributions.

Contact The Office of Technology Licensing, UC Berkeley, 2150 Shattuck Avenue,
Suite 510, Berkeley, CA 94720-1620, (510) 643-7201, otl@berkeley.edu,
http://ipira.berkeley.edu/industry-info for commercial licensing opportunities.

IN NO EVENT SHALL REGENTS BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT, SPECIAL,
INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST PROFITS, ARISING OUT OF
THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN IF REGENTS HAS BEEN ADVISED
OF THE POSSIBILITY OF SUCH DAMAGE.

REGENTS SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE
SOFTWARE AND ACCOMPANYING DOCUMENTATION, IF ANY, PROVIDED HEREUNDER IS PROVIDED
"AS IS". REGENTS HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES,
ENHANCEMENTS, OR MODIFICATIONS.
"""

import os
import subprocess

from hartsfield.factory import create_app

"""Usage mode A:

>>> python run.py

Usage mode B:

>>> export FLASK_APP=run.py
>>> flask run --help
>>> flask run --debugger
>>> flask initdb
"""

# temporary code to debug the elastic beanstalk run context
# run the shell command pwd using os.system and append stdout and stderr to the file /tmp/commands.txt
os.system('/usr/bin/pwd >> /tmp/commands.txt 2>&1')
# run the shell command whoami using os.system and append stdout and stderr to the file /tmp/commands.txt
os.system('/usr/bin/whoami >> /tmp/commands.txt 2>&1')
# run the shell command ls using os.system and append stdout and stderr to the file /tmp/commands.txt
os.system('/usr/bin/ls >> /tmp/commands.txt 2>&1')
# run the shell command ls * using os.system and append stdout and stderr to the file /tmp/commands.txt
os.system('/usr/bin/ls * >> /tmp/commands.txt 2>&1')
# run the shell command which python using os.system and append stdout and stderr to the file /tmp/commands.txt
os.system('/usr/bin/which python >> /tmp/commands.txt 2>&1')

# read the file /tmp/commands.txt and print the contents to the console
with open('/tmp/commands.txt', 'r') as file:
    print(file.read())


# When running under WSGI, system environment variables are not automatically made available to Python code, and
# an app restart will result in configurations being lost. We work around this with an explicit load from the shell
# environment, sourcing from the Elastic Beanstalk-provided /opt/python/current/env file if available.
if __name__.startswith('_mod_wsgi'):
    command = ['bash', '-c', ' env']
    shell_environment = subprocess.Popen(command, stdout=subprocess.PIPE)
    for line in shell_environment.stdout:
        key, _, value = line.decode('utf-8').rstrip().partition('=')
        os.environ[key] = value

application = create_app()


@application.cli.command()
def initdb():
    pass


host = application.config['HOST']
port = application.config['PORT']


if __name__ == '__main__':
    application.logger.info('Starting development server on %s:%s', host, port)
    application.run(host=host, port=port)
elif __name__.startswith('_mod_wsgi'):
    application.logger.info('Will start WSGI server on %s:%s', host, port)
