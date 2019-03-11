def get_url():
    filename = 'D:\selenium_python\data\url'
    with open(filename) as f_obj:
        duqu = f_obj.read()
        return duqu