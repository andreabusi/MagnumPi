from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class LcdForm(FlaskForm):
    lcd_text = StringField('LcdText', validators=[DataRequired()])
    submit = SubmitField('Display')


class GenericCPIOForm(FlaskForm):
    pin = IntegerField('pin', validators=[DataRequired()])
    value = StringField('value', validators=[DataRequired()])


class LedForm(FlaskForm):
    pin = IntegerField('PIN', validators=[DataRequired()])
    repetitions = IntegerField('Repetitions', validators=[DataRequired()])
    submit = SubmitField('Blink!')
