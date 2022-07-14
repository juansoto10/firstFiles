class User extends Account {
    constructor(name, document, email, password) {
        super(name, document, email, password);
    }

    printDataUser = () => {
        console.log("User name: ", this.name, ", User document: ", this.document, ", Email: ", this.email, ", Password: ", this.password);
    }
}