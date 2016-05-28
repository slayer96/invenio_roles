from __future__ import absolute_import, print_function

from flask import Flask
from invenio_accounts import InvenioAccounts
from flask import Flask, g, render_template
from invenio_admin import InvenioAdmin

from flask.ext.principal import ActionNeed, RoleNeed
from invenio_access import InvenioAccess
from invenio_access.permissions import DynamicPermission

app = Flask('app')

InvenioAccounts(app)
access = InvenioAccess(app)

InvenioAdmin(app, permission_factory=lambda x: x,
             view_class_factory=lambda x: x)


access = InvenioAccess(app)

action_read = ActionNeed('read')
access.register_action(action_read)

read_permission = DynamicPermission(action_read)
@app.route('/action_read')
@read_permission.require()
def action_read():
    identity = g.identity
    actions = {}
    for action in access.actions:
        actions[action.value] = DynamicPermission(action).allows(identity)

    message = ''
    return render_template("html",
                           message=message,
                           actions=actions,
                           identity=identity)


action_add_content = ActionNeed('add_content')
access.register_action(action_add_content)
add_content_permission = DynamicPermission(action_add_content)
@app.route('/action_add_content')
@add_content_permission.require()
def action_add_content ():
    identity = g.identity
    actions = {}
    for action in access.actions:
        actions[action.value] = DynamicPermission(action).allows(identity)

    message = ''
    return render_template("html",
                           message=message,
                           actions=actions,
                           identity=identity)


action_approve_content = ActionNeed('approve_content')
access.register_action(action_approve_content)
action_approve_content_permission = DynamicPermission(action_approve_content)
@app.route('/action_approve_content')
@action_approve_content_permission.require()
def action_approve_content():
    identity = g.identity
    actions = {}
    for action in access.actions:
        actions[action.value] = DynamicPermission(action).allows(identity)

    message = ''
    return render_template("html",
                           message=message,
                           actions=actions,
                           identity=identity)


action_reject_content = ActionNeed('reject_content')
access.register_action(action_reject_content)
action_reject_content_permission = ActionNeed(action_reject_content)
@app.route('/action_reject_content')
@action_reject_content_permission.require()
def action_reject_content():
    identity = g.identity
    actions = {}
    for action in access.actions:
        actions[action.value] = DynamicPermission(action).allows(identity)

    message = ''
    return render_template("html",
                           message=message,
                           actions=actions,
                           identity=identity)