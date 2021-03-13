$('.plus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    $.ajax({
        type: "GET",
        url: "/cart/plus_cart",
        data: {
            item_id:id
        },
        success: function (data) {
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total_amount").innerText = data.total_amount
            document.getElementById("discount").innerText=data.discount
        }
    })
});
$('.minus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    $.ajax({
        type: "GET",
        url: "/cart/minus_cart",
        data: {
            item_id:id
        },
        success: function (data) {
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total_amount").innerText = data.total_amount
            document.getElementById("discount").innerText=data.discount
        }
    })
});
$('.remove-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this
    $.ajax({
        type: "GET",
        url: "/cart/remove_cart",
        data: {
            item_id:id
        },
        success: function (data) {
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total_amount").innerText = data.total_amount
            document.getElementById("discount").innerText = data.discount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
});