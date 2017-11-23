"""
Describes performance tests
"""
from locust import HttpLocust, TaskSet, task


class ContactSite(TaskSet):
    """
    A simple test that simply contacts the site
    """
    @task(1)
    def check_root(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    """
    Fake user for the site
    """
    task_set = ContactSite
    min_wait = 100
    max_wait = 2000

