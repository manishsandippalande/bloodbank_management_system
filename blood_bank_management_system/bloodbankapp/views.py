from django.shortcuts import render, redirect
from bloodbankapp.models import patients, donors, bloodbank


# Create your views here.
def home(request):
    return render(request, "index.html")


def addpatient(request):
    if request.method == "GET":
        return render(request, "addpatient.html")
    else:
        name = request.POST["patientname"]
        gender = request.POST["patientgender"]
        bg = request.POST["patientbg"]
        quant = request.POST["quantity"]
        data = patients.objects.create(patient_name=name, gender=gender, patient_bloodgroup=bg, quantity=quant)
        data.save()
        bloodbankdata = bloodbank.objects.filter(bgroup=bg)
        dbquant = bloodbankdata[0].quantity
        intquant = int(dbquant) - int(quant)
        bloodbankdata.update(quantity=intquant, donated_quantity=0)
        return redirect("/patients")


def adddonor(request):
    if request.method == "GET":
        return render(request, "adddonor.html")
    else:
        name = request.POST["donorname"]
        gender = request.POST["donorgender"]
        bg = request.POST["donorbg"]
        quant = request.POST["quantity"]
        data = donors.objects.create(donor_name=name, gender=gender, donor_bloodgroup=bg, quantity=quant)
        data.save()
        bloodbankdata = bloodbank.objects.filter(bgroup=bg)
        dbquant = bloodbankdata[0].quantity
        intquant = int(quant) + int(dbquant)
        print(intquant)
        bloodbankdata.update(quantity=intquant)
        return redirect("/donors")


def dashboard(request):
    patientsdata = patients.objects.all()
    donorsdata = donors.objects.all()
    blooddata = bloodbank.objects.all()
    context = {}
    context["patientsdata"] = patientsdata
    context["donorsdata"] = donorsdata
    context["blooddata"] = blooddata
    return render(request, "dashboard.html", context)


# delete Actions


# patient
def deletepatient(request, pid):
    data = patients.objects.filter(id=pid)
    quant = data[0].quantity
    bg = data[0].patient_bloodgroup
    data.delete()
    bloodbankdata = bloodbank.objects.filter(bgroup=bg)
    dbquant = bloodbankdata[0].quantity
    intquant = int(dbquant) + int(quant)
    print(intquant)
    bloodbankdata.update(quantity=intquant)
    return redirect("/dashboard#patientdata")


# donors
def deletedonor(request, did):
    data = donors.objects.filter(id=did)
    quant = data[0].quantity
    bg = data[0].donor_bloodgroup
    data.delete()
    bloodbankdata = bloodbank.objects.filter(bgroup=bg)
    dbquant = bloodbankdata[0].quantity
    intquant = int(dbquant) - int(quant)
    print(intquant)
    bloodbankdata.update(quantity=intquant)
    return redirect("/dashboard#donorsdata")


# update Actions


# patient
def updatepatient(request, pid):
    context = {}
    data = patients.objects.filter(id=pid)
    context["data"] = data[0]
    return render(request, "updatepatient.html", context)


def updatepatient_method(request, pid):
    if request.method == "GET":
        return render(request, "updatepatient.html")
    else:
        name = request.POST["patientname"]
        gender = request.POST["patientgender"]
        bg = request.POST["patientbg"]
        quant = request.POST["quantity"]
        patientsolddata = patients.objects.filter(id=pid)
        oldquant = patientsolddata[0].quantity
        patients.objects.filter(id=pid).update(patient_name=name, gender=gender, patient_bloodgroup=bg, quantity=quant)
        bloodbankdata = bloodbank.objects.filter(bgroup=bg)
        dbquant = bloodbankdata[0].quantity
        intquant = int(dbquant) + int(oldquant) - int(quant)
        bloodbankdata.update(quantity=intquant, donated_quantity=0)
        return redirect("/dashboard")


# patient
def updatedonor(request, did):
    context = {}
    data = donors.objects.filter(id=did)
    context["data"] = data[0]
    return render(request, "updatedonor.html", context)


def updatedonor_method(request, did):
    if request.method == "GET":
        return render(request, "updatedonor.html")
    else:
        name = request.POST["donorname"]
        gender = request.POST["donorgender"]
        bg = request.POST["donorbg"]
        quant = request.POST["quantity"]
        donorolddata = donors.objects.filter(id=did)
        oldquant = donorolddata[0].quantity
        donors.objects.filter(id=did).update(
            donor_name=name, gender=gender, donor_bloodgroup=bg, quantity=quant
        )
        bloodbankdata = bloodbank.objects.filter(
            bgroup=donorolddata[0].donor_bloodgroup
        )
        dbquant = bloodbankdata[0].quantity
        intquant = int(dbquant) - int(oldquant) + int(quant)
        bloodbankdata.update(quantity=intquant, donated_quantity=0)
        return redirect("/dashboard")



# unit convertor
def uniconvert(request):
    ml = request.POST["quantity"]
    l = ml/1000
    return l

# about
def aboutpage(request):
    return render(request, 'aboutpage.html')