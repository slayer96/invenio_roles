from __future__ import absolute_import, print_function

from flask import Flask, g
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
from invenio_admin import InvenioAdmin
# from action_setting import *

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

FlaskCLI(app)
Babel(app)
Mail(app)
Menu(app)
InvenioDB(app)
InvenioAccounts(app)
app.register_blueprint(blueprint)

InvenioAdmin(app, permission_factory=lambda x: x,
             view_class_factory=lambda x: x)

access = InvenioAccess(app)

action_read = ActionNeed('read')
access.register_action(action_read)
action_read_permission = DynamicPermission(action_read)


@app.route('/action_read')
@action_read_permission.require()
def action_read():
    pass


action_upload_content = ActionNeed('add_content')
access.register_action(action_upload_content)
upload_content_permission = DynamicPermission(action_upload_content)


@app.route('/action_add_content')
@upload_content_permission.require()
def action_add_content():
    pass


action_approve_content = ActionNeed('approve_content')
access.register_action(action_approve_content)
action_approve_content_permission = DynamicPermission(action_approve_content)


@app.route('/action_approve_content')
@action_approve_content_permission.require()
def action_approve_content():
    pass


action_reject_content = ActionNeed('reject_content')
access.register_action(action_reject_content)
action_reject_content_permission = DynamicPermission(action_reject_content)


@app.route('/action_reject_content')
@action_reject_content_permission.require()
def action_reject_content():
    pass


admin_permission = DynamicPermission(RoleNeed('admin'))




@app.route('/role_admin')
@admin_permission.require()
def role_admin():
    identity = g.identity
    actions = {}
    for action in access.actions:
        actions[action.value] = DynamicPermission(action).allows(identity)


content_submission_permission = DynamicPermission(RoleNeed('content_submission'))


@app.route('/role_content_submission')
@content_submission_permission.require()
def role_content_submission():
    identity = g.identity
    actions = {}
    actions[action_approve_content.value] = action_approve_content_permission.allows(identity)
    actions[action_reject_content.value] = action_reject_content_permission.allows(identity)


content_contributors_permission = DynamicPermission(RoleNeed('content_contributors'))


@app.route('/role_content_contributors')
@content_contributors_permission.require()
def role_content_contributors():
    identity = g.identity
    actions = {}
    actions[action_upload_content.value] = upload_content_permission.allows(identity)


visitors_permission = DynamicPermission(RoleNeed('visitors'))


@app.route('/role_visitors')
@visitors_permission.require()
def role_visitors():
    identity = g.identity
    actions = {}
    actions[action_read.value] = action_read_permission.allows(identity)


