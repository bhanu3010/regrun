from wtforms import Form, StringField, validators, IntegerField, SelectField


class ScheduleTestForm(Form):
    """Schedule Test Form to submit the request to trigger the tests."""
    requester = StringField('Name', [validators.Length(min=4, max=225)])
    env_id = IntegerField('EnvironmentID')
    interface = SelectField('Interface', choices=[('RESTAPI_v_1', 'VBB REST API v1'),
                                                  ('RESTAPI_v_2', 'VBB REST API v2'),
                                                  ('RESTAPI_v_3', 'VBB REST API v3')])
    template = SelectField('Template',
                           choices=[
                                    ('VBB_API_stations_test', 'VBB_API_stations_test'),
                                    ('VBB_API_journeys_test', 'VBB_API_journeys_test'),
                                    ('VBB_API_lines_test', 'VBB_API_lines_test'),
                                    ('VBB_API_locations_test', 'VBB_API_locations_test'),
                                    ('VBB_API_radar_test', 'VBB_API_radar_test'),
                                    ('VBB_API_shapes_test', 'VBB_API_shapes_test'),
                                    ])
    custom_path = StringField('CustomDirectory')
