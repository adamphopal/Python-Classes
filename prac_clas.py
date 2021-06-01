#Nina Zakharenko - Elegant Solutions For Everyday Python Problems - PyCon 2018

class Money:

    currency_rates = {
        '$' : 1,
    }

    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount

    def __str__(self):
        return '%s%.2f' % (self.symbol, self.amount)

    def convert(self, other):
        """Convert other amount to our curreny"""
        new_amount = (
            other.amount / self.currency_rates[other.symbol]
            * self.currency_rates[self.symbol])
        return Money(self.symbol, new_amount)

    def __add__(self, other):
        """Add 2 money instances ising '+'"""
        new_amount = self.amount + self.convert(other).amount
        return Money(self.symbol, new_amount)
        


#__str__ in action
soda_cost = Money('$', 5.25)
pizza_cost = Money('$', 7.25)
#print(soda_cost)
#print(pizza_cost)
#__add__ method in action
#print(soda_cost + pizza_cost)

#custom iterators
#making a class iterable with __iter__(), and __next__()

class IterableServer:

    services = [
        {'active': False, 'protocol': 'ftp', 'port': 21},
        {'active': True, 'protocol': 'ssh', 'port': 22},
        {'active': True, 'protocol': 'http', 'port': 80},
    ]
#use a generator instead with yield
    def __iter__(self):
        for service in self.services:
            if service['active']:
                yield service['protocol'], service['port']

for protocol, port in IterableServer():
#    print('service %s on port %d' % (protocol, port))  #loops over all active services


#named tuples
from collection import namedtuple

CacheInfo = namedtuple(
    "CacheInfo", ["hits", "misses", "max_size", "curr_size"])

#giving namedtuples default values

RoutingRule = namedtuple(
    'RoutingRule',
    ['prefix', 'queue_name', 'wait_time'])

default_rule = RoutingRule(None, None, 20)
user_rule = default_rule._replace(
    prefix='user', queue_name='user-queue')










    

    
        


            

    
