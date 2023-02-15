$(document).ready(function (){

    // Add to Cart and Quantity Manupilation and With the help of this technique we read url....
    var hashes = window.location.href.slice(window.location.href.indexOf('?'));
     // alert(hashes)
    var i=hashes.indexOf(":")+1
    var j=hashes.indexOf(",")

    var pid=hashes.slice(i,j)
     // alert(pid)

    $.getJSON('/fetch_cart',function (data){
            var cart=JSON.parse(data.data)
            var key=Object.keys(cart)
            $('#shoppingcart').html(`${key.length}`)

            // alert(key.includes(pid))
            if(key.includes(pid)){
                $('.addtocart').hide()
                $('#qtycomponent').show()
                $('#qty').html(cart[pid]['qty'])
            }
            else{
                $('#qtycomponent').hide()
            }

    })

    //.......................................

    // Category Show in Navbar
    $.getJSON('/fetch_all_user_category',function (data){
        var htm=''
        data.result.map((item)=>{
            htm+=`<li><a href="#" style="color: #000000;font-weight: 600;display: flex;align-items: center"><img src="/static/inputicons/${item.categoryicon}" style="width: 34px;height: 34px">&nbsp;&nbsp;${item.categoryname}</a></li>`
        })
        $('.mainmenu').html(htm)
    })
    //......................................

   // Product Box.............................
   $.getJSON('/fetch_all_products',function (data){

     var  htm=''
    data.result.map((item)=>{

     var price
     var offerprice
     var save
     if(item.offerprice>0)
     {  price="<s style='color: red;'>"+item.price+"</s>"
        offerprice=item.offerprice
        save=item.price-item.offerprice
     }
     else {
         offerprice=item.price
         price="<div></div>"
         save="<div></div>"
     }

     htm+=`<a href='http://localhost:8000/buy_product?product=${JSON.stringify(item)}'>
            <div style="color: black;border-radius: 10px;margin: 10px;width: 260px;height: 330px;padding: 5px;display: flex;align-items: center;flex-direction: column;box-shadow: 0 4px 8px rgba(0,0,0,0.2);elevation: below;">
                <div>
                    <img src="/static/inputicons/${item.producticon}" style="width:150px;height: 150px" >
                </div>
                <div style="padding:5px;">
                    <div style="font-weight: bolder;text-align: left;width: 200px;">${item.productname} ${item.sn}</div>
                    <div style="font-size: 13px;text-align: left;width: 200px;">
                        <i>Mkt:${item.bn}</i>
                    </div>
                    <div style="font-weight: bolder;text-align: left;width: 200px;">
                        MRP: &#8377; ${price}
                    </div>
                    <div style="font-weight: bolder;text-align: left;width: 200px;">
                        Offer: &#8377; ${offerprice}
                    </div>
                    <div style="font-weight: 600;text-align: left;width: 200px;color: green">
                        You save &#8377; ${save}
                    </div>
                </div>    
         </div>
      </a>
        `
    })
        $('#productlist').html(htm)

    })
    //..................................................

    // SubCategory Show After Carousel..................
    $.getJSON('/fetch_all_subcategory',function (data){
        var htm=''
        data.result.map((item)=>{
            htm+=`<div style="margin: 5px;padding: 10px;width: 230px;background: rgba(211,211,211,0.32);height: 110px;border-radius: 10px;display: flex;flex-direction: row;box-shadow: 2px 2px #ecf0f1;elevation: below;">
                    <span style="padding: 5px"><img src="/static/inputicons/${item.subcategoryicon}" width="75" ></span>
                    <div style="display: flex;flex-direction: column;margin-top: 6px;" ><div style="padding: 5px;font-weight: bolder">${item.subcategoryname}</div><div style="color: #0f9d58" >Save upto 15%</div></div>   
                  </div>`
        })
        $('#subcategorylist').html(htm)
    })
    //..................................................

    // Add to Cart......................................
    $('.addtocart').click(function (){
        $('.addtocart').hide()
        $('#qtycomponent').show()
        $('#qty').html(1)
        product=$(this).attr('product')
        cartContainer($(this).attr('product'),$('#qty').html())
    })
    //..................................................

    // Quantity Plus and Minu Button Manupialtion.......
    $('.plus').click(function(){
        var v=$('#qty').html()
        if(v<=4){
            v++
        }
        $('#qty').html(v)
       cartContainer($(this).attr('product'),$('#qty').html())
    })

     $('.minus').click(function(){
        var v=$('#qty').html()
        if(v>0){
            v--
        }
        if(v==0){
            $('.addtocart').show()
            $('#qtycomponent').hide()
            // alert($(this).attr('productid'))
            removeCartContainer($(this).attr('productid'))
        }
        if(v!=0){
            $('#qty').html(v)
            cartContainer($(this).attr('product'),$('#qty').html())
        }
    })
    //..................................................

})

// Add the Product in the Add to Cart
function cartContainer(product1,qty){
    // alert(product1)
     $.getJSON('/add_to_cart',{'product':product1,'qty':qty},function (data){
            // alert(data.data)
            var cart=JSON.parse(data.data)
            var key=Object.keys(cart)
            $('#shoppingcart').html(`${key.length}`)
        })

}
//..................................

// Remove the Product in the Cart
function removeCartContainer(productid,qty){

    $.getJSON('/remove_from_cart',{'productid':productid},function (data){
                // alert(data.data)
                var cart=JSON.parse(data.data)
                var key=Object.keys(cart)
                $('#shoppingcart').html(`${key.length}`)

            })

}
//......................................
