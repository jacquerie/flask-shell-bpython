from setuptools import setup


setup(
    name="flask-shell-bpython",
    author="Jacopo Notarstefano",
    author_email="jacopo.notarstefano@gmail.com",
    description="Replace the default `flask shell` command with a similar command running BPython.",
    url="http://github.com/jacquerie/flask-shell-bpython",
    version="0.0.1",
    py_modules=['flask_shell_bpython'],
    install_requires=[
        'flask>=0.11',
        'click',
        'bpython>=0.15',
    ],
    entry_points={
        'flask.commands': [
            'shell=flask_shell_bpython:shell_command',
        ],
    },
)
