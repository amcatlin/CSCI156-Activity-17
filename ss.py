__author__ = 'Alicia'

class SS:
    class InvalidSocial(ValueError):
        pass

    def __init__(self, ss):
        self.ss = ss

    def validatess(self):
        try:
            aaa, gg, ssss = self.ss.split('-')
            e, v, i, l = ssss[0:4]
            area = int(aaa)
            group = int(gg)
            serial = int(ssss)
            if len(aaa) == 3 and len(gg) == 2 and len(ssss) == 4:
                if aaa == '078' and gg == '05' and ssss == '1120':
                    raise self.InvalidSocial
                elif (e == '6' and v == '6' and i == '6') or (v == '6' and i == '6' and l == '6'):
                    raise self.InvalidSocial
                elif 1 <= area < 900 and area != 666:
                    if 1 <= group <= 99:
                        if 1 <= serial <= 9999:
                            self.ss = aaa, gg, ssss
                        else:
                            raise self.InvalidSocial
                    else:
                        raise self.InvalidSocial
                else:
                    raise self.InvalidSocial
            else:
                raise self.InvalidSocial
        except ValueError:
            raise self.InvalidSocial

    def getsocial(self):
        self.ss = input("Social: ").strip()
        try:
            self.validatess()
        except self.InvalidSocial:
            print("Invalid SS, please try again\n")
            self.getsocial()

