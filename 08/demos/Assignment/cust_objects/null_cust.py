from .abs_cust import AbsCust

class NullCust(AbsCust):
    def __init__(self,cust_type):
        self._cust_type = cust_type

    @property
    def name(self):
        return None

    @name.setter
    def name(self, name):
        pass

    def send_invoice(self):
        print(f'Customer type "{self._cust_type}" not found.')
