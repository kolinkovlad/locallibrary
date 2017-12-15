snow_man = u'Привіт'

# snow_man = 'caf\u00e9'

print(snow_man)
print(type(snow_man), snow_man)
ds = snow_man.encode('utf-8')
print(type(ds), ds)
text1 = ds.decode("utf-8")
print(type(text1), text1)

