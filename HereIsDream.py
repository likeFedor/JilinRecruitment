#-*- coding:utf-8 -*-
from app import	create_app,db
from flask_script import Manager
from flask_migrate import Migrate
from flask_migrate import Migrate, MigrateCommand
import unittest
app =create_app('default')
manager=Manager(app)
migrate=Migrate(app,db)
from tests.test_client import FlaskClientTestCase
@manager.command

def test():
#suite=unittest.TestSuite()
#suite.addTest(FlaskClientTestCase("test_home_page"))
#runner=unittest.TextTestRunner()
#runner.run(suite)
#����ִ��unittest hello world 
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
if __name__=='__main__':
	manager.run()