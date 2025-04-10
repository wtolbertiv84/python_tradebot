

import re

i = 0

fname = input('Please input your first name: ').title()

lname = input('Please input your last name: ').title()

gender = input('What is your gender: ')

age = input('What is your age: ')

city = input('What is your city: ').title()
state = input('What is your state: ').upper()
country = input('What is your country: ').title()

fname_validation = re.findall('[0-9]', '[!@#$%^&*()_-+=;:"?.,/<>~`]', fname)
lname_validation = re.findall('[0-9]', '[!@#$%^&*()_-+=;:"?.,/<>~`]', lname) 
gender_validation = re.findall('[0-9]', '[!@#$%^&*()_-+=;:"?.,/<>~`]', gender) 
age_validation = re.findall('[0-9]', '[!@#$%^&*()_-+=;:"?.,/<>~`]', age)
city_validation = re.findall('[0-9]', '[!@#$%^&*()_-+=;:"?.,/<>~`]', city)
state_validation = re.findall('[0-9]', '[!@#$%^&*()_-+=;:"?.,/<>~`]', state)
country_validation = re.findall('[0-9]', '[!@#$%^&*()_-+=;:"?.,/<>~`]', country)

print(fname, lname, gender)

def person(gender):
  if gender.lower() == 'male':
    gender = 'Mr.'
  else: 
    gender.lower() == 'Miss'
  return gender

person(gender)
if str(range(0-9)) not in fname or lname:
  print(f'Pleasure to meet you, {person(gender)} ' f'{lname}.')
else: 
  print('That was not a valid name.\n Please try again!')





    
    
