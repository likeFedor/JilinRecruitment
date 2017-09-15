#-*- coding:utf-8 -*-
from app import	create_app,db
from flask_script import Manager,Shell
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Follow, Role, Permission, Post, Comment
import unittest
app =create_app('default')
manager=Manager(app)
migrate=Migrate(app,db)
#flask-script模块,通过shell模式创建数据库 1、python *.py shell  2、db.create_all()
def make_shell_context():
    return dict(app=app, db=db, User=User, Follow=Follow, Role=Role,
                Permission=Permission, Post=Post, Comment=Comment)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

from tests.test_client import FlaskClientTestCase
@manager.command
def test():
#suite=unittest.TestSuite()
#suite.addTest(FlaskClientTestCase("test_home_page"))
#runner=unittest.TextTestRunner()
#runner.run(suite)
#批量执行unittest hello world 
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

#部署时直接执行这个命令就行1、python manage.py delpoy
@manager.command
def deploy():
    """Run deployment tasks."""
    from flask_migrate import upgrade
    from app.models import Role, User

    # migrate database to latest revision
    upgrade()

    # create user roles
    Role.insert_roles()

    # create self-follows for all users
    User.add_self_follows()

if __name__=='__main__':
	manager.run()