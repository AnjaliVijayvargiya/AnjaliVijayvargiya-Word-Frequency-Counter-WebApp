from django.shortcuts import render
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import Counter
from nltk.corpus import stopwords
from .forms import URLForm
from .models import EntryURL

# Create your views here.

# This function will add new items and show all items
def add_show(request):
    if request.method == 'POST':
        fm = URLForm(request.POST)
        if fm.is_valid():
            url = fm.cleaned_data['URL']
            if EntryURL.objects.filter(URL=url).exists():
                print('Same URL')
                value = 'Database'
                data1 = EntryURL.objects.get(URL=url)
            else:
                #target_url = "https://www.geeksforgeeks.org/django-tutorial/"
                print(url)
                response = urlopen(url)
                html = response.read()
                clean = BeautifulSoup(html,features="html.parser").get_text()
                print(type(clean))
                s=set(stopwords.words('english'))
                clean1 = clean.split()
                clean11 = filter(lambda w: not w in s,clean1)
                counter = Counter(clean11)
                most_occur = counter.most_common(10)
                print(type(most_occur))
                #url = 'hello'
                E1 = most_occur[0][0]
                E1O = most_occur[0][1]
                E2 = most_occur[1][0]
                E2O = most_occur[1][1]
                E3 = most_occur[2][0]
                E3O = most_occur[2][1]
                E4 = most_occur[3][0]
                E4O = most_occur[3][1]
                E5 = most_occur[4][0]
                E5O = most_occur[4][1]
                E6 = most_occur[5][0]
                E6O = most_occur[5][1]
                E7 = most_occur[6][0]
                E7O = most_occur[6][1]
                E8 = most_occur[7][0]
                E8O = most_occur[7][1]
                E9 = most_occur[8][0]
                E9O = most_occur[8][1]
                E10 = most_occur[9][0]
                E10O = most_occur[9][1]
                
                reg = EntryURL(URL=url,E1=E1,E1O=E1O,E2=E2,E2O=E2O,E3=E3,E3O=E3O,E4=E4,E4O=E4O,E5=E5,E5O=E5O,E6=E6,E6O=E6O,E7=E7,E7O=E7O,E8=E8,E8O=E8O,E9=E9,E9O=E9O,E10=E10,E10O=E10O)
                reg.save()
                value = 'Freshly Processed'
                data1 = EntryURL.objects.get(URL=url)
                fm = URLForm()
            return render(request,'freq.html',{'form':fm,'st':data1,'value':value})
    else:
        fm = URLForm()
    entries = EntryURL.objects.all()
    return render(request,'display.html',{'form':fm,'entries':entries,})

def display(request):
    fm = URLForm()
    entries = EntryURL.objects.all()
    return render(request,'display.html',{'form':fm,'entries':entries,})