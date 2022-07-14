class User extends Account {
    public User(String name, String document, String email, String password) {
        super(name, document, email, password);
    }
    void printDataUser() {
        System.out.println("User Document: " + document + " User name: " + name + " Email: " + email + " Password: " + password + " ");
    }
}
