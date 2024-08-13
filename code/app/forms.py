from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class LcdForm(FlaskForm):
    lcd_text = StringField('LcdText', validators=[DataRequired()])
    submit = SubmitField('Display')


class LcdRowForm(FlaskForm):
    lcd_text = StringField('LcdText', validators=[DataRequired()])
    lcd_row = IntegerField('LcdRow', validators=[DataRequired()])
    submit = SubmitField('Display')


class GenericCPIOForm(FlaskForm):
    pin = IntegerField('pin', validators=[DataRequired()])
    value = StringField('value', validators=[DataRequired()])


class LedForm(FlaskForm):
    pin = IntegerField('PIN', validators=[DataRequired()])
    repetitions = IntegerField('Repetitions', validators=[DataRequired()])
    sleep_time = IntegerField('Sleep time', validators=[DataRequired()], default=1000)
    submit = SubmitField('Blink!')
