from django.shortcuts import render,redirect
from . import Pool
from django.http import JsonResponse

def CategoryInterface(request):
    try:
        admin=request.session['admin']
        return render(request,'CategoryInterface.html',{'msg':'','records':request.session['admin']})
    except:
        return render(request,'AdminLogin.html',{'msg':''})

def SubmitCategory(request):
   try:
     db,cmd=Pool.ConnectionPooling()
     categoryname=request.POST['categoryname']
     iconfile=request.FILES['categoryicon']
     q="insert into categories(categoryname,categoryicon) values('{0}','{1}')".format(categoryname,iconfile.name)
     print(q)
     cmd.execute(q)
     db.commit()
     F=open("D:/medassist_ecom/assets/inputicons/"+iconfile.name,"wb")
     for chunk in iconfile.chunks():
        F.write(chunk)
     F.close()
     db.close()
     return render(request, "categoryinterface.html", {'msg': 'Record Submitted','records':request.session['admin']})
   except Exception as e:
     print(e)
     return render(request, "categoryinterface.html", {'msg': 'Fail to Submit Record','records':request.session['admin']})


def DisplayAllCategories(request):
    try:
        admin=request.session['admin']
    except:
        return render(request,'AdminLogin.html', {'msg': ''})
    try:
        db,cmd=Pool.ConnectionPooling()
        q="select * from categories"
        cmd.execute(q)
        result=cmd.fetchall()
        db.close()
        return render(request,'DisplayAllCategories.html',{'result':result,'records':request.session['admin']})
    except Exception as e:
        print('xxxxxxxxxxxxx',e)
        return render(request, 'DisplayAllCategories.html', {'result':'', 'records': request.session['admin']})


def FillCategories(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        q="select * from categories"
        cmd.execute(q)
        result=cmd.fetchall()
        db.close()
        return JsonResponse({'result':result},safe=False)
    except Exception as e:
        print('xxxxxxxxxxxxx',e)
        return JsonResponse({'result':{}},safe=False)

def UpdateCategories(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        categoryid=request.GET['cid']
        categoryname=request.GET['cn']
        q="update categories set categoryname='{0}' where categoryid= {1} ".format(categoryname,categoryid)
        cmd.execute(q)
        db.commit()
        db.close()
        JsonResponse({'result':True},safe=False)
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>',e)
        JsonResponse({'result':False},safe=False)


def DeleteCategories(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        categoryid=request.GET['cid']
        q="delete from categories where categoryid= {0} ".format(categoryid)
        cmd.execute(q)
        db.commit()
        db.close()
        JsonResponse({'result':True},safe=False)
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>',e)
        JsonResponse({'result':False},safe=False)

def EditCategoryPicture(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        categoryid=request.POST['cid']
        categoryicon=request.FILES['icon']
        q="update categories set categoryicon='{0}' where categoryid= {1} ".format(categoryicon.name,categoryid)
        print('xxxxxxxxxxxxxx',q)
        cmd.execute(q)
        db.commit()
        F=open("D:/medassist_ecom/assets/inputicons/"+categoryicon.name, "wb")
        for chunk in categoryicon.chunks():
            F.write(chunk)
        F.close()
        db.close()
        JsonResponse({'result':True},safe=False)
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>',e)
        JsonResponse({'result':False},safe=False)
