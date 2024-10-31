from flask import Blueprint, render_template, request, redirect, url_for, session
from .storage import ArticleStorage

bp = Blueprint('blog', __name__)
storage = ArticleStorage()

@bp.route('/home')
def index():
    articles = storage.get_articles()
    return render_template('index.html', articles=articles)

@bp.route('/article/<id>')
def article(id):
    article = storage.get_article(id)
    return render_template('article.html', article=article)

@bp.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    articles = storage.get_articles()
    return render_template('dashboard.html', articles=articles)

@bp.route('/add', methods=('GET', 'POST'))
def add_article():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        storage.save_article(title, content)
        return redirect(url_for('blog.dashboard'))

    return render_template('add_article.html')

@bp.route('/edit/<id>', methods=('GET', 'POST'))
def edit_article(id):
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    article = storage.get_article(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        storage.save_article(title, content, id)  # Update existing article
        return redirect(url_for('blog.dashboard'))

    return render_template('edit_article.html', article=article)

@bp.route('/delete/<id>', methods=('POST',))
def delete_article(id):
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    storage.delete_article(id)
    return redirect(url_for('blog.dashboard'))