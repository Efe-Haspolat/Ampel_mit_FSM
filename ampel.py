import time
class FsmEfe:
    def __init__(self, ilkRenk="KIRMIZI", ikinciRenk="SARI", sonRenk="YEŞİL", süre1=10, süre2=2, süre3=15):

        self.ilkRenk = ilkRenk
        self.ikinciRenk = ikinciRenk
        self.sonRenk = sonRenk

        self.state_renk = ilkRenk

        self.ilk_renk_süresi = süre1
        self.ikinci_renk_süresi = süre2
        self.son_renk_süresi = süre3

    def trafik_isiklarini_calistir(self):
        if self.state_renk == self.ilkRenk:
            print(self.state_renk)
            time.sleep(self.ilk_renk_süresi)
            self.state_renk = self.ikinciRenk

        if self.state_renk == self.ikinciRenk:
            print(self.state_renk)
            time.sleep(self.ikinci_renk_süresi)
            self.state_renk = self.sonRenk

        if self.state_renk == self.sonRenk:
            print(self.state_renk)
            time.sleep(self.son_renk_süresi)
            self.state_renk = self.ilkRenk