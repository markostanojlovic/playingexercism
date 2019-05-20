class Luhn(object):
    def __init__(self, card_num):
        self.card = card_num.replace(' ','')[::-1]

    def is_valid(self):
        if not self.card.isdigit() or len(self.card) < 2:
            return False
        luhn = [ (int(num)*2 if int(num)*2 <10 else int(num)*2-9)
        if i % 2 == 1 else int(num) for i, num in enumerate(self.card)]
        return sum(luhn) % 10 == 0
