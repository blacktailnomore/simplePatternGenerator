from JsonReader import jsonReader


class mahjongCard:
    __wan = 0
    __tiao = 0
    __bing = 0
    __dnxb = 0
    __zfb = 0
    __cards = []

    def __init__(self, filename, mode='r+'):
        js = jsonReader(filename, mode)
        obj = js.getJsonObj()
        mask = [v for k, v in obj.items()]
        self.__wan = int(mask[0], 16)
        self.__tiao = int(mask[1], 16)
        self.__bing = int(mask[2], 16)
        self.__dnxb = int(mask[3], 16)
        self.__zfb = int(mask[4], 16)

    def __clearCards(self):
        self.__cards.clear()

    def __funGenerator(self, upper, revalCount, mask):
        a, counter = 0, 1
        while True:
            if counter > upper:
                return
            a = mask + counter
            for x in range(revalCount):
                yield a
            counter += 1

    def generator(self, needZi=True):
        self.__clearCards()
        for x in self.__funGenerator(9, 4, self.__wan):
            self.__cards.append(x)

        for x in self.__funGenerator(9, 4, self.__tiao):
            self.__cards.append(x)

        for x in self.__funGenerator(9, 4, self.__bing):
            self.__cards.append(x)

        if needZi:
            for x in self.__funGenerator(4, 4, self.__dnxb):
                self.__cards.append(x)

            for x in self.__funGenerator(3, 4, self.__zfb):
                self.__cards.append(x)

        return self.__cards

    def getValue(self, card):
        return card & 0xf

    def getColor(self, card):
        return card >> 4

    def isZi(self, card):
        return self.isDNXB(card) or self.isZFB(card)

    def isWan(self, card):
        return card & self.__wan

    def isTiao(self, card):
        return card & self.__tiao

    def isBing(self, card):
        return card & self.__bing

    def isDNXB(self, card):
        return card & self.__dnxb

    def isZFB(self, card):
        return card & self.__zfb


if __name__ == '__main__':
    mc = mahjongCard(r'conf/carddef.json')
    cards = mc.generator()
    print(mc.isZi(cards[0]))
