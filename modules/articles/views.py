

from base import db, base_app, default_view, current_user, login_required, role_required
from base import call_view
from base.user import User

from modules.articles import articles_mod
from models import Article, Article_Comment

from flask import render_template, request, flash

# ##############################################################################
# Name: default
# Synop: main entry point for module
@articles_mod.route("/view")
def default():
    arts = Article.query.order_by('Article.pub_date DESC').all()
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
@role_required('contributor')
def update_articles():
    arts = Article.query.all()
    return render_template("update_articles.html", articles = arts)

# ##############################################################################
# Name: add_article
# Synop: add an article submitted by authenticated user
@articles_mod.route("/add", methods=['POST', 'GET'])
@role_required('contributor')
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
        return default()
    
    return render_template("add_article.html")

# ##############################################################################
# Name: edit_article
# Synop: update the specified article with the changes submitted via POST
@articles_mod.route("/edit/<int:articleid>", methods=['GET', 'POST'])
@role_required('contributor')
def edit_article(articleid):
    art = Article.query.get(articleid)
    if art is None:
        flash("No Such Article", "Error")
        return default()

    if request.method == 'POST':
        if art.author_id == current_user.id or current_user.has_role('admin'):
            art.body = request.form.get("body")
            art.css = request.form.get("css")
            art.javascript_before = request.form.get("javascript_before")
            art.javascript_after = request.form.get("javascript_after")
            art.title = request.form.get("title")
            art.author_blurb = request.form.get("author_blurb")
            base_app.db.session.commit()
            flash("Article Updated", "Success")
            return default()
    
    return render_template("edit_article.html", article = art)

# ##############################################################################
# Name: delete_article
# Synpo: obvious
@articles_mod.route("/delete/<int:articleid>")
@role_required('contributor')
def delete_article(articleid):
    art = Article.query.get(articleid)
    if art is None:
        flash("No Such Article", "Error")
        return default()

    if current_user.id == art.author_id or current_user.has_role('admin'):
        for comment in art.comments:
            base_app.db.session.delete(comment)
        base_app.db.session.delete(art)
        base_app.db.session.commit()
        flash("Article Deleted", "Success")
    
    return default()

# ##############################################################################
# Name: add_article_comment
# Synop: obvious
@articles_mod.route("/addcomment/<int:articleid>", methods=['POST'])
@login_required
def add_article_comment(articleid):
    art = Article.query.get(articleid)
    if art is None:
        flash("No Such Article", "Error")
        return default()

    cmt = Article_Comment()
    cmt.article_id = art.id
    cmt.author_id = current_user.id
    cmt.body = request.form.get("comment-body")

    base_app.db.session.add(cmt)
    base_app.db.session.commit()
    
    return view_article(articleid)
