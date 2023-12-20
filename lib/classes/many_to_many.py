import re

class NationalPark:
    def __init__(self, name):
        self._name = name
        self._trips = []

    @property
    def name(self):
        return self._name

    def trips(self):
        return self._trips

    def visitors(self):
        return list(set(trip.visitor for trip in self._trips))

    def total_visits(self):
        return len(self._trips)

    def best_visitor(self):
        if not self._trips:
            return None
        visitor_counts = {}
        for trip in self._trips:
            if trip.visitor in visitor_counts:
                visitor_counts[trip.visitor] += 1
            else:
                visitor_counts[trip.visitor] = 1
        return max(visitor_counts, key=visitor_counts.get)

class Visitor:
    def __init__(self, name):
        self._name = name
        self._trips = []

    @property
    def name(self):
        return self._name

    def trips(self):
        return self._trips

    def national_parks(self):
        return list(set(trip.national_park for trip in self._trips))

    def total_visits(self):
        return len(self._trips)

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value

class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self._start_date = start_date
        self._end_date = end_date
        self.national_park._trips.append(self)
        self.visitor._trips.append(self)
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if isinstance(value, str) and re.match(r"^[A-Za-z]+\s\d{1,2}(st|nd|rd|th)$", value):
            self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if isinstance(value, str) and re.match(r"^[A-Za-z]+\s\d{1,2}(st|nd|rd|th)$", value):
            self._end_date = value