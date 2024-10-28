from flask.cli import FlaskGroup

from project import app

cli = FlaskGroup(app)

if __name__ == "__main__":
    cli.main(args=['run', '--host','0.0.0.0'])
