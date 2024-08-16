from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class LcdForm(FlaskForm):
    lcd_text = StringField('LcdText', validators=[DataRequired()])
    lcd_new_line = BooleanField('LcdNewLine', default=True)
    submit = SubmitField('Display')


class LcdRowForm(FlaskForm):
    lcd_text_1 = StringField('LcdText1', validators=[DataRequired()])
    lcd_text_2 = StringField('LcdText2', validators=[DataRequired()])
    lcd_text_3 = StringField('LcdText3', validators=[DataRequired()])
    lcd_text_4 = StringField('LcdText4', validators=[DataRequired()])
    submit = SubmitField('Display')


class GenericCPIOForm(FlaskForm):
    pin = IntegerField('pin', validators=[DataRequired()])
    value = StringField('value', validators=[DataRequired()])


class LedForm(FlaskForm):
    pin = IntegerField('PIN', validators=[DataRequired()])
    repetitions = IntegerField('Repetitions', validators=[DataRequired()])
    sleep_time = IntegerField('Sleep time', validators=[DataRequired()], default=1000)
    submit = SubmitField('Blink!')
