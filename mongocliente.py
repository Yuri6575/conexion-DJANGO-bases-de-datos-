from pymongo import Mongocliente

#conectar a MongoDB
cliente = Mongocliente("mongodb://localhost:27017")
db = cliente ["ecommerce3066478"]

#crear colecciones
clientes = db ["clientes12"]
clientes = db ["producto12"]
clientes = db ["ventas12"]
clientes = db ["compras12"]
clientes = db ["comercio12"]

# INSERTE DOCUMENTOS DE EJEMPLO

clientes.insert_one({"nombre": "juan Pérez", "correo": "juan@gmail.com", "telefono": "123456789", "direccion": "calle 12"})
productos.insert_one({"nombre": "laptop", "descripcion": "laptop  de alta gama", "precio": "1200", "sctok": "calle 12"})