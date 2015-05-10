from flask import session, jsonify, url_for, redirect, request
from octy import app
from flask_oauthlib.client import OAuth
from octy import db
from octy.models import User
from octy.models import LinkedinProfile
from octy.transactionalEmails import sendEmail

oauth = OAuth(app)

linkedin = oauth.remote_app(
    'linkedin',
    consumer_key='tgqpmdbwrca8',
    consumer_secret='udCHlYrbPLbLVNH1',
    request_token_params={
        'scope': 'r_emailaddress',
        'state': 'RandomString',
    },
    base_url='https://api.linkedin.com/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://www.linkedin.com/uas/oauth2/accessToken',
    authorize_url='https://www.linkedin.com/uas/oauth2/authorization',
)

@app.route('/')
def index():
    if 'linkedin_token' in session:
        me = linkedin.get('people/~')
        me.data['email'] = linkedin.get('people/~/email-address').data
        return jsonify(me.data)
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return linkedin.authorize(callback=url_for('authorized', _external=True))

@app.route('/logout')
def logout():
    session.pop('linkedin_token', None)
    return redirect(url_for('index'))

@app.route('/login/authorized')
def authorized():
    resp = linkedin.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['linkedin_token'] = (resp['access_token'], '')
    me = linkedin.get('people/~')
    dataEmail = me.data['email'] = linkedin.get('people/~/email-address').data

    # Check if user in db
    userInDb = False
    for email in db.session.query(LinkedinProfile.email):
        if (email[0] == dataEmail):
            userInDb = True
    

    # Save to db
    if (userInDb == False):
        userLinkedinProfile = LinkedinProfile(
            email=dataEmail,
            firstname=me.data['firstName'],
            lastname=me.data['lastName'],
            headline=me.data['headline']
        )
        user = User(
            email=dataEmail,
            linkedin_profile=userLinkedinProfile
        )

        sendEmail (user, 'newUser')

        db.session.add(user)
        db.session.commit()

    return jsonify(me.data)

@linkedin.tokengetter
def get_linkedin_oauth_token():
    return session.get('linkedin_token')

def change_linkedin_query(uri, headers, body):
    auth = headers.pop('Authorization')
    headers['x-li-format'] = 'json'
    if auth:
        auth = auth.replace('Bearer', '').strip()
        if '?' in uri:
            uri += '&oauth2_access_token=' + auth
        else:
            uri += '?oauth2_access_token=' + auth
    return uri, headers, body

linkedin.pre_request = change_linkedin_query
