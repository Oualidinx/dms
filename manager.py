from flask_migrate import Migrate, MigrateCommand
from flask_script import Shell, Manager
from main_app import create_app, db, application
import os
from main_app.users.models import *


application = create_app("testing")
manager = Manager(application)
migrate = Migrate(application, db, render_as_batch=True)


@application.shell_context_processor
def make_shell_context():
    return dict(app=application, db=db, User=User
                )


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()

