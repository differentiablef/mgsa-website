# #############################################################################
# Name:  NewsPost 
# Synop: Basic news post model for front-page
#

from base import db
from base.user import User

from datetime import *

class Article(db.Model):
    __tablename__ = 'article'
    id            = db.Column(db.Integer, primary_key=True)
    title         = db.Column(db.String(80))
    css           = db.Column(db.Text)
    body          = db.Column(db.Text)
    javascript_before    = db.Column(db.Text)
    javascript_after    = db.Column(db.Text)
    pub_date      = db.Column(db.DateTime)
    author_id        = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship("User", backref='articles')
    author_blurb = db.Column(db.Text)
    
    def __init__(self, title="", body="", author=0):
        self.title = title
        self.body = body
        self.author_id = author
        self.pub_date = datetime.utcnow()

    def __repr__(self):
        return '%s by %s' % (self.title, self.author.get_display_name())

    def set_javascript_before(self, js):
        self.javascript_before = js

    def set_javascript_after(self, js):
        self.javascript_after = js
    
    def set_stylesheet(self,css):
        self.css = css;
        
    def set_title(self, title):
        self.title = title
    
    def set_body(self, body):
        self.body = body

    def get_display_name(self):
        return User.query.get(self.author_id).get_display_name();
        
    def get_title(self):
        return self.title;
        
    def get_body(self):
        return self.body;

    def get_javascript_after(self):
        return self.javascript_after

    def get_javascript_before(self):
        return self.javascript_before

    def get_stylesheet(self):
        return self.css
        
    def get_pub_date(self):
        return self.pub_date.strftime('%m/%d/20%y %I:%M');

    def get_author_blurb(self):
        return self.author_blurb

class Article_Comment(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    article_id       = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)       # id number of the post this is a comment for
    article          = db.relationship("Article", backref="comments")
    body          = db.Column(db.Text)          # text of the comment
    pub_date      = db.Column(db.DateTime)      # comment date
    author_id     = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)       # id number of author
    author        = db.relationship("User")
    
    user = db.relationship("User", backref='article_comments')
    
    def __init__(self, articleid=0, body=None, pub_date=None):
        
        self.article_id = articleid
        self.body = body
        self.pub_date = datetime.utcnow()
        
    def __repr__(self):
        return '%s by %s' % (self.body, self.author.get_display_name())


    def get_body(self):
        return self.body

    def get_pub_date(self):
        return self.pub_date.strftime('%m/%d/20%y %I:%M');

    def get_display_name(self):
        return self.author.get_display_name();

