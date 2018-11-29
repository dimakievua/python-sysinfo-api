import os
import tempfile

import pytest
from sysinfo import create_app
from sysinfo import printinfo

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True
    })

    with app.app_context():
        printinfo.SysInfo("gb")

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
