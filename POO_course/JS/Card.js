class Card extends Payment {
    constructor(id, cardNumber, cvv, cardDate) {
        super(id);
        this.cardNumber = cardNumber;
        this.cvv = cvv;
        this.cardDate = cardDate;
    }
}