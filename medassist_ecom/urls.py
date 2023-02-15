"""medassist_ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import Category_Controller
from . import SubCategory_Controller
from . import AdminLogin
from . import Brand_Controller
from . import Product_Controller
from . import UserInterface

urlpatterns = [
    path('admin/', admin.site.urls),

    #Category Panel........................
    path('categoryinterface/', Category_Controller.CategoryInterface),
    path('submitcategory', Category_Controller.SubmitCategory),
    path('displayallcategory/', Category_Controller.DisplayAllCategories),
    path('fillcategory/', Category_Controller.FillCategories),
    path('updatecategory/', Category_Controller.UpdateCategories),
    path('deletecategory/', Category_Controller.DeleteCategories),
    path('editcategorypicture', Category_Controller.EditCategoryPicture),

    # SubCategory Panel........................
    path('subcategoryinterface/', SubCategory_Controller.SubCategoryInterface),
    path('submitsubcategory', SubCategory_Controller.SubmitSubCategory),
    path('displayallsubcategory/', SubCategory_Controller.DisplayAllSubCategories),
    path('updatesubcategory/',SubCategory_Controller.UpdateSubCategories),
    path('deletesubcategory/',SubCategory_Controller.DeleteSubCategories),
    path('editsubcategorypicture',SubCategory_Controller.EditSubCategoryPicture),
    path('fillsubcategory/',SubCategory_Controller.FillSubCategories),

    #Brand Panel..............................
    path('brandinterface/',Brand_Controller.BrandInterface),
    path('submitbrand',Brand_Controller.SubmitBrand),
    path('displayallbrand/',Brand_Controller.DisplayAllBrand),
    path('updatebrand/', Brand_Controller.UpdateBrand),
    path('deletebrand/', Brand_Controller.DeleteBrand),
    path('editbrandpicture',Brand_Controller.EditBrandPicture),
    path('fillbrand/',Brand_Controller.FillBrand),

    #Product..............................
    path('productinterface/', Product_Controller.ProductInterface),
    path('submitproduct', Product_Controller.SubmitProduct),
    path('displayallproduct/',Product_Controller.DisplayAllProduct),
    path('updateproduct/',Product_Controller.UpdateProduct),
    path('deleteproduct/',Product_Controller.DeleteProduct),
    path('editproductpicture',Product_Controller.EditProductPicture),
    path('multipleproductimages/',Product_Controller.MultipleProductImages),
    path('submitmultiproductimages',Product_Controller.SubmitMultiProductImages),
    path('fillproduct/',Product_Controller.FillProduct),

    #Admin Panel...........................
    path('adminlogin/', AdminLogin.AdminLogin),
    path('dashboard', AdminLogin.CheckAdminLogin),
    path('home/', AdminLogin.Home),
    path('logoutadmin/', AdminLogin.LogoutAdmin),

    #UserInterface..........................
    path('userinterface/',UserInterface.Index),
    path('fetch_all_user_category/',UserInterface.FillCategories),
    path('fetch_all_products/',UserInterface.Fetch_All_Product),
    path('fetch_all_subcategory/',UserInterface.FillSubCategories),
    path('buy_product/',UserInterface.Buy_Product),
    path('add_to_cart/',UserInterface.AddToCart),
    path('fetch_cart/',UserInterface.FetchCart),
    path('remove_from_cart/',UserInterface.RemoveFromCart),
    path('my_shopping_cart/',UserInterface.MyShoppingCart),
    path('signinandsignup/',UserInterface.SignInAndSignUp),
    path('checksignin/',UserInterface.CheckSignIn),
    path('userregistration/',UserInterface.UserRegistration),
    path('logout/',UserInterface.Logout),
    path('checklogin/', UserInterface.CheckLogin),
    path('useraddress/', UserInterface.InsertUserAddress),
    path('updateuseraddress/', UserInterface.UpdateUserAddress),
    path('checkout/', UserInterface.CheckOut),

]
