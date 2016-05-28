from __future__ import absolute_import, print_function

from invenio_admin import InvenioAdmin

from flask.ext.principal import ActionNeed, RoleNeed
from invenio_access import InvenioAccess
from invenio_access.permissions import DynamicPermission

from app import app


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
def action_add_content ():
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