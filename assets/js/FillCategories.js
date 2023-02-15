$(document).ready(function (){

    $.getJSON('/fillcategory',function (data){
        data.result.map((item)=>{
            $('#categoryname').append($('<option>').text(item.categoryname).val(item.categoryid))
        })
    $('select').formSelect();
    })

$('#categoryname').change(function (){
    $('#subcategoryname').empty()
    $('#subcategoryname').append($('<option disabled selected>').text('Choose SubCategory'))
    $.getJSON('/fillsubcategory',{'categoryid':$('#categoryname').val()},function (data){
        data.result.map((item)=>{
            $('#subcategoryname').append($('<option>').text(item.subcategoryname).val(item.subcategoryid))
        })
    $('select').formSelect();
    })
})

$('#subcategoryname').change(function (){
    $('#brandname').empty()
    $('#brandname').append($('<option disabled selected>').text('Choose Brand'))
    $.getJSON('/fillbrand',{'categoryid':$('#categoryname').val(),'subcategoryid':$('#subcategoryname').val()},function (data){

        data.result.map((item)=>{
            $('#brandname').append($('<option>').text(item.brandname).val(item.brandid))
        })
    $('select').formSelect();
    })
})

$('#brandname').change(function (){
    $('#productname').empty()
    $('#productname').append($('<option disabled selected>').text('Choose Product'))
    $.getJSON('/fillproduct',{'categoryid':$('#categoryname').val(),'subcategoryid':$('#subcategoryname').val(),'brandid':$('#brandname').val()},function (data){

        data.result.map((item)=>{
            $('#productname').append($('<option>').text(item.productname).val(item.productid))
        })
    $('select').formSelect();
    })
})

})

