"""
Contains tasks that locusts will perform as part of the performance test
"""
import logging
from random import randint
from locust import TaskSet, task

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class ContactSite(TaskSet):
    """
    A simple test that simply contacts the site
    """
    @task(1)
    def check_root(self):
        self.client.get("/")


class CheckValidJSON(TaskSet):
    """
    A task that generates a JSON schema, some random JSON data, and validates
    it against the TopChef server
    """
    @property
    def json_schema(self):
        """

        :return: The JSON schema against which the random data is to be
            validated
        """
        return {
            '$schema': 'http://json-schema.org/schema#',
            'title': 'Single-parameter JSON schema',
            'type': 'object',
            'properties': {
                'value': {
                    'type': 'integer',
                    'minimum': 1,
                    'maximum': 10
                }
            },
            'required': ['value']
        }

    @staticmethod
    def generate_random_valid_json():
        """

        :return: Some compliant JSON documents
        """
        return {'value': randint(1, 10)}

    @staticmethod
    def generate_random_invalid_json():
        """

        :return: Non-compliant JSON documents
        """
        return {'value': randint(11, 10000)}

    @task(2)
    def check_valid_json(self):
        """

        Post a valid JSON document and the schema. Check that the status code
        is correct.
        """
        body = {
            'object': self.generate_random_valid_json(),
            'schema': self.json_schema
        }
        with self.client.post(
            "/validator",
            json=body,
            headers={'Content-Type': 'application/json'},
            catch_response=True,
        ) as response:
            log.debug(
                "Successful JSON validator has status code %s",
                response.status_code
            )
            log.debug('Success validator response %s', response.text)

    @task(1)
    def check_invalid_json(self):
        """

        :return: Post invalid JSON and check that the status code is correct
            for an invalid response
        """
        body = {
            'object': self.generate_random_invalid_json(),
            'schema': self.json_schema
        }

        with self.client.post(
                "/validator",
                json=body,
                catch_response=True,
                headers={'Content-Type': 'application/json'}
        ) as response:
            log.debug(
                "Failed JSON validator has status code %s",
                response.status_code
            )
            if response.status_code == 400:
                response.success()
