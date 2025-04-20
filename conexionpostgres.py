#Cuenta:
#mileidybelace@hotmail.com
#Llave:
#3RSB5RF2DWQTL7M7

import pyscop2
conn = pyscopg2.connect(
        host="localhost",
        user="postgres",
        password="1234",
)
print(conn)
print("conexion exitosa")