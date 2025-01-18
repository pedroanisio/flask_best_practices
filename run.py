# -*- coding: utf-8 -*-
# @Time    : 2019-05-15 15:52
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : run.py
# @Software: PyCharm

import os
import platform
import threading
import datetime

from ApplicationExample import create_app

app = create_app()


def show():
    flask_env = os.environ.get('FLASK_ENV')
    print('<', '-' * 66, '>')
    print('Time: {}'.format(datetime.datetime.now()))
    print('Operating System: {}'.format(platform.system()))
    print('Project Path: {}'.format(os.getcwd()))
    print('Current Environment: {}'.format(flask_env))
    print('Parent Process ID: {}'.format(os.getppid()))
    print('Child Process ID: {}'.format(os.getpid()))
    print('Thread ID: {}'.format(threading.get_ident()))
    # print(app.url_map)
    print('<', '-' * 66, '>')


def main():
    """Start the application"""

    host = app.config['RUN_HOST']
    port = app.config['RUN_PORT']
    debug = app.config['DEBUG']

    # Start on Linux server
    if platform.system() == 'Linux':
        app.run(host=host, port=port)
    else:
        # app.run(debug=True, host='0.0.0.0', port=9999)
        os.environ['is_debug'] = "is_debug"
        app.run(debug=debug, host=host, port=port)


if __name__ == '__main__':
    """
    # Set environment variables
    export FLASK_ENV='development'
    export FLASK_ENV='production'
    export FLASK_ENV='docker_production'
    """

    show()
    main()
