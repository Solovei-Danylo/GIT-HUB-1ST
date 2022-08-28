def lookup_key(data, value):
    dict_list = []
    for key in data:
        if data[key] == value:
            dict_list.append(key)
    return dict_list


lookup_key(g2g=2, sss=3)
