<?php

require_once('Car.php');
require_once('uberX.php');
require_once('Account.php');
require_once('Payment.php');
require_once('card.php');
require_once('user.php');
require_once('driver.php');
require_once('uberVan.php');

//Objeto Car
// $car = new Car("AEF456", new Account("Joao Soteiro", "122890"));
// $car->passenger = 4;
// $car->printDataCar();

// $uberx = new UberX("QWE478", new Account("Luisillo Gordillo", "SSL989"), "Renault", "Duster");
// $uberx->printDataCar();

// $card_1 = new Card(12345, "3456789", "345", "12-05-2025");
// $card_1->printDataCard();

$user = new User("Juan Soto", "1189773", "jsoto@soto.com", "del 234JJJarroz");
$user->printDataUser();

$driver = new Driver("Sharapova", "1144908", "shara@pova.com", "maduroMelaCh");
$driver->printDataDriver();

$uberVan = new UberVan("OJL395", new Driver("Carlo Ancelotti", "122333", "carlo@ancelotti.com", "ganamosLa14"), "BMW", "L12");

$uberVan->setPassenger(6);
$uberVan->printDataCar();

$uberX = new UberX("AMD234", new Driver("Di Maria", "893894", "eldimaria@fideo.com", "sdkj2222"), "Mercedes", "AMG");

$uberX->setPassenger(4);
$uberX->printDataCar();

?>