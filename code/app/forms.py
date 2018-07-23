from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LcdForm(FlaskForm):
    lcd_text = StringField('LcdText', validators=[DataRequired()])
    submit = SubmitField('Display')