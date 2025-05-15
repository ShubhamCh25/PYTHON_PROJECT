from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .models import Data
import json
# Create your views here.
def hello(request):
 
   if(request.method=='POST'):
       prev=Data.objects.all()
       prev.delete()
       name=request.FILES.get('file')
       if(name):
         df=pd.read_csv(name)
         json_df=df.reset_index().to_json(orient='records')
         json_data=json.loads(json_df)
         for i in json_data:
            exp_mon=i['emi']+i['tax']+i['other_exp']
            inc_mon=i['property_rent']-exp_mon
            d=Data(name=i['property_name'],price=i['property_price'],rent=i['property_rent'],emi=i['emi'],tax=i['tax'],exp=i['other_exp'],expenses_monthly=exp_mon,incomes_monthly=inc_mon)
            d.save()
         data_objects=Data.objects.all()
         context={'data_objects':data_objects}
         return render(request,'myapp/index.html', context)
       else:
         return render(request,'myapp/index.html')
   else:
        print("get")  
        return render(request,'myapp/index.html')
