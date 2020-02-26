class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(50))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User name:%r>' % self.username


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','username','email')