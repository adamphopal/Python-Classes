#Python tricks: Using magic (dunder) functions to create list-like objects
#Specifically, I will demonstrate __len__(), __contains__(), and __getitem__().

class ASAPMob:

    def __init__(self):

        self._members = [
            'A$AP Ferg',
            'A$AP Rocky',
            'A$AP Nast',
            'A$AP Bari',
            'A$AP Lotto'
        ]

    def __len__(self):
        
        return len(self._members)

    def __getitem__(self, key):

        if isinstance(key, int):
            return self._members.pop(key)
        raise TypeError('Cannot get key %s' % key)

    def __contains__(self, member):

        return member in self._members

    def __iter__(self):

        while self._members:
            yield self._members.pop()

asap_mob = ASAPMob()
print('There are %d members in asap mob' % len(asap_mob))
for member in asap_mob:
    print(member)
print('There are now only %d mebers' % len(asap_mob))


            
            
            
            
