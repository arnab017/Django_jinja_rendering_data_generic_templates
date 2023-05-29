from django.shortcuts import render

# Create your views here.
def app1_htmlpage(request):
    app1_dic = {
        'name': 'Application-1 HTML Page',
        'loc':'App1/Views'
    }
    return render(request,'app1_htmlpage.html',context=app1_dic)
