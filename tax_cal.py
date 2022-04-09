class cal:
    Jointincome = 0
    deduction_max = 18000
    deduction_min = 7100*12
    basicallow = 132000
    standardratezoneself=2022000
    standardratezonemarried=3144000
    joint = 0
    rate1 = 0.02
    rate2 = 0.06
    rate3 = 0.10
    rate4 = 0.14
    rate5 = 0.17
    def mpfdeduct_cal(self,total_income):
        if total_income <= self.deduction_max:
            mpfdeduct = 0
        elif total_income*0.05 >= self.deduction_max:
            mpfdeduct = self.deduction_max
        else:
            mpfdeduct = total_income*0.05
        return mpfdeduct

    def basicdeduct_cal(self,netcharge,standardratezone,basicallow):
        if netcharge > standardratezone:
            basic_deduct = 0
        elif netcharge > basicallow:
            basic_deduct = basicallow
        elif netcharge - basicallow <= 0:
            basic_deduct = netcharge
        return basic_deduct

    def dummy_basicdeduct_cal(self,netcharge):
        if netcharge > self.basicallow:
            basic_deduct = self.basicallow
        elif netcharge - self.basicallow <= 0:
            basic_deduct = netcharge
        return basic_deduct

    def noraml_tax_payable(self,chargeable):
        if chargeable in range(0, 50000):
            Tax = chargeable * self.rate1
        elif chargeable in range(50001, 100000):
            Tax = 50000 * self.rate1 + (chargeable - 50000) * self.rate2
        elif chargeable in range(100001, 150000):
            Tax = 50000 * self.rate1 + 50000 * self.rate2 + (chargeable - 100000) * self.rate3
        elif chargeable in range(150001, 200000):
            Tax = 50000 * self.rate1 + 50000 * self.rate2 + 50000 * self.rate3 + (chargeable - 150000) * self.rate4
        else:
            Tax = 50000 * self.rate1 + 50000 * self.rate2 + 50000 * self.rate3 + 50000 * self.rate4 + (chargeable - 200000) * self.rate5
        return Tax

    def standardrate_tax_payable(self,chargeable):
        Tax = chargeable * 0.15
        return Tax

    def smallest_payable(self,chargeable,standardrate):
        if chargeable == 0:
            return 0,"",0
        else :
            normal_pay = self.noraml_tax_payable(chargeable)
            dummydeduct = self.dummy_basicdeduct_cal(chargeable)
            if chargeable >= standardrate:
                standard_pay = self.standardrate_tax_payable(chargeable)
            else:
                standard_pay = normal_pay + 1
            if standard_pay <= normal_pay:
                return standard_pay, "* standard rate used", dummydeduct
            elif standard_pay > normal_pay:
                return normal_pay, "", dummydeduct


    def better(self, jointtax, Mtax, Ftax):
        if jointtax > Mtax + Ftax:
            return "Separated Assessment is recommended"
        elif jointtax < Mtax + Ftax:
            return "Joint Tax Assessment is recommended"
        else:
            return "Both Tax Assessment are same"

    def single(self,totalincome):
        if isinstance(totalincome,str):
            raise Exception("The year income should be number")
        if totalincome < 0:
            raise Exception("The year income should not less than 0")
        mpfdeduct = self.mpfdeduct_cal(totalincome)
        basicdeduct = self.basicdeduct_cal(totalincome - self.mpfdeduct_cal(totalincome),self.standardratezoneself,self.basicallow)
        netcharge = totalincome - mpfdeduct - basicdeduct
        if self.basicdeduct_cal(totalincome - self.mpfdeduct_cal(totalincome),self.standardratezoneself,self.basicallow) == totalincome:
            basicdeduct = 0
        taxtopay = self.smallest_payable(netcharge,self.standardratezoneself)
        if basicdeduct == 0:
            basicdeduct = taxtopay[2]
        return (totalincome, mpfdeduct, basicdeduct, netcharge, taxtopay[0], taxtopay[1])

    def joint(self,Mtotalincome, Ftotalincome):
        if isinstance(Mtotalincome,str) or isinstance(Ftotalincome,str):
            raise Exception("The year income should be number")
        if Mtotalincome < 0 or Ftotalincome < 0:
            raise Exception("The year income should not less than 0")
        Jointincome = Mtotalincome + Ftotalincome
        mpfdeduct = self.mpfdeduct_cal(Ftotalincome) + self.mpfdeduct_cal(Mtotalincome)
        marragededuct = self.basicdeduct_cal(Jointincome - mpfdeduct,self.standardratezonemarried,self.basicallow * 2)
        netcharge = Jointincome - mpfdeduct - marragededuct
        if self.basicdeduct_cal(Jointincome - mpfdeduct,self.standardratezonemarried,self.basicallow * 2)  >= Jointincome:
            marragededuct = 0
        if netcharge <0:
            netcharge=0
        taxtopay = self.smallest_payable(netcharge,self.standardratezonemarried)
        if marragededuct == 0:
            marragededuct = taxtopay[2]
        return (Jointincome, mpfdeduct, marragededuct, netcharge, taxtopay[0], taxtopay[1])


calj=cal()
Mtotalincome=100000
Ftotalincome=500000
print(calj.single(Mtotalincome))
print(calj.single(Ftotalincome))
print(calj.joint(Mtotalincome, Ftotalincome))
