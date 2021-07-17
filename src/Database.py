from datetime import datetime
from . import db


class Users(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    first_name = db.Column(
        db.String(50),
        nullable=False
    )
    last_name = db.Column(
        db.String(50),
        nullable=False
    )
    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.Text,
        nullable=False
    )
    address = db.Column(
        db.String(200),
        nullable=False
    )
    phone_number = db.Column(
        db.Integer,
        nullable=False
    )
    type = db.Column(
        db.String(20),
        nullable=False
    )
    password = db.Column(
        db.String(60),
        nullable=False
    )
    orders = db.relationship('Orders', backref='customer')

    def __repr__(self):
        return f"Users('{self.first_name}','{self.last_name}','{self.email}'," \
               f" '{self.type}', '{self.address}','{self.phone_number}')"


class Stores(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )
    address = db.Column(
        db.String(200),
        nullable=False
    )
    phone_number = db.Column(
        db.Integer,
        nullable=False
    )
    image_file = db.Column(
        db.String(20),
        nullable=False
    )
    registration_date = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    minimum_order = db.Column(
        db.Integer,
        nullable=False
    )
    shipping_price = db.Column(
        db.Integer,
        nullable=False
    )
    cities_of_activity = db.Column(
        db.Text,
        nullable=False
    )
    categories = db.Column(
        db.Text,
        nullable=False
    )
    items = db.relationship('Items', backref='store')
    orders = db.relationship('Orders', backref='store')

    def __repr__(self):
        return f"Store('{self.name}','{self.address}','{self.phone_number}'," \
               f"'{self.image_file}','{self.registration_date}'," \
               f"'{self.minimum_order}','{self.shipping_price}','{self.cities_of_activity}'," \
               f"'{self.categories}','{self.items}')"


class Orders(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    time_order = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    shipping_address = db.Column(
        db.Text,
        nullable=False
    )
    phone_number = db.Column(
        db.Integer,
        nullable=False
    )
    order_details = db.Column(
        db.Text,
        nullable=False
    )
    total_price = db.Column(
        db.Integer,
        nullable=False
    )
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'))
    store_id = db.Column(db.String(60), db.ForeignKey('stores.id'))

    def __repr__(self):
        return f"Orders('{self.time_order}','{self.order_details}'," \
               f"'{self.shipping_address}','{self.phone_number}', '{self.total_price}')"


class Items(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(60),
        nullable=False
    )
    description = db.Column(
        db.Text,
        nullable=False
    )
    image_file = db.Column(
        db.String(60),
        nullable=False
    )
    category = db.Column(
        db.String(30),
        nullable=False
    )
    color = db.Column(
        db.String(20),
        nullable=False
    )
    size = db.Column(
        db.String(20),
        nullable=False
    )
    price = db.Column(
        db.Integer,
        nullable=False
    )
    inventory = db.Column(
        db.String(20),
        nullable=False
    )
    store_id = db.Column(db.String(60), db.ForeignKey('stores.id'))

    def __repr__(self):
        return f"Items('{self.name}', '{self.category}'," \
               f"'{self.size}', '{self.color}', '{self.price}'," \
               f" '{self.image_file}','{self.inventory}', '{self.description}')"
