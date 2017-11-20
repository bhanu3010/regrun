import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Default config."""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY',
                                '51f52814-0071-11e6-a247-000ec6c2372c')
    MONGOALCHEMY_DATABASE = 'regrunner'

    TEST_DIR = 'vbb-rest-python/tests'
    TEST_TEMPLATE_MAP = {'VBB_API_stations_test': 'test_stations.py',
                         'VBB_API_journeys_test': 'test_journeys.py',
                         'VBB_API_lines_test': 'test_lines.py',
                         'VBB_API_locations_test': 'test_locations.py',
                         'VBB_API_radar_test': 'test_radar.py',
                         'VBB_API_shapes_test': 'test_shapes.py'
                         }
    PYTEST_CLI = 'python -m pytest -s -x %s'


class DevelopmentConfig(Config):
    """Dev config."""
    DEBUG = True


class TestingConfig(Config):
    """Test config"""
    DEBUG = True


class ProductionConfig(Config):
    """Prod config"""
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
