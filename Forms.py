from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, ValidationError


class PredictForm(FlaskForm):
    # email = StringField('Email', validators=[DataRequired(), Email()])
    # password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=8)])
    rm = StringField('Nombre moyen de pièces par logement')
    lstat = StringField('Statut inférieur de la population (en %)')
    ptratio = StringField('Ratio élèves/enseignant par commune')
    sentence = TextAreaField('Your Review', validators=[DataRequired()])

    submit = SubmitField("Predict")


    def validate_email(self, email):
        if email.data == 'root@domaine.com':
            raise ValidationError('Cet email est déjà enregisteré !')