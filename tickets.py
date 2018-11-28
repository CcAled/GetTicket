seatsList=['商务座','一等座','二等座','高级软卧','软卧','动卧','硬卧','软座','硬座','无座']

class Tickets():
    def __init__(self):
        super(Tickets, self).__init__()
        self.l_tickets=[]

    class s_ticket(object):
        def __init__(self,from_station,to_station,train_date,train_no,passenger,seat,isStudent):
            self.from_station=from_station
            self.to_station=to_station
            self.train_date=train_date
            self.train_no=train_no
            self.passenger=passenger
            self.seat=seat
            self.isStudent=isStudent

        def getInfo(self):
            t=[]
            t.append(self.from_station)
            t.append(self.to_station)
#            g=[]
#            for i in self.train_date:
#                g.append(str(i))
            t.append("-".join(str(c) for c in self.train_date))
            t.append(self.train_no)
            t.append(self.passenger)
            t.append(seatsList[self.seat-5])
            t.append('否是'[self.isStudent])
            return t

    def addTicket(self,from_station,to_station,train_date,train_no,passenger,seat,isStudent):
        t=self.s_ticket(from_station,to_station,train_date,train_no,passenger,seat,isStudent)
        self.l_tickets.append(t)

    def finishBuyingTicket(self):     #完成抢票
        del self.l_tickets[0]

    def deleteTicket(self,ticket_no):        #删除订单
        del self.l_tickets[ticket_no]
'''
def main():
    lt=Tickets()
    for j in range(4):
        from_station=input("from_station")
        to_station=input("to_station")
        train_date=input("train_date")
        train_no=input("train_no")
        passenger=input("passenger")
        lt.AddTicket(from_station,to_station,train_date,train_no,passenger)
    for i in lt.l_tickets:
        print(i.getInfo())

main()
'''
lot=Tickets()
lot.addTicket('成都','北京',[2018,12,25],'T8','三娃',5,0)
lot.addTicket('天津','北京',[2018,11,30],'Z56','大娃',8,1)
lot.addTicket('昆明','大理',[2019,1,5],'C652','二娃',9,0)


