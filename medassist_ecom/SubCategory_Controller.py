from django.shortcuts import render,redirect
from . import Pool
from django.http import JsonResponse

def SubCategoryInterface(request):
    try:
        admin=request.session['admin']
        return render(request,'SubCategoryInterface.html',{'msg':'','records':request.session['admin']})
    except Exception as e:
        return render(request,'AdminLogin.html',{'msg':''})

def SubmitSubCategory(request):
   try:
     db,cmd=Pool.ConnectionPooling()
     categoryname=request.POST['categoryname']
     subcategoryname= request.POST['subcategoryname']
     subcategoryicon=request.FILES['subcategoryicon']
     q="insert into subcategories(categoryid,subcategoryname,subcategoryicon) values({0},'{1}','{2}')".format(int(categoryname),subcategoryname,subcategoryicon.name)
     print('>>>>>>>>>>>>>>>>>>>>',q)
     cmd.execute(q)
     db.commit()
     F=open("D:/medassist_ecom/assets/inputicons/"+subcategoryicon.name,"wb")
     for chunk in subcategoryicon.chunks():
        F.write(chunk)
     F.close()
     db.close()
     return render(request,"subcategoryinterface.html", {'msg': 'Submit Record','records':request.session['admin']})
   except Exception as e:
     print('>>>>>>>>>>>>>>>>>>>',e)
     return render(request, "subcategoryinterface.html", {'msg': 'Fail to Submit Record','records':request.session['admin']})

def DisplayAllSubCategories(request):
    try:
        admin=request.session['admin']
    except:
        return render(request,'AdminLogin.html', {'msg': ''})
    try:
        db,cmd=Pool.ConnectionPooling()
        q='select S.*,(select C.categoryname from categories C where C.categoryid=S.categoryid) as tc from subcategories S'
        cmd.execute(q)
        result=cmd.fetchall()
        print(result)
        db.close()
        return render(request,'DisplayAllSubCategories.html',{'result':result,'records':request.session['admin']})
    except Exception as e:
        print(e)
        return render(request,'DisplayAllSubCategories.html', {'result': {}, 'records': request.session['admin']})


def UpdateSubCategories(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        categoryid=request.GET['cn']
        subcategoryname=request.GET['scn']
        subcategoryid = request.GET['scid']
        q="update subcategories set categoryid={0},subcategoryname='{1}' where subcategoryid= {2} ".format(categoryid,subcategoryname,subcategoryid)
        cmd.execute(q)
        db.commit()
        db.close()
        JsonResponse({'result':True},safe=False)
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>',e)
        JsonResponse({'result':False},safe=False)


def DeleteSubCategories(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        subcategoryid = request.GET['scid']
        q="delete from subcategories where subcategoryid= {0} ".format(subcategoryid)
        cmd.execute(q)
        db.commit()
        db.close()
        JsonResponse({'result':True},safe=False)
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>',e)
        JsonResponse({'result':False},safe=False)

def EditSubCategoryPicture(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        subcategoryid=request.POST['subcategoryid']
        subcategoryicon=request.FILES['subcategoryicon']
        q="update subcategories set subcategoryicon='{1}' where subcategoryid= {0} ".format(subcategoryid,subcategoryicon.name)
        print('xxxxxxxxxxxxxxxxxxxxxxxxx',q)
        cmd.execute(q)
        db.commit()
        f=open('d:/medassist_ecom/assets/inputicons/'+subcategoryicon.name,'wb')
        for chunk in subcategoryicon.chunks():
            f.write(chunk)
        f.close()
        db.close()
        JsonResponse({'result':True},safe=False)
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>',e)
        JsonResponse({'result':False},safe=False)

def FillSubCategories(request):
  try:
    db, cmd = Pool.ConnectionPooling()
    categoryid=request.GET['categoryid']
    q="select * from subcategories where categoryid={0}".format(categoryid)
    cmd.execute(q)
    result = cmd.fetchall()
    db.close()
    return JsonResponse({'result': result}, safe=False)
  except Exception as e:
    print('xxxxxxxxxxxxx', e)
    return JsonResponse({'result': {}}, safe=False)

