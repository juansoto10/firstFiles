class Main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo care agonia");

        // Car car = new Car("QWE567", new Driver("Paulina Vega", "QWE567", "pauvega@pau.com", "sddi234pau"));
        // car.setPassenger(4);
        // car.printDataCar();

        // UberX uberx_1 = new UberX("WSL234", new Driver("Loriki", "123456", "lorikulli@lori.com", "lorikua93AJ"), "Suzuki", "GN125");
        // uberx_1.setPassenger(3);
        // uberx_1.printDataCar();

        // Card card1 = new Card(12345, "2345789", "234", "12-03-2025");
        // System.out.println(card1.cardDate);

        // User user_1 = new User("Paulina Vega", "235490", "pauvega@pau.com", "pauJKl94");

        // user_1.printDataUser();

        // Driver driver_1 = new Driver("Barbara Palvin", "228038", "bpalvin@barbara.com", "palvin175SQ");

        // driver_1.printDataDriver();

        UberVan uberVan1 = new UberVan("MXD234", new Account("Kimmi Raikkonen", "123422", "kimmirai@kkonen.com", "hejJagArKimmi"));

        uberVan1.setPassenger(6);
        uberVan1.printDataCar();
    }
}