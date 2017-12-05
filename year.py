year = []
for item in range (1990, 2030-1):
    year.insert(0, item)
print(year[::-1])
year1 = year.copy()
for item_2 in year1[::4]:
    print (item_2)
test_list = year1[::4]
leap_years = []
leap_years.append(test_list)
leap_years = str(leap_years)
print(leap_years)
print("2001" in leap_years)
print("2000" in leap_years)

