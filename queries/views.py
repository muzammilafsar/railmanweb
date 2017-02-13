from .forms import LiveTrain,PnrForm

from django.shortcuts import render
from django.http import HttpResponse

import requests
import time,json
# Create your views here.
# API_KEY='6tu546dr'
# API_KEY='9z2fd4ou'
# API_KEY='4hriszqg'
API_KEY='bbfeijve'
def home(request):

    return render(request,'queries/index.html')
def check_status(request,train_no):

    return HttpResponse(liveTrain(train_no))
def liveTrain(request):
    context={}
    if request.method=='POST':
        train_no=request.POST.get('train_no')
        #train_no='19019'
        if len(train_no)!=5:
            context.update({'error':"Enter a valid 5 digit train Number"})
        else:
            api="http://api.railwayapi.com/live/train/"+train_no+"/doj/"+str(time.strftime("%Y%m%d"))+"/apikey/"+API_KEY+"/"
            print(api)
            data=json.loads(requests.get(api).text)
            if data['response_code']==200:
                context.update({'route':data['route']})
                context.update({'data': data})
            context.update({'response_code': int(data['response_code'])})

    return render(request,'queries/livetrain.html',context)



def pnr_status(request):
    answer = {}
    context = {}

    if request.method == 'POST':
        pnr_no=request.POST.get('pnr')
        #pnr_no="4128701194"
        url='http://api.railwayapi.com/pnr_status/pnr/'+str(pnr_no)+'/apikey/'+API_KEY+'/'
        print(url)
        data=json.loads(requests.get(url).text)
        form=PnrForm(request.POST)
        if form.is_valid():
            pnr_no=form.cleaned_data['pnr']
        if len(pnr_no)!=10:
            context.update({"error":"Enter a valid 10 digit PNR"})
        else:
            if data["response_code"]==200:
                answer.update({"pnr_no":pnr_no})
                answer.update({"date_of_journey":data["doj"]})
                answer.update({"from":data["from_station"]["name"]})
                answer.update({"to":data["to_station"]["name"]})
                answer.update({"train_no":data["train_num"]})
                answer.update({"train_name": data["train_name"]})
                answer.update({"chart_prepared": data["chart_prepared"]})
                context.update({"passengers":data["passengers"]})
            else:
                answer.update({"error":data["error"]})
            context.update({'response_code': int(data['response_code'])})

    context.update({"answer":answer})

    return render(request,'queries/web.html',context)

# Create your views here.
