from django.shortcuts import render
from decimal import Decimal, getcontext
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'weight/index.html')

def hello_get_query(request):
    d = {
        "your_name" : request.GET.get("your_name")
    }
    return render(request, "weight/weight_calculate_input.html", d)

def weight_calculate_output(request):
    input_gender = int(request.POST["gender"])
    input_height = Decimal(request.POST["height"])
    input_weight = Decimal(request.POST["weight"])

    if input_gender == 0:
      pbw = Decimal(50) + Decimal(0.91) * (input_height - Decimal(152.4))
      pbw = str(pbw)
    elif input_gender == 1:
      pbw = Decimal(45.5) + Decimal(0.91) * (input_height - Decimal(152.4))
      pbw = str(pbw)
    else:
      pbw = "性別を正しく入力してください"

    #　除脂肪体重を計算する
    if input_gender == 0:
      lbw = Decimal(1.1) * input_weight - Decimal(128) * (input_weight / input_height) * (input_weight / input_height)
      lbw = str(lbw)
    elif input_gender == 1:
      lbw = Decimal(1.07) * input_weight - Decimal(148) * (input_weight / input_height) * (input_weight / input_height)
      lbw = str(lbw)
    else:
      lbw = "性別を正しく入力してください"

    #　理想体重を計算する
    ibw = Decimal(22) * (input_height / Decimal(100)) * (input_height / Decimal(100))
    ibw = str(ibw)

    getcontext().prec = 4

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
