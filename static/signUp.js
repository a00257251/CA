$(function() {
    $('#btnSignUp').click(function() {

        alert("hello")
        $.ajax({
            url: '/signUp',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response)
                //__redo__:'/view'
                //window.redirect('/')
              //  window.open("");
                window.location.href = "/login";
                alert('Wellcome');
                //if(response === 200) location.href = "Home.html"
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});