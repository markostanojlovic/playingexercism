class Luhn(object):
    def __init__(self, card_num):
        self.stripped = card_num.replace(' ','')
        self.card = list(self.stripped)[::-1]
        self.luhn = []

    def is_valid(self):
        if not self.stripped.isdigit() or len(self.stripped) < 2:
            return False
        for i in range(len(self.card)):
            if i % 2 == 1:
                double = int(self.card[i]) * 2
                self.luhn.append(double if double < 10 else double - 9)
            else:
                self.luhn.append(int(self.card[i]))
        self.sum = sum(self.luhn)
        return self.sum % 10 == 0
