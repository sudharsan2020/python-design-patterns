from ..abs_cust import AbsCust


class Government(AbsCust):
    def report_type(self):
        print(f'"{self.name}" is a government saver.')
