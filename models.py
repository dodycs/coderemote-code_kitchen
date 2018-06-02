from sqlalchemy.orm import relationship, backref, joinedload
from sqlalchemy import Column, DateTime, String, Integer, Float, ForeignKey, func

from base import Base, inverse_relationship, create_tables

# DATA MODELING
class Club(Base):
   __tablename__ = 'club'
   id = Column(Integer, primary_key=True)
   name = Column(String)
   url = Column(String)

   def parse_json(self, data):
      # self.id = data['id']
      self.name = data['name']
      self.url = data['api']
      # self.league = data['league']
      # self.city = data['city']

# class Address(Base):
#    __tablename__ = 'address'
#    id = Column(Integer, primary_key=True)
#    zip = Column(String)
#    city = Column(String)
#    street = Column(String)

#    def __init__(self, data):
#       self.zip = data['zip']
#       self.city = data['city']
#       self.street = data['street']

# class Person(Base):
#    __table__ = 'person'
#    id = Column(Integer, primary_key=True)
#    first = Column(String)
#    last = Column(String)
#    gender = Column(String)
#    url = Column(String, unique=True)

#    def parse_json(self, data):
#       self.id = data['id']
#       self.first = data['first']
#       self.last = data['last']
#       self.gender = data['gender']
#       self.url = data['api']

#       self.current_address = Address(data['current_address'])

#       self.past_address = []
#       for data in data['pass_address']:
#          self.past_address.append(Address(data))

#       cur_membership_obj = get_object(data['current_membership'])
#       self.current_membership = Club(cur_membership_obj)

#       self.past_membership = []
#       for past_membership_url in data['past_membership']:
#          past_membership = Club(get_object(past_membership_url))
#          self.past_membership.append(past_membership)

#       self.employment_history = []
#       for employment_history_url in data['employment_history']:
#          employment_history = Club(get_object(employment_history_url))
#          self.employment_history.append(employment_history)

# class Department():
#    def parse_json(self, data):
#       self.id = data['id']
#       self.name = data['name']
#       self.api = data['api']

#       company_obj = get_object(data['company'])
#       self.company = Company(company_obj)

# class League():
#    def parse_json(self, data):
#       self.id = data['id']
#       self.name = data['name']
#       self.sport = data['sport']
#       self.api = data['api']

#       self.clubs = []
#       for club_url in data['clubs']:
#          club = Club(get_object(club))
#          self.clubs.append(club)

# class Company():
#    def parse_json(self, data):
#       self.id = data['id']
#       self.name = data['name']
#       self.total_assets = data['total_assets']
#       self.industry = data['industry']
#       self.founded_on = data['founded_on']
#       self.symbol = data['symbol']
#       self.revenue = data['revenue']
#       self.net_income = data['net_income']
#       self.operating_income = data['operating_income']
#       self.api = data['api']

#       self.departments = []
#       for department_url in data['departments']:
#          department = Department(get_object(department_url))
#          self.departments.append(department)

#       exchange_obj = get_object(data['exchange'])
#       self.exchange = Exchange(exchange_obj)

# class State():
#    def __init__(self, data):
#       self.id = data['id']
#       self.name = data['name']
#       self.abbreviation = data['abbreviation']
#       self.gdp = data['gdp']
#       self.api = data['api']

#       # self.cities = []
#       # for city_url in data['cities']:
#       #    city = City(get_object(city_url))
#       #    self.cities.append(city)

# class Exchange():
#    def parse_json(self, data):
#       self.id = data['id']
#       self.name = data['name']
#       self.address = data['address']
#       self.api = data['api']

#       city_obj = get_object(data['city'])
#       self.city = City(city_obj)

#    def parse_jsons(self, data):
#       self.id = data['id']
#       self.name = data['name']
#       self.address = data['address']
#       self.api = data['api']

#       city_obj = get_object(api_root.format('city', data['city']))
#       self.city = City(city_obj)

# class City():
#    def parse_json(self, data):
#       self.id = data['id']
#       self.name = data['name']
#       self.population = data['population']
#       self.zipcode = data['zipcode']
#       self.is_capital = data['is_capital']
#       self.api = data['api']

#       state_obj = get_object(data['state'])
#       self.state = State(state_obj)

#    def parse_jsons(self, data):
#       self.id = data['id']
#       self.name = data['name']
#       self.population = data['population']
#       self.zipcode = data['zipcode']
#       self.is_capital = data['is_capital']
#       self.api = data['api']

#       state_obj = get_object(api_root.format('state', data['state']))
#       self.state = State(state_obj)



# # ADD MODELS 




if __name__ is not '__main__':
    create_tables()
