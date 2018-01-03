import json
from JsonBase import jsonBase


class jsonReader(jsonBase):
    __fp = ''

    def __init__(self, filename, mode='r+'):
        try:
            super().__init__()
            self.__fp = open(filename, mode)
        except IOError as arg:           
            print("jsonReader", arg)
            self.__fp.close()

    def __del__(self):
        self.__fp.close()

    def getJsonObj(self):
        obj = json.load(self.__fp)
        return (self.isObject(obj) or self.isArray(obj)) and obj or {}

    def getBool(self, obj, param):
        assert (self.isObject(obj))
        assert (self.isBool(obj[param]))
        return obj[param]

    def getInt(self, obj, param):
        assert (self.isObject(obj))
        assert (self.isInt(obj[param]))
        return obj[param]

    def getFloat(self, obj, param):
        assert (self.isObject(obj))
        assert (self.isFloat(obj[param]))
        return obj[param]

    def getString(self, obj, param):
        assert (self.isObject(obj))
        assert (self.isString(obj[param]))
        return obj[param]

    def getSubObj(self, obj, param):
        assert (self.isObject(obj))
        assert (self.isObject(obj[param]))
        return obj[param]
