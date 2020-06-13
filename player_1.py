
class Record_Hitter:
    '''
    AVG: 타율 / XBH: 장타 / GO: 땅볼 / AO: 뜬공 / GW_RBI: 결승타 /
    BB/K: 볼넷/삼진 / P/PA: 투구수/타석 / ISOP: 순수장타율 / XR: 추정득점 /
    GPA: (1.8*출루율 + 장타율) / 4

    '''
    def __init__(self, rank, name, team, AVG, XBH, GO, AO, GO_AO, GW_RBI, BB_K, P_PA, ISOP, XR, GPA, year):
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
        self.year = year
        self.type = 'Hitter'

    def __str__(self):
        return str(self.team) + ' 소속 ' + str(self.name)

    def print(self):
        print(self.rank, self.name, self.team, self.AVG, self.XBH, self.GO, self.AO, self.GW_RBI, self.BB_K, self.P_PA, self.ISOP, self.XR, self.GPA, self.year)


class Record_Pitcher(Record_Hitter):
    '''
    ERA: 평균자책점 / G: 경기 / W: 승리 / L: 패배 / SV: 세이브 / HLD: 홀드 /
    WPCT: 승률 / IP: 이닝 / H: 피안타 / HR: 홈런 / BB: 볼넷 / HBP: 사구 / 
    SO: 삼진 / R: 실점 / ER: 자책점 / WHIP: 이닝당 출루허용률

    '''
    def __init__(self, rank, name, team, ERA, G, W, L, SV, HLD, WPCT, IP, H, HR, BB, HBP, SO, R, ER, WHIP, year):
        self.rank = int(rank)
        self.name = name
        self.team = team
        self.ERA = float(ERA)
        self.G = int(G)
        self.W = int(W)
        self.L = int(L)
        self.SV = int(SV)
        self.HLD = int(HLD)
        self.WPCT = float(WPCT)
        self.IP = float(IP)
        self.H = int(H)
        self.HR = int(HR)
        self.BB = int(BB)
        self.HBP = int(HBP)
        self.SO = int(SO)
        self.R = int(R)
        self.ER = int(ER)
        self.WHIP = float(WHIP)
        self.year = year
        self.type = 'Pitcher'
    


class Player():
    def __init__(self, name, team, type):
        self.name = name
        self.team = team
        self.record = []
        self.type = type

    def update(self, record):
        if record.type == self.type:
            self.record.append(record)
    
    def __str__(self):
        return str(self.team) + ' 소속 ' + str(self.name)    

    def print(self):
        for stat in self.record:
            stat.print()

#test code
#Kim = Player('김현수', 'LG', 'Hitter')
#record = Record_Hitter(1,'김현수','LG',0.362,61,136,102,1.33,8,0.77,3.66,0.227,99.3,0.334, 2018)
#Kim.update(record)
#Kim.record[0].print()

    


