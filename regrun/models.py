from . import db


class TestRunner(db.Document):
    """TestRunner mongo collection to store all regrun requests and results"""
    request_id = db.IntField()
    requester = db.StringField()
    env_id = db.IntField()
    interface = db.StringField()
    template = db.StringField()
    custom_path = db.StringField()
    creation_time = db.StringField()
    status = db.StringField()
    run_log = db.StringField()
    label = db.StringField()

    @classmethod
    def get_all_test_runs(cls):
        """Retrieves all the tests scheduled/completed."""
        return cls.query.all()

    @classmethod
    def get_test_run(cls, _id):
        """Retrieves one single test matching the _id argument passed"""
        return cls.query.filter(TestRunner.request_id == _id).first()
