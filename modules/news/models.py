# #############################################################################
# Name:  NewsPost 
# Synop: Basic news post model for front-page
#

from base import db
from base.user import User

from datetime import *

class NewsPost(db.Model):
    __tablename__ = 'news_post'
    id            = db.Column(db.Integer, primary_key=True)
    title         = db.Column(db.String(80))
    body          = db.Column(db.Text)
    pub_date      = db.Column(db.DateTime)
    author        = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        
    user = db.relationship("User", backref='posts')
    
    
    def __init__(self, title=None, body=None, author=0, pub_date=None):
        self.title = title
        self.body = body
        self.author = author
        
        if pub_date is None:
            pub_date = datetime.utcnow()
        
        self.pub_date = pub_date

    def __repr__(self):
        return '%s by %s' % (self.title, self.user.get_display_name())

    def set_title(self, title):
        self.title = title
    
    def set_body(self, body):
        self.body = body

    def add_comment(self):
        return 

    def get_comment(self, commentid):
        return

    def get_display_name(self):
        return User.query.get(self.author).get_display_name();
        
    def get_title(self):
        return self.title;
        
    def get_body(self):
        return self.body;
    
    def get_pub_date(self):
        return self.pub_date.strftime('%m/%d/20%y %I:%M');

class NewsPostComment(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    post_id       = db.Column(db.Integer, db.ForeignKey('news_post.id'), nullable=False)       # id number of the post this is a comment for
    body          = db.Column(db.Text)          # text of the comment
    pub_date      = db.Column(db.DateTime)      # comment date
    author        = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)       # id number of author
    
    user = db.relationship("User", backref='comments')
    post = db.relationship("NewsPost", backref='comments')
    
    def __init__(self, postid=0, body=None, author=0, pub_date=None):
        
        self.post_id = postid
        self.body = body
        self.author = author
        
        if pub_date is None:
            pub_date = datetime.utcnow()
        
        self.pub_date = pub_date

    def __repr__(self):
        return '%s by %s' % (self.body, self.user.get_display_name())


    def get_body(self):
        return self.body

    def get_pub_date(self):
        return self.pub_date.strftime('%m/%d/20%y %I:%M');

    def get_display_name(self):
        return User.query.get(self.author).get_display_name();

