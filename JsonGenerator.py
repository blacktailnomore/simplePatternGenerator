from JsonBase import jsonBase


class jsonGenerator(jsonBase):
    __fp = ''
    __root = ''

    def __init__(self, filename, mode='w+'):
        try:
            super().__init__()
            self.__fp = open(filename, mode)
        except IOError as arg:
            print("jsonGenerator", arg)
            self.__fp.close()

    def __del__(self):
        self.__fp.close()

    def setRoot(self, obj):
        pass

    def genObj(self, **kv):
        pass


doc = 0
cardobj = dict()
print(doc)

doc = []
print(doc)
