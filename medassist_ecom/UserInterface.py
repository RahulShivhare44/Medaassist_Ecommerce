from django.shortcuts import render
from django.http import JsonResponse
from . import Pool
import json
from urllib.parse import unquote
import random

def SignInAndSignUp(request):
    return render(request,'SigninAndSigup.html')

def CheckSignIn(request):
    try:
        mobileno=request.GET['mobileno']
        db,cmd=Pool.ConnectionPooling()
        q1="select * from userregistration where mobileno={}".format(mobileno)
        cmd.execute(q1)
        result=cmd.fetchone()
        request.session['userdata']=result

        q2="select * from users_address where mobileno={}".format(mobileno)
        cmd.execute(q2)
        useraddress=cmd.fetchone()
        request.session['useraddress']=useraddress

        if(result):
            otp=random.randint(1000,9999)
            print('Your OTP is:',otp)
            return JsonResponse({'result':True,'otp':otp},safe=False)
        else:
            return JsonResponse({'result': False,'otp':''}, safe=False)
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>>>',e)
        return JsonResponse({'result': False,'otp':''}, safe=False)

def UserRegistration(request):
    try:
        name=request.GET['name']
        email=request.GET['email']
        mobileno=request.GET['mobileno']

        db,cmd=Pool.ConnectionPooling()
        q="insert into userregistration(username,useremail,mobileno) values('{0}','{1}','{2}')".format(name,email,mobileno)

        request.session['userdata']={'username':name,'useremail':email,'mobileno':mobileno}

        cmd.execute(q)
        db.commit()
        db.close()
        return JsonResponse({'result':True,'userdata':''},safe=False)
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>>>',e)
        return JsonResponse({'result': False,'userdata':''}, safe=False)

def Logout(request):
    try:
        del request.session['userdata']
    except:
        pass
    try:
        del request.session['useraddress']
    except:
        pass
    userdata=''
    return render(request,"Index.html", {'userdata': userdata})

def CheckLogin(request):
    try:
        userdata = request.session['userdata']
    except Exception as e:
        userdata=''
    if(userdata!=''):
        return JsonResponse({'result':True,'userdata':userdata}, safe=False)
    else:
        return JsonResponse({'result':False}, safe=False)

def InsertUserAddress(request):
    try:
        mobileno=request.GET['mobileno']
        emailid=request.GET['emailid']
        addresslineone=request.GET['addresslineone']
        addresslinetwo=request.GET['addresslinetwo']
        city=request.GET['city']
        state=request.GET['state']
        landmark=request.GET['landmark']
        zipcode=request.GET['zipcode']

        db,cmd=Pool.ConnectionPooling()
        q="insert into users_address(mobileno,emailid,address1,address2,landmark,city,state,zipcode) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(mobileno,emailid,addresslineone,addresslinetwo,landmark,city,state,zipcode)

        request.session['useraddress']={'mobileno':mobileno,'emailid':emailid,'address1':addresslineone,'address2':addresslinetwo,'landmark':landmark,'city':city,'state':state,'zipcode':zipcode}
        print('USERDATA:',request.session['useraddress'])

        cmd.execute(q)
        db.commit()
        db.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>>>',e)
        return JsonResponse({'result': False}, safe=False)

def UpdateUserAddress(request):
    try:
        mobileno=request.GET['mobileno']
        emailid=request.GET['emailid']
        addresslineone=request.GET['address1']
        addresslinetwo=request.GET['address2']
        city=request.GET['city']
        state=request.GET['state']
        landmark=request.GET['landmark']
        zipcode=request.GET['zipcode']

        db,cmd=Pool.ConnectionPooling()
        q="update users_address set emailid='{0}',address1='{1}',address2='{2}',landmark='{3}',city='{4}',state='{5}',zipcode='{6}' where mobileno='{7}' ".format(emailid,addresslineone,addresslinetwo,landmark,city,state,zipcode,mobileno)
        updateaddress=request.session['useraddress']
        updateaddress['mobileno']=mobileno
        updateaddress['emailid']=emailid
        updateaddress['address1']=addresslineone
        updateaddress['address2']=addresslinetwo
        updateaddress['landmark']=landmark
        updateaddress['city']=city
        updateaddress['state']=state
        updateaddress['zipcode']=zipcode
        request.session['useraddress']=updateaddress

        cmd.execute(q)
        db.commit()
        db.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as e:
        print('>>>>>>>>>>>>>>>>>>>>',e)
        return JsonResponse({'result': False}, safe=False)

def CheckOut(request):
    try:
        try:
            CART_CONTAINER = request.session['CART_CONTAINER']
            total = 0
            totalprice = 0
            totalsavings = 0
            for key in CART_CONTAINER.keys():
                # print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',key,CART_CONTAINER[key]['price'])
                CART_CONTAINER[key]['save']=(int(CART_CONTAINER[key]['price'])-int(CART_CONTAINER[key]['offerprice'])) * int(CART_CONTAINER[key]['qty'])
                CART_CONTAINER[key]['productprice']=int(CART_CONTAINER[key]['offerprice'])*int(CART_CONTAINER[key]['qty'])
                totalsavings += CART_CONTAINER[key]['save']
                amt = int(CART_CONTAINER[key]['offerprice'])*int(CART_CONTAINER[key]['qty'])
                total+=amt
                totalprice+=int(CART_CONTAINER[key]['price']) * int(CART_CONTAINER[key]['qty'])
        except Exception as err:
            print('Error:', err)
            CART_CONTAINER = {}

        try:
            userdata = request.session['userdata']
        except Exception as e:
            print('User Data:', e)
            userdata = ''

        return render(request, "CheckOut.html",{'data':CART_CONTAINER.values(),'totalproducts':len(CART_CONTAINER),'totalamount':total,'totalprice':totalprice,'totalsavings': totalsavings,'userdata': userdata})
    except Exception as e:
        print('xxxxxxxxxxxxxxx', e)
        return render(request, "CheckOut.html",{'data': []})


def MyShoppingCart(request):
    try:
        try:
           CART_CONTAINER=request.session['CART_CONTAINER']

           total=0
           totalprice=0
           totalsavings=0
           for key in CART_CONTAINER.keys():
               # print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',key,CART_CONTAINER[key]['price'])
               CART_CONTAINER[key]['save'] = (int(CART_CONTAINER[key]['price'])-int(CART_CONTAINER[key]['offerprice']))*int(CART_CONTAINER[key]['qty'])
               CART_CONTAINER[key]['productprice'] = int(CART_CONTAINER[key]['offerprice'])*int(CART_CONTAINER[key]['qty'])
               totalsavings += CART_CONTAINER[key]['save']
               amt = int(CART_CONTAINER[key]['offerprice']) * int(CART_CONTAINER[key]['qty'])
               total+=amt
               totalprice+=int(CART_CONTAINER[key]['price'])*int(CART_CONTAINER[key]['qty'])


        except Exception as err:
            print('Error:',err)
            CART_CONTAINER={}
        print('My Shopping Cart:',CART_CONTAINER.values())

        try:
            userdata=request.session['userdata']
        except Exception as e:
            print('User Data:',e)
            userdata=''
        print('Userdata:',userdata)

        try:
            useraddress=request.session['useraddress']
        except Exception as e:
            print('User Address:',e)
            useraddress='None'
        print('UserAddress:',useraddress)

        return render(request, "MyCart.html",{'data':CART_CONTAINER.values(),'totalproducts':len(CART_CONTAINER),'totalamount':total,'totalprice':totalprice,'totalsavings':totalsavings,'userdata':userdata,'useraddress':useraddress})
    except Exception as e:
        print('xxxxxxxxxxxxxxx',e)
        return render(request, "MyCart.html",{'data':[]})

def AddToCart(request):
    try:
        product=request.GET['product']
        qty=request.GET['qty']
        product=product.replace("'","\"")
        product=json.loads(product)
        product['qty']=qty
        print('UPDATED PRODUCTS:',type(product))

        # Create Cart Container Using Session
        try:
           CART_CONTAINER=request.session['CART_CONTAINER']
           CART_CONTAINER[str(product['productid'])]=product
           request.session['CART_CONTAINER'] = CART_CONTAINER
        except:
            # CART_CONTAINER={product['productid']:product}
            CART_CONTAINER={}
            CART_CONTAINER[str(product['productid'])]=product
            request.session['CART_CONTAINER']=CART_CONTAINER
            print("Error")

        print('CART_CONTAINER:',CART_CONTAINER)
        CART_CONTAINER = str(CART_CONTAINER).replace("'","\"")

        return JsonResponse({'data':CART_CONTAINER},safe=False)
    except Exception as e:
        print('xxxxxxxxxxxxxxx',e)
        return JsonResponse({'data': []}, safe=False)

def FetchCart(request):
    try:
        # Create Cart Container Using Session
        try:
           CART_CONTAINER=request.session['CART_CONTAINER']
        except:
            CART_CONTAINER={}

        print('CART_CONTAINER:',CART_CONTAINER)
        CART_CONTAINER = str(CART_CONTAINER).replace("'","\"")

        return JsonResponse({'data':CART_CONTAINER},safe=False)
    except Exception as e:
        print('xxxxxxxxxxxxxxx',e)
        return JsonResponse({'data': []}, safe=False)

def RemoveFromCart(request):
    try:
       productid = request.GET['productid']
       CART_CONTAINER=request.session['CART_CONTAINER']
       del CART_CONTAINER[str(productid)]
       request.session["CART_CONTAINER"]=CART_CONTAINER
       print("CART_CONTAINER->>>>>>>>>>>>>>>>>>>>>>>>",request.session['CART_CONTAINER'])
       CART_CONTAINER = str(CART_CONTAINER).replace("'", "\"")
       return JsonResponse({'data': CART_CONTAINER}, safe=False)
    except Exception as err:
        print("ERRORRRRR:",err)
        return JsonResponse({'data': []}, safe=False)


def Index(request):
    try:
        userdata = request.session['userdata']
    except Exception as e:
        print('User Data', e)
        userdata = ''

    return render(request,"Index.html",{'userdata':userdata})

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

def Fetch_All_Product(request):
  try:
    db,cmd=Pool.ConnectionPooling()
    q='select P.*,(select C.categoryname from categories C where C.categoryid=P.categoryid) as cn,(select S.subcategoryname from subcategories S where S.subcategoryid=P.subcategoryid) as sn,(select B.brandname from brand B where B.brandid=P.brandid) as bn from product P'
    cmd.execute(q)
    result=cmd.fetchall()
    # print(result)
    db.close()
    return JsonResponse({'result':result},safe=False)
  except Exception as e:
    print(e)
    return JsonResponse({'result':{}},safe=False)

def FillSubCategories(request):
  try:
    db, cmd = Pool.ConnectionPooling()
    q="select * from subcategories"
    cmd.execute(q)
    result = cmd.fetchall()
    db.close()
    return JsonResponse({'result': result}, safe=False)
  except Exception as e:
    print('xxxxxxxxxxxxx', e)
    return JsonResponse({'result': {}}, safe=False)

def Buy_Product(request):
    product = unquote(request.GET['product'])
    product = json.loads(product)
    print("zzzzzzzzzzzzz", product)

    try:
        userdata = request.session['userdata']
    except Exception as e:
        print('User Data', e)
        userdata = ''
    db,cmd=Pool.ConnectionPooling()
    q='select * from picture where productid={0}'.format(product['productid'])
    cmd.execute(q)
    picture=cmd.fetchall()

    return render(request,"Buy_product.html",{'product':product,'pictures':picture,'userdata':userdata})

