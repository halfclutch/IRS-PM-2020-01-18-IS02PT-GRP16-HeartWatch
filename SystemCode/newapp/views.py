from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .forms import NameForm, NameForm01, NameFormThal, NameFormCP, NameFormMaxhr, NameFormFLVessels2, NameFormFLVessels, NameFormExang, NameFormRestecg
from .forms import NameFormCP2, NameFormMaxhr2, NameFormOldpeak, NameFormFLVessels3, NameFormThal2, NameFormAge, NameFormGender, NameFormChol, NameFormTrestbps, NameFormFbs, NameFormRestecg2, NameFormExang2, NameFormSlope
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
        return HttpResponseRedirect('questionHB')
    else:
        form = NameForm()
    return render(request, 'questionnaire01.html', {'form': form})

def questionThal(request):
    #initialize values of parameters
    cp = '-1'
    max_heart_beat = '-1'
    old_peak = '-1'
    major_vessels = '-1'
    thal = '-1'
    age = '-1'
    gender = '-1'
    chol = '-1'
    trestbps = '-1'
    fbs = '-1'
    restecg = '-1'
    exang = '-1'
    slope = '-1'

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

    form = NameFormThal(request.POST)
    if form.is_valid():
        #cd = form.cleaned_data
        thal = form.cleaned_data['thal']

        request.session['thal'] = thal
        
        if int(thal) == 3:
            return HttpResponseRedirect('questionCP')
        elif int(thal) == 6 or int(thal) == 7 :
            return HttpResponseRedirect('questionFLVessels')
    else:
        form = NameFormThal()
    return render(request, 'questionnaire01.html', {'form': form})

def questionCP(request):
    form = NameFormCP(request.POST)
    if form.is_valid():
        #cd = form.cleaned_data
        cp = form.cleaned_data['cp']

        request.session['cp'] = cp
        
        if int(cp) == 2 or int(cp) == 3:
            return HttpResponseRedirect('questionMaxhr')
        elif int(cp) == 1 or int(cp) == 4:
            return HttpResponseRedirect('questionFLVessels2')
    else:
        form = NameFormCP()
    return render(request, 'questionnaire01.html', {'form': form})

def questionMaxhr(request):
    form = NameFormMaxhr(request.POST)
    if form.is_valid():
        #cd = form.cleaned_data
        max_heart_beat = form.cleaned_data['max_heart_beat']

        request.session['max_heart_beat'] = max_heart_beat
        
        return HttpResponseRedirect('questionnaire02')
    else:
        form = NameFormMaxhr()
    return render(request, 'questionnaire01.html', {'form': form})

def questionFLVessels2(request):
    form = NameFormFLVessels2(request.POST)
    if form.is_valid():
        #cd = form.cleaned_data
        major_vessels = form.cleaned_data['major_vessels']

        request.session['major_vessels'] = major_vessels
        
        return HttpResponseRedirect('questionnaire02')
    else:
        form = NameFormFLVessels2()
    return render(request, 'questionnaire01.html', {'form': form})

def questionFLVessels(request):
    form = NameFormFLVessels(request.POST)
    if form.is_valid():
        #cd = form.cleaned_data
        major_vessels = form.cleaned_data['major_vessels']

        request.session['major_vessels'] = major_vessels
        
        if int(major_vessels) == 0:
            return HttpResponseRedirect('questionExang')
        elif int(major_vessels) > 0:
            return HttpResponseRedirect('questionRestecg')
    else:
        form = NameFormFLVessels()
    return render(request, 'questionnaire01.html', {'form': form})

def questionExang(request):
    form = NameFormExang(request.POST)
    if form.is_valid():
        #cd = form.cleaned_data
        exang = form.cleaned_data['exang']

        request.session['exang'] = exang
        
        return HttpResponseRedirect('questionnaire02')
    else:
        form = NameFormExang()
    return render(request, 'questionnaire01.html', {'form': form})

def questionRestecg(request):
    form = NameFormRestecg(request.POST)
    if form.is_valid():
        #cd = form.cleaned_data
        restecg = form.cleaned_data['restecg']

        request.session['restecg'] = restecg
        
        return HttpResponseRedirect('questionnaire02')
    else:
        form = NameFormRestecg()
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

def questionnaire03(request):
    #cd = form.cleaned_data
    if  'skip' in request.POST:
        return HttpResponseRedirect('result')
    if request.session['cp'] == '-1':
            form = NameFormCP2(request.POST)
            if form.is_valid():
                cp = form.cleaned_data['cp']
                request.session['cp'] = cp
                return HttpResponseRedirect('questionnaire03')
            else:
                form = NameFormCP2()
            return render(request, 'questionnaire01.html', {'form': form})         
    elif request.session['max_heart_beat'] == '-1':
            form = NameFormMaxhr2(request.POST)
            if form.is_valid():
                max_heart_beat = form.cleaned_data['max_heart_beat']
                request.session['max_heart_beat'] = max_heart_beat
                return HttpResponseRedirect('questionnaire03')
            else:
                form = NameFormMaxhr2()
            return render(request, 'questionnaire01.html', {'form': form})
    elif request.session['old_peak'] == '-1':
            form = NameFormOldpeak(request.POST)
            if form.is_valid():
                old_peak = form.cleaned_data['old_peak']
                request.session['old_peak'] = old_peak
                return HttpResponseRedirect('questionnaire03')
            else:
                form = NameFormOldpeak()
            return render(request, 'questionnaire01.html', {'form': form})
    elif request.session['major_vessels'] == '-1':
            form = NameFormFLVessels3(request.POST)
            if form.is_valid():
                major_vessels = form.cleaned_data['major_vessels']
                request.session['major_vessels'] = major_vessels
                return HttpResponseRedirect('questionnaire03')
            else:
                form = NameFormFLVessels3()
            return render(request, 'questionnaire01.html', {'form': form})
    elif request.session['thal'] == '-1':
            form = NameFormThal2(request.POST)
            if form.is_valid():
                thal = form.cleaned_data['thal']
                request.session['thal'] = thal
                return HttpResponseRedirect('questionnaire03')
            else:
                form = NameFormThal2()
            return render(request, 'questionnaire01.html', {'form': form})
    elif request.session['age'] == '-1':
            form = NameFormAge(request.POST)
            if form.is_valid():
                age = form.cleaned_data['age']
                request.session['age'] = age
                return HttpResponseRedirect('questionnaire03')
            else:
                form = NameFormAge()
            return render(request, 'questionnaire01.html', {'form': form})
    elif request.session['gender'] == '-1':
            form = NameFormGender(request.POST)
            if form.is_valid():
                gender = form.cleaned_data['gender']
                request.session['gender'] = gender
                return HttpResponseRedirect('questionnaire03')
            else:
                form = NameFormGender()
            return render(request, 'questionnaire01.html', {'form': form})
    elif request.session['chol'] == '-1':
            form = NameFormChol(request.POST)
            if form.is_valid():
                chol = form.cleaned_data['chol']
                request.session['chol'] = chol
                return HttpResponseRedirect('questionnaire03')
            else:
                form = NameFormChol()
            return render(request, 'questionnaire01.html', {'form': form})
    elif request.session['trestbps'] == '-1':
            form = NameFormTrestbps(request.POST)
            if form.is_valid():
                trestbps = form.cleaned_data['trestbps']
                request.session['trestbps'] = trestbps
                return HttpResponseRedirect('questionnaire03')
            else:
                form = NameFormTrestbps()
            return render(request, 'questionnaire01.html', {'form': form})
    elif request.session['fbs'] == '-1':
            form = NameFormFbs(request.POST)
            if form.is_valid():
                fbs = form.cleaned_data['fbs']
                request.session['fbs'] = fbs
                return HttpResponseRedirect('questionnaire03')
            else:
                form = NameFormFbs()
            return render(request, 'questionnaire01.html', {'form': form})
    elif request.session['restecg'] == '-1':
            form = NameFormRestecg2(request.POST)
            if form.is_valid():
                restecg = form.cleaned_data['restecg']
                request.session['restecg'] = restecg
                return HttpResponseRedirect('questionnaire03')
            else:
                form = NameFormRestecg2()
            return render(request, 'questionnaire01.html', {'form': form})
    elif request.session['exang'] == '-1':
            form = NameFormExang2(request.POST)
            if form.is_valid():
                exang = form.cleaned_data['exang']
                request.session['exang'] = exang
                return HttpResponseRedirect('questionnaire03')
            else:
                form = NameFormExang2()
            return render(request, 'questionnaire01.html', {'form': form})
    elif request.session['slope'] == '-1':
            form = NameFormSlope(request.POST)
            if form.is_valid():
                slope = form.cleaned_data['slope']
                request.session['slope'] = slope
                return HttpResponseRedirect('result')
            else:
                form = NameFormSlope()
            return render(request, 'questionnaire01.html', {'form': form})
           

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

    if CF_net > 0.5:
        Prediction = True
    else:
        Prediction = False
        CF_net = 1-CF_net

    if Rule_no == 1:
        Indicative_factors = f"Thallium Stress Test -> {request.session['thal']}, Chest Pain Type -> {request.session['cp']} and Max Heart Rate -> {request.session['max_heart_beat']}"
    elif Rule_no == 2:
        Indicative_factors = f"Thallium Stress Test -> {request.session['thal']}, Chest Pain Type -> {request.session['cp']} and Max Heart Rate -> {request.session['max_heart_beat']}"
    elif Rule_no == 3:
        Indicative_factors = f"Thallium Stress Test -> {request.session['thal']}, Chest Pain Type -> {request.session['cp']} and Vessels highlighted by fluroscopy -> {request.session['major_vessels']}"
    elif Rule_no == 4:
        Indicative_factors = f"Thallium Stress Test -> {request.session['thal']}, Chest Pain Type -> {request.session['cp']} and Vessels highlighted by fluroscopy -> {request.session['major_vessels']}"
    elif Rule_no == 5:
        Indicative_factors = f"Thallium Stress Test -> {request.session['thal']}, Vessels highlighted by fluroscopy -> {request.session['major_vessels']} and Exercise-Angina -> {request.session['exang']}"
    elif Rule_no == 6:
        Indicative_factors = f"Thallium Stress Test -> {request.session['thal']}, Vessels highlighted by fluroscopy -> {request.session['major_vessels']} and Exercise-Angina -> {request.session['exang']}"
    elif Rule_no == 7:
        Indicative_factors = f"Thallium Stress Test -> {request.session['thal']}, Vessels highlighted by fluroscopy -> {request.session['major_vessels']} and Rest-ECG -> {request.session['restecg']}"
    elif Rule_no == 8:
        Indicative_factors = f"Thallium Stress Test -> {request.session['thal']}, Vessels highlighted by fluroscopy -> {request.session['major_vessels']} and Rest-ECG -> {request.session['restecg']}"

    thisdict = {
        "Chest Pain Type": request.session['cp'],
        "Max Heart Rate achieved": request.session['max_heart_beat'],
        #"old_peak": request.session['old_peak'],
        "Number of Major Vessels colored by Fluoroscopy": request.session['major_vessels'],
        "Thallium Stress Test results: 3 = Normal; 6 = Fixed Defect; 7 = Reversable Defect": request.session['thal'],
        #"age": request.session['age'],
        #"gender": request.session['gender'],
        #"chol": request.session['chol'],
        #"trestbps": request.session['trestbps'],
        #"fbs": request.session['fbs'],
        "Resting ECG results": request.session['restecg'],
        "Exercise-induced Angina": request.session['exang'],
        #"slope": request.session['slope'],
        "Smoker": request.session['smoke'],
        "Drinker": request.session['drink'],
        "Exercise": request.session['exercise']
    }

    return render(request, 'result.html', {'Prediction': Prediction, 'CF_net': "{:.2f}".format(CF_net), 'Indicative_factors': Indicative_factors, 'data': thisdict.items()})


