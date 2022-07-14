<?php
require_once('Payment.php');

class Card extends Payment {
    public $card_number;
    public $cvv;
    public $card_date;

    public function __construct($id, $card_number, $cvv, $card_date) {
        parent::__construct($id);
        $this->card_number = $card_number;
        $this->cvv = $cvv;
        $this->card_date = $card_date;
    }

    public function printDataCard() {
        echo "Card number: $this->card_number Card Date: ".$this->card_date." ";
    }
}