# Condition Logic
# if condition will executes only if the condition is True
# elif condition checks another condition
# else statement or condition returns the False statement

licensed = input('Enter whether you won license or not if type YES else NO:- ')
user_age = int(input("Enter your age:- "))
if user_age >= 18 and licensed == 'YES' or 'yes':
    print('your are old enough to drive')

elif licensed == 'NO' or 'no' and user_age <= 18:
    print('your are not old enough to get license')

else:
    print('your are not old enough to drive')