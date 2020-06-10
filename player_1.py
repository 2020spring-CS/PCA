
class Player:
    '''
    AVG: 평균자책점 / XBH: 장타 / GO: 땅볼 / AO: 뜬공 / GW_RBI: 결승타 /
    BB/K: 볼넷/삼진 / P/PA: 투구수/타석 / ISOP: 순수장타율 / XR: 추정득점 /
    GPA: (1.8*출루율 + 장타율) / 4

    '''
    def __init__(self, rank, name, team, AVG, XBH, GO, AO, GO_AO, GW_RBI, BB_K, P_PA, ISOP, XR, GPA):
        self.rank = int(rank)
        self.name = name
        self.team = team
        self.AVG = float(AVG)
        self.XBH = int(XBH)
        self.GO = int(GO)
        self.AO = int(AO)
        self.GW_RBI = int(GW_RBI)
        self.BB_K = float(BB_K)
        self.P_PA = float(P_PA)
        self.ISOP = float(ISOP)
        self.XR = float(XR)
        self.GPA = float(GPA)
    
    def __str__(self):
        return str(self.name) + ' of ' + str(self.team)

    def print(self):
        print(self.name)