from app import database

# crea las tablas flask db init
# crea las migraciones flask db migrate
# actualiza la base de datos con la tabla
class Agente(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String(250))
    apellido = database.Column(database.String(250))
    email = database.Column(database.String(250))

    def __str__(self):
        return (
            f"""
            id: {self.id}\n
            nombre: {self.nombre}\n
            apellido: {self.apellido}\n
            email: {self.email}
            """
        )


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    def __repr__(self):
        return '<User %r>' % self.username