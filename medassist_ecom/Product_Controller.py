from django.shortcuts import render,redirect
from . import Pool
from django.http import JsonResponse


def ProductInterface(request):
    try:
     return render(request,'ProductInterface.html',{'msg':'','records':request.session['admin']})
    except:
     return render(request, 'AdminLogin.html', {'msg': ''})

def SubmitProduct(request):
   try:
     db,cmd=Pool.ConnectionPooling()
     categoryid=request.POST['categoryname']
     subcategoryid=request.POST['subcategoryname']
     brandid=request.POST['brandname']
     productname=request.POST['productname']
     price=request.POST['price']
     offerprice=request.POST['offerprice']
     packingtype=request.POST['packingtype']
     qty=request.POST['qty']
     status=request.POST['status']
     salestatus=request.POST['salestatus']
     rating=request.POST['rating']
     producticon=request.FILES['producticon']

     q="insert into product(categoryid,subcategoryid,brandid,productname,price,offerprice,packingtype,qty,status,salestatus,rating,producticon) values({0},{1},{2},'{3}',{4},{5},'{6}',{7},'{8}','{9}','{10}','{11}')".format(categoryid,subcategoryid,brandid,productname,price,offerprice,packingtype,qty,status,salestatus,rating,producticon.name)
     cmd.execute(q)
     db.commit()
     F=open("D:/medassist_ecom/assets/inputicons/"+producticon.name,"wb")
     for chunk in producticon.chunks():
        F.write(chunk)
     F.close()
     db.close()
     return render(request,'ProductInterface.html',{'msg':'Record Submitted','records':request.session['admin']})
   except Exception as e:
     print('>>>>>>>>>>>>>>>>>>>',e)
     return render(request,'ProductInterface.html',{'msg':'Fail to Submit Record','records':request.session['admin']})


def DisplayAllProduct(request):
  try:
    admin = request.session['admin']
  except:
    return render(request, 'AdminLogin.html', {'msg': ''})
  try:
    db,cmd=Pool.ConnectionPooling()
    q='select P.*,(select C.categoryname from categories C where C.categoryid=P.categoryid) as cn,(select S.subcategoryname from subcategories S where S.subcategoryid=P.subcategoryid) as sn,(select B.brandname from brand B where B.brandid=P.brandid) as bn from product P'
    cmd.execute(q)
    result=cmd.fetchall()
    print(result)
    db.close()
    return render(request, 'DisplayAllProduct.html',{'result': result,'records':request.session['admin']})
  except Exception as e:
    print(e)
    return render(request, 'DisplayAllProduct.html', {'result': {},'records':request.session['admin']})


def UpdateProduct(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        categoryid=request.GET['categoryid']
        subcategoryid=request.GET['subcategoryid']
        brandid=request.GET['brandid']
        productname=request.GET['productname']
        price=request.GET['price']
        offerprice=request.GET['offerprice']
        packingtype=request.GET['packingtype']
        qty=request.GET['qty']
        status=request.GET['status']
        salestatus=request.GET['salestatus']
        rating=request.GET['rating']
        productid=request.GET['productid']

        q="update product set categoryid={0},subcategoryid={1},brandid={2},productname='{3}',price={4},offerprice={5},packingtype='{6}',qty={7},status='{8}',salestatus='{9}',rating='{10}' where productid={11} ".format(categoryid,subcategoryid,brandid,productname,price,offerprice,packingtype,qty,status,salestatus,rating,productid)
        print(q)
        cmd.execute(q)
        db.commit()
        db.close()
        JsonResponse({'result':True})
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>',e)
        JsonResponse({'result':False})


def DeleteProduct(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        productid=request.GET['productid']
        q="delete from product where productid= {0} ".format(productid)
        cmd.execute(q)
        db.commit()
        db.close()
        JsonResponse({'result':True},safe=False)
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>',e)
        JsonResponse({'result':False},safe=False)


def EditProductPicture(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        productid=request.POST['productid']
        producticon=request.FILES['producticon']
        q="update product set producticon='{1}' where productid={0}".format(productid,producticon.name)
        print('xxxxxxxxxxxxxxxxxxxxxxxxx',q)
        cmd.execute(q)
        db.commit()
        f=open('d:/medassist_ecom/assets/inputicons/'+producticon.name,'wb')
        for chunk in producticon.chunks():
            f.write(chunk)
        f.close()
        db.close()
        JsonResponse({'result':True},safe=False)
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>',e)
        JsonResponse({'result':False},safe=False)

def MultipleProductImages(request):
    try:
        return render(request,'MultipleProductsImages.html',{'msg': '', 'records': request.session['admin']})
    except:
        return render(request, 'AdminLogin.html', {'msg': ''})

def SubmitMultiProductImages(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        categoryid=request.POST['categoryid']
        subcategoryid=request.POST['subcategoryid']
        brandid=request.POST['brandid']
        productid=request.POST['productid']
        icon=request.FILES['producticon']
        q="insert into picture(categoryid,subcategoryid,brandid,productid,image) values({0},{1},{2},{3},'{4}')".format(categoryid,subcategoryid,brandid,productid,icon.name)
        cmd.execute(q)
        db.commit()
        f=open('d:/medassist_ecom/assets/inputicons/'+icon.name,'wb')
        for chunk in icon.chunks():
            f.write(chunk)
        f.close()
        db.close()
        return render(request,'MultipleProductsImages.html',{'msg':'Record Submitted','records': request.session['admin']})
    except Exception as e:
        print(e)
        return render(request, 'MultipleProductsImages.html', {'msg': 'Fail to Record Submit','records': request.session['admin']})

def FillProduct(request):
    try:
     db,cmd=Pool.ConnectionPooling()
     categoryid=request.GET['categoryid']
     subcategoryid=request.GET['subcategoryid']
     brandid=request.GET['brandid']
     q='select * from product where categoryid={0} and subcategoryid={1} and brandid={2}'.format(categoryid,subcategoryid,brandid)
     print('>>>>>>>>>>>>>>>>>>>',q)
     cmd.execute(q)
     record=cmd.fetchall()
     db.close()
     return JsonResponse({'result':record},safe=False)
    except Exception as e:
     print('xxxxxxxxxxxxxxxxxxxx',e)
     return JsonResponse({'result':{}},safe=False)
