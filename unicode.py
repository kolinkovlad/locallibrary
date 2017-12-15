import unicodedata


def unic_val(val):
    name = unicodedata.name(val)
    value = unicodedata.lookup(name)
    print("val=", val, "name=", name, "value2=", value)


if __name__ == "__main__":
    unic_val('a')
    unic_val('\u00ff')