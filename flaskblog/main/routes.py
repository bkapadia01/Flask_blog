from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.main.forms import ModalForm

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template('home.html', posts=posts)
    
@main.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html', title = 'ABoooT')

@main.route('/modal', methods=['GET', 'POST'])
@login_required
def modal():
    form = ModalForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author= current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post has been created', 'success')
        return redirect(url_for('main.modal'))
    return render_template('modal.html', title = 'modal', form=form, legend='Create Post')

# @main.route('/modal', methods=['GET', 'POST'])
# @login_required
# def modal():
#     form = PostForm()
#     if form.validate_on_submit():
#         post = Post(title=form.title.data, content=form.content.data, author= current_user)
#         db.session.add(post)
#         db.session.commit()
#         flash('Post has been created', 'success')
#         return redirect(url_for('main.home'))
#     return render_template('modal.html', title='ModalPost', form=form, legend='Create Post')



