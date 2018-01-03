

class jsonBase:
    def __init__(self):
        pass

    def isArray(self, param):
        return isinstance(param, list)

    def isObject(self, param):
        return isinstance(param, dict)

    def isFloat(self, param):
        return isinstance(param, float)

    def isInt(self, param):
        return isinstance(param, int)

    def isBool(self, param):
        return isinstance(param, bool)

    def isString(self, param):
        return isinstance(param, str)