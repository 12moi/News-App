


from app import create_app
from flask_script import Manager, Server

# import app

app=create_app('production')

manager=Manager(app)
manager.add_command('server',Server)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

manager.add_command('server',Server)
if __name__=='__main__':
    app.run()