

from base import db, base_app, default_view, current_user, login_required, role_required
from base import call_view
from base.user import User

from modules.articles import articles_mod
from models import Article, Article_Comment

from flask import render_template

# ##############################################################################
# Name: default
# Synop: main entry point for module
@articles_mod.route("/view")
def default():
    arts = Article.query.all()
    return render_template("view_articles.html", articles = arts)

# ##############################################################################
# Name: view_article
# Synop: Display a particular article
@articles_mod.route("/view/<int:articleid>")
def view_article(articleid):
    art = Article.query.get(articleid)
    if art is None:
        flash("No Such Article", "Error")
        return default()
    
    return render_template("view_article.html", article = art)

# ##############################################################################
# Name: update_articles
# Synop: display a list of articles suitable for admin purposes
@articles_mod.route("/edit")
def update_articles():
    arts = Article.query.all()
    return render_template("update_articles.html", articles = arts)

# ##############################################################################
# Name: add_article
# Synop: add an article submitted by authenticated user
@articles_mod.route("/add", methods=['POST', 'GET'])
def add_article():
    if request.method == 'POST':
        art = Article()
        art.author_id = current_user.id
        art.body = request.form.get("body")
        art.css = request.form.get("css")
        art.javascript_before = request.form.get("javascript_before")
        art.javascript_after = request.form.get("javascript_after")
        art.title = request.form.get("title")
        art.author_blurb = request.form.get("author_blurb")
        
        base_app.db.session.add(art)
        base_app.db.session.commit()
    
    return render_template("add_article.html")

# ##############################################################################
# Name: edit_article
# Synop: update the specified article with the changes submitted via POST
@articles_mod.route("/edit/<int:articleid>")
def edit_article(articleid):
    return default()

# ##############################################################################
# Name: delete_article
# Synpo: obvious
@articles_mod.route("/delete/<int:articleid>")
def delete_article(articleid):
    return default();

# ##############################################################################
# Name: add_article_comment
# Synop: obvious
@articles_mod.route("/addcomment/<int:articleid>", methods=['POST'])
def add_article_comment(articleid):
    return default()
