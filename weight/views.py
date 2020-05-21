from django.shortcuts import render
from decimal import Decimal, getcontext
from django.http import HttpResponse
from django.template import loader
from weight.mymodules import opioid_conversion

# Create your views here.
def index(request):
    return render(request, 'weight/index.html')

def hello_get_query(request):
    return render(request, "weight/weight_calculate_input.html")

def weight_calculate_output(request):
    input_gender = int(request.POST["gender"])
    input_height = Decimal(request.POST["height"])
    input_weight = Decimal(request.POST["weight"])

    if input_gender == 0:
      pbw = Decimal(50) + Decimal(0.91) * (input_height - Decimal(152.4))
      pbw = str(f'{pbw:.2f}')
    else:
      pbw = Decimal(45.5) + Decimal(0.91) * (input_height - Decimal(152.4))
      pbw = str(f'{pbw:.2f}')

    #　除脂肪体重を計算する
    if input_gender == 0:
      lbw = Decimal(1.1) * input_weight - Decimal(128) * (input_weight / input_height) * (input_weight / input_height)
      lbw = str(f'{lbw:.2f}')
    else:
      lbw = Decimal(1.07) * input_weight - Decimal(148) * (input_weight / input_height) * (input_weight / input_height)
      lbw = str(f'{lbw:.2f}')

    #　理想体重を計算する
    ibw = Decimal(22) * (input_height / Decimal(100)) * (input_height / Decimal(100))
    ibw = str(f'{ibw:.2f}')

    template = loader.get_template("weight/weight_calculate_output.html")
    context = {
        "gender" : input_gender,
        "height" : input_height,
        "weight" : input_weight,
        "pbw" : pbw,
        "lbw" : lbw,
        "ibw" : ibw,
    }
    return HttpResponse(template.render(context, request))

def opioid_conv_query(request):
    return render(request, "weight/opioid_conv_input.html")

def opioid_conv_output(request):
    input_opioid_use = request.POST["opioid_use"]
    input_opioid_dose = Decimal(request.POST["opioid_dose"])
    odcm = opioid_conversion.opi_dose_conv_mor(input_opioid_use, input_opioid_dose)
    mco = opioid_conversion.mor_conv_opioids(odcm)

    template = loader.get_template("weight/opioid_conv_output.html")
    context = {
        "opioid_use" : input_opioid_use,
        "opioid_dose" : input_opioid_dose,
        "conv_opioids" : mco
    }
    return HttpResponse(template.render(context, request))
