
class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    date_joined = db.Column(db.DateTime,default=datetime.utcnow)
    blogs = db.relationship('Blog', backref ='user', passive_deletes=True,lazy = "dynamic")
    comments = db.relationship('Comment', backref ='user' , passive_deletes=True,  lazy ="dynamic")
    