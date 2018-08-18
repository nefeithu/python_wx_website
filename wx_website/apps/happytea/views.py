from django.shortcuts import render

# Create your views here.
def wxmp(request):
    if request.method == 'GET':
        echostr = request.GET.get('echostr')
        logger.info('wx reg succ')
        return HttpResponse(echostr)