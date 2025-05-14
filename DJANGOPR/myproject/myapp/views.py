from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
# Create your views here.
def hello(request):
 
    if(request.method=='POST'):
       name=request.FILES.get('file')
       df=pd.read_csv(name)
       print(df)
    return render(request,'myapp/index.html')
