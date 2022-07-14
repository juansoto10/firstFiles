class Driver extends Account {
    constructor(name, document, email, password) {
        super(name, document, email, password);
    }

    printDataDriver = () => {
        console.log("Driver name: ", this.name, ", Driver document: ", this.document, ", Email: ", this.email, ", Password: ", this.password);
    }
}