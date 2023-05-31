class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []
        

       
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance (name, str) and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception("Name should not change after NationaPark is created")


    def trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        else:
            raise Exception("must be of type Trip")
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if isinstance(new_visitor, Visitor):
            self.visitors.append(new_visitor)
        else:
            raise Exception("must of type Visitor")
    
    def total_visits(self):
        pass
    
    def best_visitor(self):
        pass