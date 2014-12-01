__author__ = 'Alicia'


class SS:
    class InvalidSocial(ValueError):
        """ Format for a social security number was invalid"""
        pass

    def __init__(self, ss=None):
        if ss is None:
            self.ss = self.getsocial()
        else:
            self.ss = self.getsocial(ss)

    def validatess(self):
        try:
            AAA, GG, SSSS = self.ss.split('-')
            area = int(AAA)
            group = int(GG)
            serial = int(SSSS)
            if len(AAA) == 3 and len(GG) == 2 and len(SSSS) == 4:
                if AAA == '078' and GG == '05' and SSSS == '1120':
                    raise self.InvalidSocial('SS used on TV')
                elif '666' in SSSS:
                    raise self.InvalidSocial('666 was in the last 4 digits')
                elif 1 <= area < 900 and area != 666:
                    if 1 <= group <= 99:
                        if 1 <= serial <= 9999:
                            self.ss = AAA + '-' + GG + '-' + SSSS
                        else:
                            raise self.InvalidSocial('Serial is not in valid range')
                    else:
                        raise self.InvalidSocial('Group is not in valid range')
                else:
                    raise self.InvalidSocial('Area is not in valid range')
            else:
                raise self.InvalidSocial('SS not the correct length or split wrong')
        except ValueError:
            raise self.InvalidSocial('There were letters entered in the social')

    def getsocial(self, ss=None):
        if ss is None:
            self.ss = input("Please enter employees social security number: ").strip()
        else:
            self.ss = ss
        try:
            self.validatess()
            return self.ss
        except self.InvalidSocial:
            print("Invalid social security, please enter it again: \n")
            return self.getsocial()