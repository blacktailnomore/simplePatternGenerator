from JsonBase import jsonBase
import json

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
        if self.isObject(obj):
            self.__root = {}
        elif self.isArray(obj):
            self.__root = []
        else:
            raise ValueError("not array or object",obj)

    def dump(self):
        json.dumps(self.__root)

    def getRoot(self):
        return self.__root

    def genObj(self, obj, **kv):
        pass

    def genArray(self, obj, *kv):
        pass

    def addObj(self, obj, **kv):
        pass

    def addArray(self, obj, *kv):
        pass

if __name__ == '__main__':
    doc = {
        'hands': [], 
        'chi': [],
        'peng':[],
        'ZiMo':False,  
        'GangShangKaiHua':False,
        'QiangGang':False,
        'MiaoShouHuiChun':False,
        'HeJueZhang':False,
        'HuaFan':0,
        'ExceptedRes':{}
        }

    jg = jsonGenerator(r'Res/dump.json')
    jg.setRoot([])
    root = jg.getRoot()
    root.append(doc)
    print(root)
    root = jg.getRoot()
    print(root)

