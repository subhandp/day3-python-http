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

    def salary(self):
        return filter(None,map(self.salary_map,self.data))

    def location(self):
        return filter(None,map(self.location_map,self.data))

    def birthday(self):
        return filter(None,map(self.birthday_map,self.data))

    def department(self):
        return filter(None,map(self.department_map,self.data))


employee = Employees(json)
result = employee.salary()
result = employee.location()
result = employee.birthday()
result = employee.department()



print(list(result))

# import requests



# r = requests.get('https://mul14.github.io/data/employees.json')
# r_json = r.json()
# sep = ', '


# def find_salary(value):
#     if (int(value['salary']) > 15000000): return value['first_name']


# def find_location(value):
#     # def locations(val): return val['city']
#     # location = list(map(locations, value['addresses']['city']))
#     # print(value['addresses'])
#     return list(filter(lambda address: address['city'] == 'DKI Jakarta', value['addresses']))
#     # if 'DKI Jakarta' in value['addresses']['city']: return value['first_name']


# def find_birthday(value):
#     april = int(value['birthday'].split('-')[1]) == 4
#     return value['first_name'] if april else False


# def find_dept(value):
#     if value['department']['name'] == 'Research and development':
#         return value['first_name']


# def find_absences(value):
#     def count(val): return int(val.split('-')[1]) == 10 and int(val.split('-')[0]) == 2019
#     oktober = filter(count,value['presence_list'])
#     return {"name":value['first_name'],"absent":len(list(oktober))}


# employee_location = filter(None,map(find_location, r_json))
# print(list(employee_location))
# employee_salary = filter(None,map(find_salary, r_json))
# employee_birthday = filter(None,map(find_birthday, r_json))
# employee_dept = filter(None,map(find_dept, r_json))
# employee_absences = filter(None,map(find_absences, r_json))

# # print(r_json)