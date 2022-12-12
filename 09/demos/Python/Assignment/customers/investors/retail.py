from ..abs_cust import AbsCust


class Retail(AbsCust):
    def report_type(self):
        print(f'"{self.name}" is a retail investor.')