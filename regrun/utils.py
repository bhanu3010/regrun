import datetime
import time
from cgi import escape

import gevent_subprocess as subprocess
import os
from requests import post

from .models import TestRunner

basedir = os.path.abspath(os.path.dirname(__file__))


def current_time():
    """Returns current time, used to save record creation time"""
    curr_time_in_epoch = time.time()
    hr_format = datetime.datetime.fromtimestamp(curr_time_in_epoch)
    return hr_format.strftime('%Y-%m-%d %H:%M:%S')


def save_record(record, **kwargs):
    """Helper function to save record to mongo"""

    _ = [setattr(record, attr, value) for attr, value in kwargs.items()
         if hasattr(record, attr) and attr != 'save']
    if 'save' in kwargs and kwargs['save'] is True:
        record.save()


def launch_test_runner(config, request_id, template, custom_path,
                       status_url, user_id):
    """Main function responsible to launch gevent threads in background.

    :param config: to derive test inputs from config.
    :param request_id: generated for each submitted requests.
    :param template: template to map against vbb API tests.
    :param custom_path: to launch tests.
    :param status_url: to which status events are emitted.
    :param user_id: (identification token issued while registering the user).

    """
    test_to_run = config.get('TEST_TEMPLATE_MAP').get(template)
    test_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             config.get('TEST_DIR'), test_to_run)
    cmd = config.get('PYTEST_CLI') % test_path

    # Buffer delay to accommodate record creation
    time.sleep(0.001)
    record = TestRunner.get_test_run(request_id)

    run_log = []

    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, cwd=basedir)

    # Iterate till process is alive
    while p.poll() is None:
        resp = p.stdout.readline().strip()

        # Escape and convert it to raw strings so that jinja2 doesnt hate!!
        raw_resp = escape(resp) if resp else resp
        post(status_url, json={'data': raw_resp, 'user_id': user_id,
                               'request_id': request_id, 'event': 'status'})

        run_log.append(raw_resp)
        record.run_log = "<br>".join(run_log) + "<br>"

        fields = dict(label='info', status='RUNNING', save=True)
        save_record(record, **fields)

    # Possible handler to catch cases where process terminates before
    # stdout is flushed. 
    # TODO: To optimize the code.
    pending = p.stdout.readlines()
    for line in pending:
        raw_resp = escape(line) if line else line
        post(status_url, json={'data': raw_resp, 'user_id': user_id,
                               'request_id': request_id, 'event': 'status'})
        run_log.append(raw_resp)

        record.run_log = "<br>".join(run_log) + "<br>"
        fields = dict(label='info', status='RUNNING', save=True)
        save_record(record, **fields)

    # Exit code evaluator
    return_code = p.wait()
    if return_code != 0:
        fields = dict(label='important', status='FAILED', save=True)
        save_record(record, **fields)

        post(status_url, json={'status': 'FAILED', 'user_id': user_id,
                               'request_id': request_id, 'event': 'conclude'})
    else:
        fields = dict(label='success', status='SUCCESS', save=True)
        save_record(record, **fields)
        post(status_url, json={'status': 'SUCCESS', 'user_id': user_id,
                               'request_id': request_id, 'event': 'conclude'})
