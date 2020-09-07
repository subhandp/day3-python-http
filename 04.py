import requests

req= requests.get('https://mul14.github.io/data/employees.json')
json = req.json()

class Employees:
    def __init__(self,json):
        self.data = json

    def salary_map(self, data):
        if ( int(data['salary']) > 15000000): return data['first_name']  + ' ' + data['last_name']

    def location_map(self,data):
        return list(filter(lambda address: address['city'] == 'DKI Jakarta', data['addresses']))

    def birthday_map(self,data):
        return data['first_name']  + ' ' + data['last_name'] if int(data['birthday'].split('-')[1]) == 4 else False

    def department_map(self,data):
        if data['department']['name'] == 'Research and development': return data['first_name']  + ' ' + data['last_name']

    def location_map(self,data):
        return list(filter(lambda address: address['city'] == 'DKI Jakarta', data['addresses']))

    def presences_map(self,data):
        return list(filter(lambda presence: ( int(presence.split('-')[0]) == 2019 and int(presence.split('-')[1]) ==10), data['presence_list']))

    def salary(self):
        return filter(None,map(self.salary_map,self.data))

    def location(self):
        return filter(None,map(self.location_map,self.data))

    def birthday(self):
        return filter(None,map(self.birthday_map,self.data))

    def department(self):
        return filter(None,map(self.department_map,self.data))
    
    def presences(self):
        return filter(None,map(self.presences_map,self.data))


employee = Employees(json)
result = employee.salary()
result = employee.location()  
result = employee.birthday()
result = employee.department()
result = employee.presences()