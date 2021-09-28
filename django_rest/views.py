from django.shortcuts import render, redirect
from .models import meterReadings
from .forms import restSerializer
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view


"""@csrf_exempt
def restApi_list(request):
    if request.method=='GET':
        restApi=meterReadings.objects.all()
        restApi_serializer = restSerializer(restApi,many=trye)
        return JsonResponse(restApi_serializer.data, safe=False)
    elif request.method=='POST':
        restApi_data=JSONParser().parse(request)
        rest_serializer = restSerializer(data=restApi_data)
        if rest_serializer.is_valid():
            rest_serializer.save()
            return JsonResponse(rest_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(rest_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def restApi_detail(request, pk):
    try:
        restApi = meterReadings.objects.get(pk=pk)
    except meterReadings.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        restApi_serializer = restSerializer(restApi)
        return JsonResponse(restApi_serializer.data)

    elif request.method == 'PUT':
        restapi_data = JSONParser().parse(request)
        rest_serializer = CustomerSerializer(restApi, data=restapi_data)
        if rest_serializer.is_valid():
            rest_serializer.save()
            return JsonResponse(rest_serializer.data)
        return JsonResponse(rest_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        restApi.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)"""

# Create your views here.
def bookList(request):
    books = meterReadings.objects.all()
    return render(request,"book-list.html",{'meters':books})
@api_view(['GET', 'POST'])
def bookCreate(request):
    if request.method == "POST":
        form = restSerializer(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return HttpResponseRedirect('book-list')
            except:
                pass
    else:
        form = restSerializer()
    return render(request,'book-create.html',{'form':form})

def bookUpdate(request, id):
    book = meterReadings.objects.get(id=id)
    form = restSerializer(initial={'house': meterReadings.house, 'flat': meterReadings.flat, 'choicesMater': meterReadings.choicesMater, 'metRadings': meterReadings.metRadings})
    if request.method == "POST":
        form = restSerializer(request.POST, instance=book)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return HttpResponseRedirect('/book-list')
            except Exception as e:
                pass
    return render(request,'book-update.html',{'form':form})

def bookDelete(request, id):
    book = meterReadings.objects.get(id=id)
    try:
        book.delete()
    except:
        pass
    return redirect('book-list')
