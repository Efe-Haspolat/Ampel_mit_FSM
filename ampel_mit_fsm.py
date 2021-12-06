from ampel import FsmEfe
import time

class AmpelFsm(FsmEfe):
    pass


ampel = FsmEfe("ROT", "GELB", "GRÜN", 10, 2, 10)
ampel2 = FsmEfe()

ampel.trafik_isiklarini_calistir()
ampel2.trafik_isiklarini_calistir()

while True:
    ampel.trafik_isiklarini_calistir() # girilen argümanlara göre renk ve süreler ile oluşacak
    print("")
    ampel2.trafik_isiklarini_calistir() # varsayılan değerler kullanılacak