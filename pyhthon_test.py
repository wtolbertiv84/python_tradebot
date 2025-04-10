

#import re

i = 0

fname = input('Please input your first name: ')

lname = input('Please input your last name: ')

gender = input('What is your gender: ')

#y = re.search('[0-9]', x)

#z = re.findall(x, re.ASCII)
print(fname, lname, gender)

def person(gender):
  if gender.lower() == 'male':
    gender = 'Mr.'
  else: 
    gender.lower() == 'Miss'
  return gender

person(gender)
if str(range(0-9)) not in fname or lname:
  print(f'Pleasure to meet you, {person(gender)} ' f'{lname.title()}.')
else: 
  print('That was not a valid name.\n Please try again!')






    
    
