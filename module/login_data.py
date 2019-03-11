def login_data():
    filename = 'D:\selenium_python\data\\login_data'
    zidian1 = {}
    with open(filename) as f_obj:
        duqu = f_obj.readlines()
        for a in duqu:
            key = a.split('=', 1)[0]
            value = a.split('=', 1)[1]
            zidian1[key] = value
    return zidian1