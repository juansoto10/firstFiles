class Card extends Payment {
    String cardNumber;
    String cvv;
    String cardDate;

    public Card(Integer id, String cardNumber, String cvv, String cardDate) {
        super(id);
        this.cardNumber = cardNumber;
        this.cvv = cvv;
        this.cardDate = cardDate;
    }
}
