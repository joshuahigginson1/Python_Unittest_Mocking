"""In this script, we will write a test which uses a mocked response."""

# Imports --------------------------------------------------------------

from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

# Test Classes ---------------------------------------------------------


class TestBase(TestCase):
    """This class forms the basis for our other unit tests, using the
    TestCase built-in from flask_testing."""

    def create_app(self):
        """This function returns our application application. It is
        required for use with flask_testing."""
        return app


class TestResponse(TestBase):
    """This test class is designed to test our HTTP
    responses to an external API."""

    def test_football(self):
        """This test simulates returning a request from an external API,
        and getting back a response of 1."""

        with patch('requests.get') as get_api_request:
            get_api_request.return_value.text = "1"

            response = self.client.get(url_for('sport'))
            self.assertIn(b'Football', response.data)

    def test_badminton(self):
        """This test simulates returning a request from an external API,
        and getting back a response of 2."""

        with patch('requests.get') as get_api_request:
            get_api_request.return_value.text = "2"

            response = self.client.get(url_for('sport'))
            self.assertIn(b'Badminton', response.data)

    def test_hockey(self):
        """This test simulates returning a request from an external API,
        and getting back a response of 3."""

        with patch('requests.get') as get_api_request:
            get_api_request.return_value.text = "3"

            response = self.client.get(url_for('sport'))
            self.assertIn(b'Hockey', response.data)

    def test_else(self):
        """This test simulates returning a request from an external API,
        and getting back a response of 3."""
        with patch('requests.get') as get_api_request:
            get_api_request.return_value.text = "35"

            response = self.client.get(url_for('sport'))
            self.assertIn(b'Boxing', response.data)

