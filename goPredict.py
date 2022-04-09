from model.predict import ret_predict
from algo.algo import algorithm

database = {}

class PredictAvailableMeals:
    def __init__(self):
        self._predicted_products = []
        self._list_of_products = []
        self._adress = None

    def pass_to_predict(self):
        lopp = ret_predict()
        for i in lopp:
            self._list_of_products.append(i[0])

    def add_adress_and_products(self, adress, products):
        self._adress = adress
        list_to_extend = products.split(';')
        list_to_extend.pop(0)
        self._list_of_products.extend(list_to_extend)

    def save_to_database(self):
        database[self._adress] = self._list_of_products

    def check_available_dishes(self):
        return algorithm(database)

    @property
    def list_of_products(self):
        return self._list_of_products

    @list_of_products.setter
    def list_of_products(self, val):
        self._list_of_products = val


    @property
    def adress(self):
        return self._adress

    @adress.setter
    def adress(self, val):
        self._adress = val
    # @property
    # def predicted_products(self):
    #     return self._predicted_products


_go_predict = None


def get_go_predict_object():
    global _go_predict
    if _go_predict is None:
        _go_predict = PredictAvailableMeals()
    return _go_predict

# d = PredictAvailableMeals()
#
# d.pass_to_predict()
# print(d.predicted_products)
