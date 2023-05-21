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
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    items = db.Column(db.String())
    start_time = db.Column(db.DateTime(), nullable=True)
    end_time = db.Column(db.DateTime(), nullable=True)
    address = db.Column(db.String(), nullable=False)
    contact = db.Column(db.Integer(), nullable=True)
    notes = db.Column(db.String(), nullable=True)
    website = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return f"<Event {self.name}>"      
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, name, description, items, start_time, end_time, address, contact, notes, website):
        self.name = name
        self.description = description
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
        self.address = address
        self.contact = contact
        self.notes = notes
        self.website = website
        