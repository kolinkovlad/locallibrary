
year2 = [year2 + 1 for year2 in range(1989, 2017)]
print(year2)

leap_years2 = [leap_years2 for leap_years2 in year2
               if leap_years2 % 4 == 0 and leap_years2 % 100 != 0
               or leap_years2 % 400 == 0]
print(leap_years2)

a = int(input('Введіть номер року >>>> '))
if a in leap_years2:
    print(a, ' - ', 'Рік є високосним')
else:
    print(a, ' - ', 'Рік не є високосним')


