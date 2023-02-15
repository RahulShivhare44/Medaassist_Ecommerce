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

    // Quantity Plus and Minu Button Manupialtion.......
    $(document).click(function(event){
        var blockid=event.target.id
        var tempid=blockid.slice(0,4)
        tempid=JSON.stringify(tempid)
        // alert(tempid)
        if(tempid.includes("plus")){
            // alert('hello')
                var p=$(this).attr('product')
                alert(p)
                // var v=p.qty
                // if (v<=4) {
                //     v++
                // }
                // var qtyid=blockid.slice(4,)
                // $('#'+qtyid).html(v)
                // cartContainer($(this).attr('product'),$('#'+qtyid).html())

        }
    })
    //  $('.minus').click(function(){
    //     var v=$('#qty').html()
    //     if(v>0){
    //         v--
    //     }
    //     if(v==0){
    //         $('.addtocart').show()
    //         $('#qtycomponent').hide()
    //         // alert($(this).attr('productid'))
    //         removeCartContainer($(this).attr('productid'))
    //     }
    //     if(v!=0){
    //         $('#qty').html(v)
    //         cartContainer($(this).attr('product'),$('#qty').html())
    //
    //     }
    // })
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
            location.href='http://localhost:8000/my_shopping_cart/'
        })
}
//..................................

// Remove the Product in the Cart
function removeCartContainer(productid,qty){
    // alert(qty)
    $.getJSON('/remove_from_cart',{'productid':productid},function (data){
                // alert(data.data)
                var cart=JSON.parse(data.data)
                var key=Object.keys(cart)
                $('#shoppingcart').html(`${key.length}`)
                location.href='http://localhost:8000/my_shopping_cart/'
            })

}
//......................................
