const MongoClient = require('mongodb').MongoClient;
const uri = "mongodb://localhost:27017"; // Conexión a la base de datos MongoDB

MongoClient.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(client => {
    const db = client.db('myDatabase');
    const collection = db.collection('users');
    
    // Realizar operaciones CRUD
    collection.insertOne({ name: "John Doe", email: "john@example.com" })
      .then(result => {
        console.log("User inserted:", result);
        client.close();
      });
  })
  .catch(error => {
    console.error("Error connecting to MongoDB:", error);
  });
