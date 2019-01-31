class Phone(object):
    def __init__(self, phone_number):
        phone_l = [i for i in phone_number if i.isdigit()]
        if len(phone_l) == 11 and phone_l[0] == '1':
            phone_l.pop(0)
        if len(phone_l) == 10 and int(phone_l[0]) in range(2,10) and int(phone_l[3]) in range(2,10):
            self.number = ''.join(phone_l)
            self.area_code = ''.join(phone_l[:3])
            self.subscriber = ''.join(phone_l[3:])
        else:
            raise ValueError('Number not valid')

    def pretty(self):
        return '({}) {}-{}'.format(self.area_code,self.subscriber[:3],self.subscriber[3:])
