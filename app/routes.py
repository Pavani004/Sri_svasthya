from flask import Blueprint, render_template, request
from app.forms import HealthForm
from app.models import process_input

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = HealthForm()
    
    if form.validate_on_submit():
        user_input = {
            'age': form.age.data,
            'lifestyle': form.lifestyle.data,
            'medical_history': form.medical_history.data,
            'symptoms': form.symptoms.data
        }
        prediction, cluster_info = process_input(user_input)
        return render_template('result.html', prediction=prediction, cluster_info=cluster_info)
    
    return render_template('index.html', form=form)  # Changed from home.html → index.html
