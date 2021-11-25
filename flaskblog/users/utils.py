from flask import url_for, current_app
from secrets import token_hex
from os.path import splitext, join
from PIL.Image import open
from flaskblog import mail
from flask_mail import Message


def save_picture(form_picture):
    random_hex = token_hex(8)
    _, f_ext = splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = join(current_app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''
    To reset your password, visit the fallowing link: {url_for('reset_token', token=token, _external=True)}
    If you did not make this request then simply ignore this email and no changes will be made 
    '''
    mail.send(msg)
