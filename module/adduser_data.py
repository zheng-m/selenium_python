def adduser():
    filename = 'D:\selenium_python\data\\adduser'
    zidian = {}
    with open(filename) as f_obj:
        duqu = f_obj.readlines()
        for a in duqu:
            key = a.split('=', 1)[0]
            value = a.split('=', 1)[1]
            zidian[key] = value
    return zidian
