aso 1: Modificar el archivo de configuración (mongod.conf)
Primero, asegúrate de que la autenticación esté habilitada en la configuración del servidor MongoDB. Para esto, debes modificar el archivo mongod.conf.

En el archivo de configuración (mongod.conf), agrega o modifica la siguiente línea:

yaml
Copiar
security:
  authorization: "enabled"
Esto activa la autorización y requiere que los usuarios se autentiquen antes de poder realizar cualquier acción.

Paso 2: Reiniciar MongoDB
Una vez configurado el archivo, reinicia el servidor MongoDB para que los cambios surtan efecto:

bash
Copiar
sudo systemctl restart mongod
Ahora, MongoDB exigirá autenticación para realizar cualquier operación.

2. Crear el primer usuario administrador
Una vez habilitada la autenticación, es necesario crear un usuario administrador, ya que, de lo contrario, no podrás autenticarte ni crear más usuarios. Para crear un usuario administrador:

Paso 1: Conectar a MongoDB sin autenticación
Conéctate a MongoDB sin autenticación (ya que aún no has creado ningún usuario) utilizando el cliente de línea de comandos (mongo):

bash
Copiar
mongo
Paso 2: Acceder a la base de datos de administración
Dentro de MongoDB, accede a la base de datos admin, que es donde crearás el primer usuario administrador:

js
Copiar
use admin
Paso 3: Crear el usuario administrador
Ahora, crea un usuario administrador utilizando el comando db.createUser(). Este usuario tendrá permisos para crear otros usuarios y gestionar la base de datos:

js
Copiar
db.createUser({
  user: "admin",
  pwd: "admin_password",  // Asegúrate de usar una contraseña segura
  roles: [{ role: "root", db: "admin" }]
})
Aquí, el rol root otorga privilegios completos sobre todas las bases de datos y operaciones en MongoDB.

Paso 4: Salir e iniciar sesión con el usuario administrador
Una vez creado el usuario, sal del shell de MongoDB y vuelve a ingresar utilizando el usuario administrador:

bash
Copiar
mongo -u admin -p admin_password --authenticationDatabase admin
3. Crear otros usuarios con roles específicos
Una vez que tienes un usuario administrador, puedes crear otros usuarios con roles específicos según los permisos que desees otorgarles. Los roles en MongoDB definen qué acciones puede realizar un usuario sobre las bases de datos.

Paso 1: Crear un nuevo usuario con rol específico
Por ejemplo, si quieres crear un usuario con acceso solo de lectura a una base de datos específica, puedes hacerlo con el siguiente comando:

js
Copiar
use myDatabase

db.createUser({
  user: "readOnlyUser",
  pwd: "secure_password",
  roles: [{ role: "read", db: "myDatabase" }]
})
El rol read otorga solo permisos de lectura sobre la base de datos myDatabase.

Paso 2: Crear un usuario con permisos de escritura
Si deseas un usuario que pueda insertar, actualizar y eliminar documentos, asigna el rol readWrite:

js
Copiar
use myDatabase

db.createUser({
  user: "readWriteUser",
  pwd: "secure_password",
  roles: [{ role: "readWrite", db: "myDatabase" }]
})
4. Roles predefinidos en MongoDB
MongoDB proporciona varios roles predefinidos que puedes asignar a los usuarios. Algunos de los roles más comunes son:

root: Rol con permisos completos en todas las bases de datos.
read: Permite leer los datos de una base de datos específica.
readWrite: Permite leer y escribir datos en una base de datos.
dbAdmin: Permite administrar las configuraciones y índices de una base de datos.
userAdmin: Permite administrar usuarios y roles dentro de una base de datos.
clusterAdmin: Permite administrar la infraestructura del clúster.
backup: Permite realizar copias de seguridad.
restore: Permite restaurar copias de seguridad.
5. Autenticación de base de datos y base de datos de autenticación
Cuando un usuario se autentica, se especifica la base de datos que contiene los datos de autenticación. Generalmente, se utiliza la base de datos admin para la autenticación, pero puedes usar una base de datos específica para almacenar los usuarios (si se necesita).

Ejemplo de autenticación contra la base de datos admin:

bash
Copiar
mongo -u myUser -p myPassword --authenticationDatabase admin
6. Autorización: Control de acceso mediante roles
La autorización se refiere a las acciones que un usuario puede realizar una vez autenticado. MongoDB utiliza autorización basada en roles (RBAC), lo que significa que puedes asignar permisos a los usuarios según el rol que se les haya asignado.

Cada rol tiene permisos específicos, y puedes crear roles personalizados si es necesario. Por ejemplo, un rol personalizado podría permitir a un usuario realizar solo ciertas operaciones sobre un conjunto limitado de colecciones.

Crear un rol personalizado
Si necesitas un rol personalizado, puedes definirlo con un conjunto específico de permisos:

js
Copiar
db.createRole({
  role: "customRole",
  privileges: [
    {
      resource: { db: "myDatabase", collection: "myCollection" },
      actions: ["find", "update"]
    }
  ],
  roles: []
})
Luego, puedes asignar este rol a un usuario:

js
Copiar
use myDatabase

db.createUser({
  user: "customUser",
  pwd: "secure_password",
  roles: [{ role: "customRole", db: "myDatabase" }]
})
7. Deshabilitar la autenticación en producción
Es importante recordar que nunca dejes MongoDB sin autenticación habilitada en producción. La autenticación es una medida crítica para proteger los datos de accesos no autorizados.

8. Auditoría (opcional)
MongoDB también permite habilitar auditoría para registrar las actividades de los usuarios. Esto puede ser útil para revisar los accesos y acciones que los usuarios han realizado sobre la base de datos. La auditoría puede habilitarse configurando parámetros en el archivo mongod.conf:

yaml
Copiar
security:
  auditLog:
    destination: file
    path: /var/log/mongodb/audit.log