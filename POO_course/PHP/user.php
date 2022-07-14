<?php
require_once('Account.php');

class User extends Account {
    public function __construct($name, $document, $email, $password) {
        parent::__construct($name, $document, $email, $password);
    }

    public function printDataUser() {
        echo "User name: $this->name, User document: ".$this->document.", Email: ".$this->email.", Password: ".$this->password."<br>";
    }
}