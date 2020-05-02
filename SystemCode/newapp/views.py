from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .forms import NameForm, NameForm01
from .rules import *

def questionnaire01(request):
    form = NameForm(request.POST)
    if form.is_valid():
        #cd = form.cleaned_data
        cp = form.cleaned_data['cp']
        max_heart_beat = form.cleaned_data['max_heart_beat']
        old_peak = form.cleaned_data['old_peak']
        major_vessels = form.cleaned_data['major_vessels']
        thal = form.cleaned_data['thal']
        age = form.cleaned_data['age']
        gender = form.cleaned_data['gender']
        chol = form.cleaned_data['chol']
        trestbps = form.cleaned_data['trestbps']
        fbs = form.cleaned_data['fbs']
        restecg = form.cleaned_data['restecg']
        exang = form.cleaned_data['exang']
        slope = form.cleaned_data['slope']

        request.session['cp'] = cp
        request.session['max_heart_beat'] = max_heart_beat
        request.session['old_peak'] = old_peak
        request.session['major_vessels'] = major_vessels
        request.session['thal'] = thal
        request.session['age'] = age
        request.session['gender'] = gender
        request.session['chol'] = chol
        request.session['trestbps'] = trestbps
        request.session['fbs'] = fbs
        request.session['restecg'] = restecg
        request.session['exang'] = exang
        request.session['slope'] = slope
        return HttpResponseRedirect('questionnaire02')
    else:
        form = NameForm()
    return render(request, 'questionnaire01.html', {'form': form})

def questionnaire02(request):
    form = NameForm01(request.POST)
    if form.is_valid():
        #cd = form.cleaned_data
        smoke = int(form.cleaned_data['smoke'])
        if smoke == 1:
            request.session['smoke'] = "Yes"
        else:
            request.session['smoke'] = "No"
        drink = int(form.cleaned_data['drink'])
        if drink == 1:
            request.session['drink'] = "Yes"
        else:
            request.session['drink'] = "No"
        exercise = int(form.cleaned_data['exercise'])
        if exercise == 1:
            request.session['exercise'] = "Yes"
        else:
            request.session['exercise'] = "No"

        return HttpResponseRedirect('result')

    else:
        form = NameForm01()
    return render(request, 'questionnaire02.html', {'form': form})

def result(request):
    userans = request.session.items()
    dic = {}
    def listtodict(lis, dic):
        dic = dict(lis)
        return dic
    userans = listtodict(userans, dic)

    smoke = userans.get("smoke")
    drink = userans.get("drink")

    if smoke == 'No' and drink =='No':
        CF_lifestyle = 0
    elif smoke == 'Yes' and drink =='No':
        CF_lifestyle = 0.66
    elif smoke == 'No' and drink == 'Yes':
        CF_lifestyle = 0.81
    else:
        CF_lifestyle = 0.94

    result = return_scheme(userans)
    Prediction = result[0]
    CF_medical = result[1]
    Rule_no = result[2]
    print(Rule_no)  

    if CF_medical > 0:
        CF_net = CF_medical + CF_lifestyle*(1-CF_medical)
    else:
        CF_net = CF_medical

    if Rule_no == 1:
        Indicative_factors = f"Patient's most indicative factors are thal = {request.session['thal']}, cp = {request.session['cp']} and max_heart_beat = {request.session['max_heart_beat']}"
    elif Rule_no == 2:
        Indicative_factors = f"Patient's most indicative factors are thal = {request.session['thal']}, cp = {request.session['cp']} and max_heart_beat = {request.session['max_heart_beat']}"
    elif Rule_no == 3:
        Indicative_factors = f"Patient's most indicative factors are thal = {request.session['thal']}, cp = {request.session['cp']} and FLVessels = {request.session['major_vessels']}"
    elif Rule_no == 4:
        Indicative_factors = f"Patient's most indicative factors are thal = {request.session['thal']}, cp = {request.session['cp']} and FLVessels = {request.session['major_vessels']}"
    elif Rule_no == 5:
        Indicative_factors = f"Patient's most indicative factors are thal = {request.session['thal']}, FLVessels = {request.session['major_vessels']} and exercise-angina = {request.session['exang']}"
    elif Rule_no == 6:
        Indicative_factors = f"Patient's most indicative factors are thal = {request.session['thal']}, FLVessels = {request.session['major_vessels']} and exercise-angina = {request.session['exang']}"
    elif Rule_no == 7:
        Indicative_factors = f"Patient's most indicative factors are thal = {request.session['thal']}, FLVessels = {request.session['major_vessels']} and rest-ECG = {request.session['restecg']}"
    elif Rule_no == 8:
        Indicative_factors = f"Patient's most indicative factors are thal = {request.session['thal']}, FLVessels = {request.session['major_vessels']} and rest-ECG = {request.session['restecg']}"

    thisdict = {
        "cp": request.session['cp'],
        "max_heart_beat": request.session['max_heart_beat'],
        "old_peak": request.session['old_peak'],
        "FLVessels": request.session['major_vessels'],
        "thal": request.session['thal'],
        "age": request.session['age'],
        "gender": request.session['gender'],
        "chol": request.session['chol'],
        "trestbps": request.session['trestbps'],
        "fbs": request.session['fbs'],
        "rest-ECG": request.session['restecg'],
        "exercise-angina": request.session['exang'],
        "slope": request.session['slope'],
        "smoker": request.session['smoke'],
        "drinker": request.session['drink'],
        "exercise": request.session['exercise']
    }

    return render(request, 'result.html', {'Prediction': Prediction, 'CF_net': CF_net, 'Indicative_factors': Indicative_factors, 'data': thisdict.items()})


