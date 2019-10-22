from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError


class ModalForm(FlaskForm):
    title = StringField('Recipient:', validators=[DataRequired()])
    content = TextAreaField('Message:', validators=[DataRequired()])
    submit = SubmitField('Submit')
