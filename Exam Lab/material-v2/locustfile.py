import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task(10)
    def add(self):
        for a in range(10):
            self.client.get(f"/add?a={a}00&b=999", name = "add")
            time.sleep(1)

    @task()
    def sub(self):
        for a in range(10):
            self.client.get(f"/sub?a={a}00&b=999", name = "sub")
            time.sleep(1)
    
    @task()
    def mul(self):
        for a in range(10):
            self.client.get(f"/mul?a={a}00&b=999", name = "mul")
            time.sleep(1)
        
    @task()
    def secret(self):
        for a in range(10):
            self.client.get(f"/secret?X={a}", name = "secret")
            time.sleep(1)
    