from django.shortcuts import render, redirect
from . models import UserPersonalModel
from . forms import UserPersonalForm, UserRegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import numpy as np
import joblib


def Landing_1(request):
    return render(request, '1_Landing.html')

def Register_2(request):
    form = UserRegisterForm()
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('Login_3')
        else:
            messages.error(request,form.errors)

    context = {'form':form}
    return render(request, '2_Register.html', context)


def Login_3(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home_4')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'3_Login.html', context)

def Home_4(request):
    return render(request, '4_Home.html')

def Teamates_5(request):
    return render(request,'5_Teamates.html')

def Domain_Result_6(request):
    return render(request,'6_Domain_Result.html')

def Problem_Statement_7(request):
    return render(request,'7_Problem_Statement.html')
    

def Per_Info_8(request):
    if request.method == 'POST':
        fieldss = ['firstname','lastname','age','address','phone','city','state','country']
        form = UserPersonalForm(request.POST)
        if form.is_valid():
            print('Saving data in Form')
            form.save()
        return render(request, '4_Home.html', {'form':form})
    else:
        print('Else working')
        form = UserPersonalForm(request.POST)    
        return render(request, '8_Per_Info.html', {'form':form})
    
Model = joblib.load('APP\INTRUSION.pkl')

    
def Deploy_9(request): 
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]
        print(int_features)
        final_features = [np.array(int_features, dtype=object)]
        print(final_features)
        prediction = Model.predict(final_features)
        print(prediction)
        output = prediction[0]
        print(f'output{output}')
        if output == 0:
            A = "THE DENIAL OF SERVICE (DOS) ATTACK MIGHT BE OCCUR IN THIS CONDITION"
            B = "PREVENTION: Preventing a Denial of Service (DoS) attack involves implementing robust network security measures, such as deploying firewalls and intrusion detection/prevention systems. Additionally, regularly updating and patching software vulnerabilities can thwart potential attack vectors. Employing rate limiting and traffic filtering mechanisms helps mitigate the impact of sudden, excessive requests, enhancing overall system resilience against DoS threats."
            return render(request, '9_Deploy.html', {"prediction_text":A, "prediction_text1":B})
        elif output == 1:
            A = "THE NONE OF ATTACK MIGHT BE OCCUR IN THIS CONDITION. THIS IS NORMAL"
            B = "PREVENTION: THERE ARE NO NEED PREVENTIONS. "
            return render(request, '9_Deploy.html', {"prediction_text":A, "prediction_text1":B})
        elif output == 2:
            A = "THE PROBE ATTACK MIGHT BE OCCUR IN THIS CONDITION"
            B = "PREVENTION: Preventing probe attacks involves implementing strong network security practices. Regularly monitoring and analyzing network traffic for anomalous patterns can help detect probes early. Additionally, deploying intrusion detection systems and keeping software and systems updated with the latest security patches further fortifies defenses against potential probing activities."
            return render(request, '9_Deploy.html', {"prediction_text":A, "prediction_text1":B})
        elif output == 3:
            A = "THE REMOTE TO LOCAL (R2L) ATTACK MIGHT BE OCCUR IN THIS CONDITION"
            B = "PREVENTION: Preventing Remote-to-Local (R2L) attacks requires securing remote access points. Employing strong authentication mechanisms, such as multi-factor authentication, enhances the security of remote connections. Regularly auditing and monitoring access logs for unusual activities helps identify and mitigate potential R2L threats promptly."
            return render(request, '9_Deploy.html', {"prediction_text": A, "prediction_text1": B})
        elif output == 4:
            A = "THE USER-TO-ROOT (U2R) ATTACK MIGHT BE OCCUR IN THIS CONDITION"
            B = "PREVENTION: Mitigating User-to-Root (U2R) attacks involves implementing robust access controls. Employ the principle of least privilege to restrict user permissions, minimizing the impact of potential exploits. Regularly update and patch system vulnerabilities to address known security weaknesses, reducing the likelihood of successful U2R attacks. Additionally, continuous monitoring of user activities and behavior can aid in the early detection of suspicious actions, enhancing overall system security." 
            return render(request, '9_Deploy.html', {"prediction_text": A, "prediction_text1": B})

    else:
        return render(request, '9_Deploy.html')


def Per_Database_10(request):
    models = UserPersonalModel.objects.all()
    return render(request, '10_Per_Database.html', {'models':models})

def Logout(request):
    logout(request)
    return redirect('Register_2')
