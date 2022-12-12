from ..abs_cust import AbsCust


class Commercial(AbsCust):
    def report_type(self):
        print(f'"{self.name}" is a commercial saver.')