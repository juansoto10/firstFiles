<?php
require_once('Account.php');
class Car {
    public $id;
    public $license;
    public $driver;
    protected $passenger;

    public function __construct($license, $driver) {
        $this->license = $license;
        $this->driver = $driver;
    }

    public function printDataCar() {
        // echo "Licencia: $this->license Driver: ".$this->driver->name."<br>";

        echo "
        Licencia: $this->license 
        Driver: {$this->driver->name} 
        Número de pasajeros: $this->passenger
        "."<br>";
    }

    public function getPassenger() {
        return $this->passenger;
    }

    public function setPassenger($passenger) {
        if($passenger == 4) {
            $this->passenger = $passenger;
        }
        else {
            echo "You must assign 4 passengers"."<br>";
        }
    }
}

?>