from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
import random
import time

#etesal kamel bazi
#bastan zarib zooodtar



class APP(MDApp):
    def build(self):
        BUILDER = Builder.load_file("UI.kv")
        return BUILDER
    def WRITE(self,X):
        FILE = open("POINT.txt","w")
        FILE.write(str(X))
    def SHOWMONEY(self, MOT):
        try:
            self.root.ids.Money.text = str(MOT)[:5]
        except:
            self.root.ids.Money.text = str(MOT)
    def on_start(self):
        FILE = open("POINT.txt", 'r')
        self.SCOREMONEY = FILE.read()
        if float(self.SCOREMONEY) <= 0 or self.SCOREMONEY == "":
            self.WRITE("50")
            self.SCOREMONEY = "50"
            self.SHOWMONEY(self.SCOREMONEY)
        else:
            self.SHOWMONEY(self.SCOREMONEY)
    def bet(self,NUMBER,Coefficient):
        if NUMBER == "" or Coefficient == "":
            return None
        else:
            if float(self.SCOREMONEY) <=0:
                self.on_start()
            self.BETED= float(NUMBER)
            self.SCOREMONEY = self.minus()
            self.SHOWMONEY(self.SCOREMONEY)
            self.BETEDcon = 0
            self.MAZRAB = float(Coefficient)
            self.randommaker()
            RANDOMCHOOSERT=random.randrange(len(self.randomlist))
            self.RANDOMNUM = self.randomlist[RANDOMCHOOSERT]
            self.event = Clock.schedule_interval(self.set_label, 0.1)
            self.SCOREMONEY = self.plus()
            print(self.SCOREMONEY)
            self.SHOWMONEY(self.SCOREMONEY)
            self.WRITE(self.SCOREMONEY)
    def randommaker(self):
        self.randomlist=[]
        for i in range(0,51):
            io = random.uniform(0.0,1.0)
            self.randomlist.append(io)
        for i in range(0,76):
            io = random.uniform(0.0,10.0)
            self.randomlist.append(io)
        for i in range(0,16):
            io = random.uniform(0.0,100.0)
            self.randomlist.append(io)
    def set_label(self,dt):
        self.BETEDcon+=0.1
        try:
            self.root.ids.score_label.text = str(self.BETEDcon)[:5]
        except:
            self.root.ids.score_label.text = str(self.BETEDcon)
        if self.BETEDcon >= self.RANDOMNUM:
            self.event.cancel()
    def plus(self):
        return float(self.SCOREMONEY) + self.Coefficient()
    def Coefficient(self):
        if self.RANDOMNUM>= self.MAZRAB:
            return self.MAZRAB*self.BETED
        if self.RANDOMNUM<self.MAZRAB:
            return 0
    def minus(self):
        return float(self.SCOREMONEY) - self.BETED



APP().run()