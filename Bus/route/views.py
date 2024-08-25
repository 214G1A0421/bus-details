from django.shortcuts import render

# Create your views here.
def func1(request):
    blist={'bus':[{'bid':'Bus1','Route':'Darmavaram','stime':"7am",'rtime':"9:10am"},
                  {'bid':'Bus2','Route':'atp','stime':"8:00am",'rtime':"9:00am"},
                  {'bid':'Bus3','Route':'tadipatri','stime':"8:10am",'rtime':"9:10am"},
                  {'bid':'Bus4','Route':'bks','stime':"8:30am",'rtime':"9:05am"}]}
    return render(request,'srch.html',blist)

