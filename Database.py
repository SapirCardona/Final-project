from datetime import datetime
from __init__ import db


class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(60),
        nullable=False
    )
    orders = db.relationship(
        'Orders',
        backref='buyer',
        lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"


class Store(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    storename = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )
    address = db.Column(
        db.String(200),
        nullable=False
    )
    phonenumber = db.Column(
        db.Integer(),
        nullable=False
    )
    imagefile = db.Column(
        db.String(20),
        nullable=False
    )
    orders = db.relationship(
        'Orders',
        backref='orders',
        lazy=True
    )

    def __repr__(self):
        return f"Store('{self.storename}','{self.address}','{self.phonenumber}','{self.imagefile}')"


class Orders(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    dateorder = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    userid = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )
    storeid = db.Column(
        db.String,
        db.ForeignKey('store.id'),
        nullable=False
    )

    def __repr__(self):
        return f"Orders('{self.dateorder}','{self.userid}','{self.storeid}')"
