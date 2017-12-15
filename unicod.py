__author__ = 'Ivan'
#
# import unicodedata
#
# def unic_val(val):
#     name=unicodedata.name(val)
#     value=unicodedata.lookup(name)
#     print(val, name, value)
#
# if __name__=="__main__":
#     unic_val('a')
#     unic_val('\u00ff')
#

snow_man = '\u2603'

print(snow_man)

print(type(snow_man))
print(len(snow_man))
ds=snow_man.encode('utf8')
print(snow_man)
print(type(ds),ds)

text1 = ds.decode('utf-8')

print(type(text1),text1)

#ds = snow_man.encode('ascii')<-Error
ds = snow_man.encode('ascii','ignore')
ds = snow_man.encode('ascii','replace')
ds = snow_man.encode('ascii','backslashreplace')
#ds = snow_man.encode/'ascii','xmlcharreplace')

place='caf\u00e9'
print(place)
print(type(place))
place_bytes=place.encode("utf-8")

place2=place_bytes.decode("utf-8")
place2=place_bytes.decode("ascii")
place2=place_bytes.decode("latin-1")
place2=place_bytes.decode("wondows-1251")