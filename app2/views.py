from django.shortcuts import render

# Create your views here.
def app2_htmlpage(request):
    app2_dic = {
        'name' : 'Application-2 HTML Page',
        'loc' : 'App2/views'
    }
    return render(request,'app2_htmlpage.html',context=app2_dic)