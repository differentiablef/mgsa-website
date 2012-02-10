

from base import db, base_app, default_view, current_user, login_required, role_required
from base import call_view
from base.user import User

from modules.articles import articles_mod
from models import Article, Article_Comment

from flask import render_template

# Local imports
@articles_mod.route("/view")
def default():
    arts = Article.query.all()
    return render_template("view_articles.html", articles = arts)

@articles_mod.route("/view/<int:articleid>")
def view_article(articleid):
    art = Article.query.get(articleid)
    if art is None:
        flash("No Such Article", "Error")
        return default()
    
    return render_template("view_article.html", article = art)

@articles_mod.route("/edit")
def update_articles():
    arts = Article.query.all()
    return render_template("update_articles.html", articles = arts)


@articles_mod.route("/add", methods=['POST', 'GET'])
def add_article():
    return render_template("add_article.html")

@articles_mod.route("/edit/<int:articleid>")
def edit_article(articleid):
    return default()

@articles_mod.route("/delete/<int:articleid>")
def delete_article(articleid):
    return default();

@articles_mod.route("/addcomment/<int:articleid>", methods=['POST'])
def add_article_comment(articleid):
    
    return default()
