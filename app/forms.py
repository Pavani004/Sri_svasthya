from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, NumberRange

class HealthForm(FlaskForm):
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=1, message="Age must be a positive number")])
    
    lifestyle = SelectField('Lifestyle', choices=[
        ('active', 'Active'),
        ('moderate', 'Moderate'),
        ('sedentary', 'Sedentary')
    ], validators=[DataRequired()])
    
    medical_history = TextAreaField('Medical History (e.g., diabetes, hypertension)', validators=[DataRequired()])
    
    symptoms = TextAreaField('Symptoms', validators=[DataRequired()])
    
    submit = SubmitField('Submit')
