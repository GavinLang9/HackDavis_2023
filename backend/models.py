from exts import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.Text(), nullable=True)
    def __repr__(self):
        return f"<User {self.name}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        

class Event(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text())
    time = db.Column(db.DateTime())

    def __repr__(self):
        return f"<Event {self.name}>"      
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, title, description, time):
        self.title = title
        self.description = description
        self.time = time
        