import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task()
    def add(self):
        for a in range(10):
            self.client.get(f"/math/add?a={a}00&b=999", name = "add")
            time.sleep(1)

    @task()
    def sub(self):
        for a in range(10):
            self.client.get(f"/math/sub?a={a}00&b=999", name = "sub")
            time.sleep(1)
    
    @task()
    def mul(self):
        for a in range(10):
            self.client.get(f"/math/mul?a={a}00&b=999", name = "mul")
            time.sleep(1)
    
    @task()
    def div(self):
        for a in range(10):
            self.client.get(f"/math/div?a={a}00&b=999", name = "div")
            time.sleep(1)
    
    @task()
    def concat(self):
        for a in range(10):
            self.client.get(f"/str/concat?a={a}00&b=999", name = "concat")
            time.sleep(1)
    
    @task()
    def lower(self):
        for _ in range(10):
            self.client.get(f"/str/lower?a=AAAAA", name = "lower")
            time.sleep(1)

    @task()
    def upper(self):
        for _ in range(10):
            self.client.get(f"/str/upper?a=aaaaa", name = "upper")
            time.sleep(1)

    @task()
    def middle(self):
        for _ in range(10):
            self.client.get(f"/str/middle", name = "middle")
            time.sleep(1)