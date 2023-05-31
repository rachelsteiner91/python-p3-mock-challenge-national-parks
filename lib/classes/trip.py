
class Trip:

    all=[]

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

        # self._visitor = []

        visitor.trips(self)
        visitor.national_parks(national_park)
        national_park.trips(self)
        national_park.visitors(visitor)


    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        from classes.visitor import Visitor
        if isinstance(visitor, Visitor):
            self._visitor.append(visitor)
        else:
            raise Exception("visitor must be type Visitor")
        
    @property
    def national_park(self):
        return self._national_park
    
    @visitor.setter
    def national_park(self, national_park):
        from classes.national_park import NationalPark
        if isinstance(national_park, NationalPark):
            self._national_park.append(national_park)
        else:
            raise Exception("nationalpark must be type NationalPark")
