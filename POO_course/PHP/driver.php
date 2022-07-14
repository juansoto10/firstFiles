<?php
require_once('Account.php');

class Driver extends Account {
    public function __construct($name, $document, $email, $password) {
        parent::__construct($name, $document, $email, $password);
    }

    public function printDataDriver() {
        echo "Driver name: $this->name, Driver document: ".$this->document.", Email: ".$this->email.", Password: ".$this->password."<br>";
    }
}