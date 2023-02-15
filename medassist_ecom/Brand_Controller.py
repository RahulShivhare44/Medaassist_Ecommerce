from django.shortcuts import render,redirect
from . import Pool
from django.http import JsonResponse


def BrandInterface(request):
    try:
     admin = request.session['admin']
     return render(request,'BrandInterface.html',{'msg':'','records':request.session['admin']})
    except:
        return render(request, 'AdminLogin.html', {'msg': ''})

def SubmitBrand(request):
   try:
     db,cmd=Pool.ConnectionPooling()
     categoryname=request.POST['categoryname']
     subcategoryname=request.POST['subcategoryname']
     brandname=request.POST['brandname']
     contactperson=request.POST['contactperson']
     mobileno=request.POST['mobileno']
     brandicon=request.FILES['brandicon']
     status=request.POST['status']
     q="insert into brand(categoryid,subcategoryid,brandname,contactperson,mobileno,brandicon,status) values({0},{1},'{2}','{3}','{4}','{5}','{6}')".format(categoryname,subcategoryname,brandname,contactperson,mobileno,brandicon.name,status)
     print('>>>>>>>>>>>>>>>>>>>>',q)
     cmd.execute(q)
     db.commit()
     F=open("D:/medassist_ecom/assets/inputicons/"+brandicon.name,"wb")
     for chunk in brandicon.chunks():
        F.write(chunk)
     F.close()
     db.close()
     return render(request,"BrandInterface.html", {'msg':'Submit Record','records':request.session['admin']})
   except Exception as e:
     print('>>>>>>>>>>>>>>>>>>>',e)
     return render(request,"BrandInterface.html", {'msg':'Fail to Submit Record','records':request.session['admin']})

def DisplayAllBrand(request):
  try:
   admin = request.session['admin']
  except:
   return render(request, 'AdminLogin.html', {'msg': ''})
  try:
    db,cmd=Pool.ConnectionPooling()
    q='select B.*,(select C.categoryname from categories C where C.categoryid=B.categoryid) as cn,(select S.subcategoryname from subcategories S where S.subcategoryid=B.subcategoryid) as sn from brand B'
    cmd.execute(q)
    result=cmd.fetchall()
    print(result)
    db.close()
    return render(request, 'DisplayAllBrand.html',{'result': result,'records':request.session['admin']})
  except Exception as e:
    print(e)
    return render(request, 'DisplayAllSubCategories.html', {'result': {},'records':request.session['admin']})


def UpdateBrand(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        brandid=request.GET['brandid']
        categoryid=request.GET['categoryid']
        subcategoryid=request.GET['subcategoryid']
        brandname=request.GET['brandname']
        contactperson=request.GET['contactperson']
        mobileno=request.GET['mobileno']
        status=request.GET['status']
        q="update brand set categoryid={0},subcategoryid={1},brandname='{2}',contactperson='{3}',mobileno='{4}',status='{5}' where brandid= {6} ".format(categoryid,subcategoryid,brandname,contactperson,mobileno,status,brandid)
        cmd.execute(q)
        db.commit()
        db.close()
        JsonResponse({'result':True},safe=False)
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>',e)
        JsonResponse({'result':False},safe=False)


def DeleteBrand(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        brandid=request.GET['brandid']
        q="delete from brand where brandid= {0} ".format(brandid)
        cmd.execute(q)
        db.commit()
        db.close()
        JsonResponse({'result':True},safe=False)
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>',e)
        JsonResponse({'result':False},safe=False)


def EditBrandPicture(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        brandid=request.POST['brandid']
        brandicon=request.FILES['brandicon']
        q="update brand set brandicon='{1}' where brandid= {0} ".format(brandid,brandicon.name)
        print('xxxxxxxxxxxxxxxxxxxxxxxxx',q)
        cmd.execute(q)
        db.commit()
        f=open('d:/medassist_ecom/assets/inputicons/'+brandicon.name,'wb')
        for chunk in brandicon.chunks():
            f.write(chunk)
        f.close()
        db.close()
        JsonResponse({'result':True},safe=False)
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>',e)
        JsonResponse({'result':False},safe=False)

def FillBrand(request):
    try:
     db,cmd=Pool.ConnectionPooling()
     categoryid=request.GET['categoryid']
     subcategoryid=request.GET['subcategoryid']
     q='select * from brand where categoryid={0} and subcategoryid={1}'.format(categoryid,subcategoryid)
     print('>>>>>>>>>>>>>>>>>>>',q)
     cmd.execute(q)
     record=cmd.fetchall()
     db.close()
     return JsonResponse({'result':record},safe=False)
    except Exception as e:
     print('xxxxxxxxxxxxxxxxxxxx',e)
     return JsonResponse({'result':{}},safe=False)
