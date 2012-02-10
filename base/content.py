
from base import db

class Content(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tag = db.Column(db.String(300), unique = True)
    contents = db.Column(db.Text)

    def __repr__(self):
        return "%s" % self.tag

    def set_tag(self, tag):
        self.tag = tag

    def set_contents(self, contents):
        self.contents = contents

    def get_tag(self):
        return self.tag

    def get_contents(self):
        return self.contents
    

