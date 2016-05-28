from __future__ import absolute_import, print_function

from flask import Flask, g, render_template
from flask.ext.principal import ActionNeed, RoleNeed
from flask_babelex import Babel
from flask_cli import FlaskCLI
from flask_login import current_user
from flask_mail import Mail
from flask_menu import Menu
from invenio_accounts import InvenioAccounts
from invenio_accounts.views import blueprint
from invenio_db import InvenioDB

from invenio_access import InvenioAccess
from invenio_access.permissions import DynamicPermission
from action_setting import *

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = ''
FlaskCLI(app)
Babel(app)
Mail(app)
Menu(app)
InvenioDB(app)
InvenioAccounts(app)
app.register_blueprint(blueprint)


access = InvenioAccess(app)

action_read = ActionNeed('read')
access.register_action(action_read)

action_add_content = ActionNeed('add_content')
access.register_action(action_add_content)

action_approve_content = ActionNeed('approve_content')
access.register_action(action_approve_content)


action_reject_content = ActionNeed('reject_content')
access.register_action(action_reject_content)


@app.route("/")
def index():
    identity = g.identity
    actions = {}
    for action in access.actions:
        actions[action.value] = DynamicPermission(action).allows(identity)

    if current_user.is_anonymous:
        return render_template("invenio_access/open.html",
                               actions=actions,
                               identity=identity)
    else:
        return render_template("invenio_access/limited.html",
                               message='',
                               actions=actions,
                               identity=identity)


admin_permission = DynamicPermission(RoleNeed('admin'))
@app.route('/role_admin')
@admin_permission.require()
def role_admin():
    identity = g.identity
    actions = {}
    for action in access.actions:
        actions[action.value] = DynamicPermission(action).allows(identity)

    message = ''
    return render_template("base.html",
                           message=message,
                           actions=actions,
                           identity=identity)


content_submission_permission = DynamicPermission(RoleNeed('content_submission'))
@app.route('/role_content_submission')
@content_submission_permission.require()
def role_content_submission():
    identity = g.identity
    actions = {}
    actions[action_approve_content.value] = action_approve_content_permission.allows(identity)
    actions[action_reject_content.value] = action_reject_content_permission.allows(identity)


    message = ''
    return render_template("invenio_access/limited.html",
                           message=message,
                           actions=actions,
                           identity=identity)



content_contributors_permission = DynamicPermission(RoleNeed('content_contributors'))
@app.route('/role_content_contributors')
@content_contributors_permission.require()
def role_content_contributors():
    identity = g.identity
    actions = {}

    actions[action_upload_content.value] = upload_content_permission.allows(identity)

    message = ''
    return render_template("base.html",
                           message=message,
                           actions=actions,
                           identity=identity)


visitors_permission = DynamicPermission(RoleNeed('visitors'))
@app.route('/role_visitors')
@visitors_permission.require()
def role_visitors():
    identity = g.identity
    actions = {}
    actions[action_read.value] = action_read_permission.allows(identity)
    message = ''
    return render_template("base.html",
                           message=message,
                           actions=actions,
                           identity=identity)


if __name__ == '__main__':
    app.run()
