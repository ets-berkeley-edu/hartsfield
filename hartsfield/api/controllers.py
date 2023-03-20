"""
Copyright ©2023. The Regents of the University of California (Regents). All Rights Reserved.
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
from flask import current_app as app

@app.route('/api/user/<user_id>/url', methods=['GET', 'POST'])
def get_user_url(user_id=None):
    # TO DO: Actual fetching logic
    response = [{
            "user": 'Cesar Villalobos',
            "signed_url": 'https://thisismymockurl.berkeley.edu/9fed0c91c15a01c86cac2a6e74eede0e',
            "expiration_date": '12/31/2023'
        },
        {
            "user": 'Cesar Villalobos',
            "signed_url": 'https://thisismymockurl.berkeley.edu/406dae77319aa765d84e9f81dc586d71',
            "expiration_date": '04/12/2023'
        }
    ]
    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    return '<p>logging you in... </p>' #do_the_login()

@app.route('/')
def hello_world():
    return "<p>Hello World</p>"

