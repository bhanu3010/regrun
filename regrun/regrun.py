from flask import Blueprint, render_template, request, current_app

from forms import ScheduleTestForm
from .models import TestRunner

main = Blueprint('main', __name__)


@main.route("/")
def index():
    """Index route handler"""
    tests = TestRunner.get_all_test_runs()
    return render_template("dashboard.html", Tests=tests)


@main.route("/event", methods=['POST'])
def event():
    """Event route handler

    Used to post interim status to the browser.
    """
    params = request.json
    user_id = params['user_id']
    event = params['event']
    request_id = params['request_id']

    ns = current_app.clients.get(user_id)
    if event == 'status':
        ts = params['data']
        ns.emit("response", {'args': ts, 'req_id': request_id,
                             'status': 'RUNNING'},
                namespace='/regrun',
                broadcast=True)
    elif event == 'conclude':
        status = params['status']
        ns.emit("exit", {'status': status, 'req_id': request_id},
                namespace='/regrun',
                broadcast=True)
    return 'ok'


@main.route("/schedule")
def schedule():
    """ScheduleTest form"""
    if request.method == "GET":
        return render_template("schedule.html",
                               form=ScheduleTestForm(request.form))


@main.route('/test/<_id>')
def test(_id):
    """Test route handler to emit individual test results"""
    test_run = TestRunner.get_test_run(int(_id))
    return render_template("test.html", test=test_run)
