from payment import Payment
from datetime import date

class Card(Payment):
    card_number = str
    cvv = str
    card_date = date

    def __init__(self, id, card_number, cvv, card_date):
        super().__init__(id)
        self.card_number = card_number
        self.cvv = cvv
        self.card_date = card_date