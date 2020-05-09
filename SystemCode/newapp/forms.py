from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row

cp = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
]

major_vessels = [
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
]


thal = [
    (3, 'normal'),
    (6, 'fixed defect'),
    (7, 'reversable defect'),
]

gender = [
    (0, 'Male'),
    (1, 'Female'),
]

fbs = [
    (0, 'No'),
    (1, 'Yes'),
]

restecg = [
    (0, '0'),
    (1, '1'),
    (2, '2'),
]

exang = [
    (0, 'No'),
    (1, 'Yes'),
]

slope = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
]

class NameForm(forms.Form):
    cp = forms.ChoiceField(label='Question 1: What is the chest pain type?', choices=cp, widget=forms.RadioSelect)
    max_heart_beat = forms.IntegerField(label='Question 2: What is the max heart beat?', widget=forms.NumberInput(attrs={'placeholder': 'Max heart beat'}))
    old_peak = forms.FloatField(label='Question 3: What is the old peak reading?', widget=forms.NumberInput(attrs={'placeholder': 'Old peak reading'}))
    major_vessels = forms.ChoiceField(label='Question 4: How many major vessels are coloured?', choices=major_vessels, widget=forms.RadioSelect)
    thal = forms.ChoiceField(label='Question 5: What is the thal type', choices=thal, widget=forms.RadioSelect)
    age = forms.IntegerField(label="Question 6: What is the patient's age?", widget=forms.NumberInput(attrs={'placeholder': 'Age'}))
    gender = forms.ChoiceField(label="Question 7: What is the patient's gender?", choices=gender, widget=forms.RadioSelect)
    chol = forms.IntegerField(label="Question 8: What is the total cholesterol level", widget=forms.NumberInput(attrs={'placeholder': 'Cholesterol level in mg/dl'}))
    trestbps = forms.IntegerField(label="Question 9: What is the resting blood pressure", widget=forms.NumberInput(attrs={'placeholder': 'Blood pressure in mm Hg'}))
    fbs = forms.ChoiceField(label="Question 10: Is fasting blood sugar higher than 120mg/dl?", choices=fbs, widget=forms.RadioSelect)
    restecg = forms.ChoiceField(label="Question 11: What is the resting ECG result?", choices=restecg, widget=forms.RadioSelect)
    exang = forms.ChoiceField(label="Question 12: Presence of exercise induced angina?", choices=exang, widget=forms.RadioSelect)
    slope = forms.ChoiceField(label='Question 13: What is the slope of the peak exercise ST segment?', choices=slope, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super(NameForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionnaire01'
        self.helper.layout = Layout(
        Fieldset(
            "Medical Questionnaire",
                Row('cp', css_class='form-group'),
                Row('max_heart_beat', css_class='form-group'),
                Row('old_peak', css_class='form-group'),
                Row('major_vessels', css_class='form-group'),
                Row('thal', css_class='form-group'),
                Row('age', css_class='form-group'),
                Row('gender', css_class='form-group'),
                Row('chol', css_class='form-group'),
                Row('trestbps', css_class='form-group'),
                Row('fbs', css_class='form-group'),
                Row('restecg', css_class='form-group'),
                Row('exang', css_class='form-group'),
                Row('slope', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        ),

    )

class NameFormThal(forms.Form):
    thal = forms.ChoiceField(label='What is the thal type', choices=thal, widget=forms.RadioSelect)
    
    def __init__(self, *args, **kwargs):
        super(NameFormThal, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionThal'
        self.helper.layout = Layout(
        Fieldset(
            "Medical Questionnaire",
                Row('thal', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        ),
    )

class NameFormCP(forms.Form):
    cp = forms.ChoiceField(label='What is the chest pain type?', choices=cp, widget=forms.RadioSelect)
    
    def __init__(self, *args, **kwargs):
        super(NameFormCP, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionCP'
        self.helper.layout = Layout(
        Fieldset(
            "Medical Questionnaire",
                Row('cp', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        ),
    )

class NameFormMaxhr(forms.Form):
    max_heart_beat = forms.IntegerField(label='What is the max heart beat?', widget=forms.NumberInput(attrs={'placeholder': 'Max heart beat'}))
    
    def __init__(self, *args, **kwargs):
        super(NameFormMaxhr, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionMaxhr'
        self.helper.layout = Layout(
        Fieldset(
            "Medical Questionnaire",
                Row('max_heart_beat', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        ),
    )

class NameFormFLVessels2(forms.Form):
    major_vessels = forms.ChoiceField(label='How many major vessels are coloured?', choices=major_vessels, widget=forms.RadioSelect)
    
    def __init__(self, *args, **kwargs):
        super(NameFormFLVessels2, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionFLVessels2'
        self.helper.layout = Layout(
        Fieldset(
            "Medical Questionnaire",
                Row('major_vessels', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        ),

    )

class NameFormFLVessels(forms.Form):
    major_vessels = forms.ChoiceField(label='How many major vessels are coloured?', choices=major_vessels, widget=forms.RadioSelect)
    
    def __init__(self, *args, **kwargs):
        super(NameFormFLVessels, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionFLVessels'
        self.helper.layout = Layout(
        Fieldset(
            "Medical Questionnaire",
                Row('major_vessels', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        ),

    )

class NameFormExang(forms.Form):
    exang = forms.ChoiceField(label="Presence of exercise induced angina?", choices=exang, widget=forms.RadioSelect)
    
    def __init__(self, *args, **kwargs):
        super(NameFormExang, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionExang'
        self.helper.layout = Layout(
        Fieldset(
            "Medical Questionnaire",
                Row('exang', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        ),

    )

class NameFormRestecg(forms.Form):
    restecg = forms.ChoiceField(label="What is the resting ECG result?", choices=restecg, widget=forms.RadioSelect)
    
    def __init__(self, *args, **kwargs):
        super(NameFormRestecg, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionRestecg'
        self.helper.layout = Layout(
        Fieldset(
            "Medical Questionnaire",
                Row('restecg', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        ),

    )

class NameFormCP2(forms.Form):
    cp = forms.ChoiceField(label='What is the chest pain type?', choices=cp, widget=forms.RadioSelect)
    
    def __init__(self, *args, **kwargs):
        super(NameFormCP2, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionnaire03'
        self.helper.add_input(Submit('skip', 'Skip', css_class='button white'))
        self.helper.layout = Layout(
        Fieldset(
            "Optional Medical Questionnaire",
                Row('cp', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white'),
            #Submit('cancel', 'Cancel', onclick='history.go(-1);')
        ),
    )

class NameFormMaxhr2(forms.Form):
    max_heart_beat = forms.IntegerField(label='What is the max heart beat?', widget=forms.NumberInput(attrs={'placeholder': 'Max heart beat'}))
    
    def __init__(self, *args, **kwargs):
        super(NameFormMaxhr2, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionnaire03'
        self.helper.add_input(Submit('skip', 'Skip', css_class='button white'))
        self.helper.layout = Layout(
        Fieldset(
            "Optional Medical Questionnaire",
                Row('max_heart_beat', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        ),
    )

class NameFormOldpeak(forms.Form):
    old_peak = forms.FloatField(label='What is the old peak reading?', widget=forms.NumberInput(attrs={'placeholder': 'Old peak reading'}))
    
    def __init__(self, *args, **kwargs):
        super(NameFormOldpeak, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionnaire03'
        self.helper.add_input(Submit('skip', 'Skip', css_class='button white'))
        self.helper.layout = Layout(
        Fieldset(
            "Optional Medical Questionnaire",
                Row('old_peak', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white'),
            #Button('cancel', 'Cancel', onclick='window.location.href="{}"'.format(cancel_url))
        ),
    )

class NameFormFLVessels3(forms.Form):
    major_vessels = forms.ChoiceField(label='How many major vessels are coloured?', choices=major_vessels, widget=forms.RadioSelect)
    
    def __init__(self, *args, **kwargs):
        super(NameFormFLVessels3, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionnaire03'
        self.helper.add_input(Submit('skip', 'Skip', css_class='button white'))
        self.helper.layout = Layout(
        Fieldset(
            "Optional Medical Questionnaire",
                Row('major_vessels', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white'),
            #Button('cancel', 'Cancel', onclick='window.location.href="{}"'.format(cancel_url))
        ),
    )

class NameFormThal2(forms.Form):
    thal = forms.ChoiceField(label='What is the thal type', choices=thal, widget=forms.RadioSelect)
    
    def __init__(self, *args, **kwargs):
        super(NameFormThal2, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionnaire03'
        self.helper.add_input(Submit('skip', 'Skip', css_class='button white'))
        self.helper.layout = Layout(
        Fieldset(
            "Optional Medical Questionnaire",
                Row('thal', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white'),
            #Button('cancel', 'Cancel', onclick='window.location.href="{}"'.format(cancel_url))
        ),
    )

class NameFormAge(forms.Form):
    age = forms.IntegerField(label="What is the patient's age?", widget=forms.NumberInput(attrs={'placeholder': 'Age'}))
    
    def __init__(self, *args, **kwargs):
        super(NameFormAge, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionnaire03'
        self.helper.add_input(Submit('skip', 'Skip', css_class='button white'))
        self.helper.layout = Layout(
        Fieldset(
            "Optional Medical Questionnaire",
                Row('age', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white'),
            #Button('cancel', 'Cancel', onclick='window.location.href="{}"'.format(cancel_url))
        ),
    )

class NameFormGender(forms.Form):
    gender = forms.ChoiceField(label="What is the patient's gender?", choices=gender, widget=forms.RadioSelect)
    
    def __init__(self, *args, **kwargs):
        super(NameFormGender, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionnaire03'
        self.helper.add_input(Submit('skip', 'Skip', css_class='button white'))
        self.helper.layout = Layout(
        Fieldset(
            "Optional Medical Questionnaire",
                Row('gender', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white'),
            #Button('cancel', 'Cancel', onclick='window.location.href="{}"'.format(cancel_url))
        ),
    )

class NameFormChol(forms.Form):
    chol = forms.IntegerField(label="What is the total cholesterol level", widget=forms.NumberInput(attrs={'placeholder': 'Cholesterol level in mg/dl'}))
    
    def __init__(self, *args, **kwargs):
        super(NameFormChol, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionnaire03'
        self.helper.add_input(Submit('skip', 'Skip', css_class='button white'))
        self.helper.layout = Layout(
        Fieldset(
            "Optional Medical Questionnaire",
                Row('chol', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white'),
            #Button('cancel', 'Cancel', onclick='window.location.href="{}"'.format(cancel_url))
        ),
    )

class NameFormTrestbps(forms.Form):
    trestbps = forms.IntegerField(label="What is the resting blood pressure", widget=forms.NumberInput(attrs={'placeholder': 'Blood pressure in mm Hg'}))
    
    def __init__(self, *args, **kwargs):
        super(NameFormTrestbps, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionnaire03'
        self.helper.add_input(Submit('skip', 'Skip', css_class='button white'))
        self.helper.layout = Layout(
        Fieldset(
            "Optional Medical Questionnaire",
                Row('trestbps', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white'),
            #Button('cancel', 'Cancel', onclick='window.location.href="{}"'.format(cancel_url))
        ),
    )

class NameFormFbs(forms.Form):
    fbs = forms.ChoiceField(label="Is fasting blood sugar higher than 120mg/dl?", choices=fbs, widget=forms.RadioSelect)
    
    def __init__(self, *args, **kwargs):
        super(NameFormFbs, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionnaire03'
        self.helper.add_input(Submit('skip', 'Skip', css_class='button white'))
        self.helper.layout = Layout(
        Fieldset(
            "Optional Medical Questionnaire",
                Row('fbs', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white'),
            #Button('cancel', 'Cancel', onclick='window.location.href="{}"'.format(cancel_url))
        ),
    )

class NameFormRestecg2(forms.Form):
    restecg = forms.ChoiceField(label="What is the resting ECG result?", choices=restecg, widget=forms.RadioSelect)
    
    def __init__(self, *args, **kwargs):
        super(NameFormRestecg2, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionnaire03'
        self.helper.add_input(Submit('skip', 'Skip', css_class='button white'))
        self.helper.layout = Layout(
        Fieldset(
            "Optional Medical Questionnaire",
                Row('restecg', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white'),
            #Button('cancel', 'Cancel', onclick='window.location.href="{}"'.format(cancel_url))
        ),
    )

class NameFormExang2(forms.Form):
    exang = forms.ChoiceField(label="Question 12: Presence of exercise induced angina?", choices=exang, widget=forms.RadioSelect)
    
    def __init__(self, *args, **kwargs):
        super(NameFormExang2, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionnaire03'
        self.helper.add_input(Submit('skip', 'Skip', css_class='button white'))
        self.helper.layout = Layout(
        Fieldset(
            "Optional Medical Questionnaire",
                Row('exang', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white'),
            #Button('cancel', 'Cancel', onclick='window.location.href="{}"'.format(cancel_url))
        ),
    )

class NameFormSlope(forms.Form):
    slope = forms.ChoiceField(label='What is the slope of the peak exercise ST segment?', choices=slope, widget=forms.RadioSelect)
    
    def __init__(self, *args, **kwargs):
        super(NameFormSlope, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionnaire03'
        self.helper.add_input(Submit('skip', 'Skip', css_class='button white'))
        self.helper.layout = Layout(
        Fieldset(
            "Optional Medical Questionnaire",
                Row('slope', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white'),
            #Button('cancel', 'Cancel', onclick='window.location.href="{}"'.format(cancel_url))
        ),
    )

smoke = [
    (0, 'No'),
    (1, 'Yes'),
]

drink = [
    (0, 'No'),
    (1, 'Yes'),
]

exercise = [
    (0, 'No'),
    (1, 'Yes'),
]

class NameForm01(forms.Form):
    smoke = forms.ChoiceField(label='Question 1: Is patient a regular smoker?', choices=smoke, widget=forms.RadioSelect)
    drink = forms.ChoiceField(label='Question 2: Is patient a regular drinker?', choices=drink, widget=forms.RadioSelect)
    exercise = forms.ChoiceField(label='Question 3: Does patient exercise regularly?', choices=exercise, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super(NameForm01, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-form'
        self.helper.form_class = 'class-form'
        self.helper.form_method = 'post'
        self.helper.form_action = 'questionnaire02'
        self.helper.layout = Layout(
        Fieldset(
            "Lifestyle Questionnaire",
                Row('smoke', css_class='form-group'),
                Row('drink', css_class='form-group'),
                Row('exercise', css_class='form-group'),
            css_class="fieldset",
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        ),

    )