"""
Describes performance tests
"""
from task_sets import ContactSite, CheckValidJSON
from locust import HttpLocust


class WebsiteContact(HttpLocust):
    """
    Locust that simply contacts the root user for the site
    """
    task_set = ContactSite
    min_wait = 100
    max_wait = 2000
    weight = 1


class JSONValidator(HttpLocust):
    """
    Locust that validates JSON against the server
    """
    task_set = CheckValidJSON
    min_wait = 100
    max_wait = 2000
    weight = 1
