from MahjongCard import mahjongCard

if __name__ == '__main__':
    mc = mahjongCard(r'conf/carddef.json')
    cards = mc.generator()
    cards = mc.generator(False)
    print(cards)
    c2 = []
