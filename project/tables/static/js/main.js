
$(document).ready(function(){
	console.log("Hi there!")

    $('.button-collapse').sideNav();
    $('.parallax').parallax();

///// Register /////
    $('#nav').on('click', "#register", function(event){
      event.preventDefault();
        var template = $('#register-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);
    });

    $('#answer_div').on('submit', '#register_form',function(event){
    event.preventDefault();

    var query_string = $(this).serialize() // returns all the data in your form

    $.ajax({
        method: "POST",
        url: "register",
        data: query_string,
    }).done(function(data, status){
    // console.log("submitted")

    if (data.success){
      ////// if they registered then display the Login ////////
            var template = $('#login-template').html();
            var renderM = Mustache.render(template);
            $('#answer_div').html(renderM);
            $('#answer_div').append("<br><br>");
            $('#answer_div').append(data.Message);
            }
        });
    });


// ///// Login /////
    $('#nav').on('click', "#login", function(event){
      event.preventDefault();
        var template = $('#login-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);
    });

    // $('#answer_div').on('submit', '#login_form',function(event){
    // event.preventDefault();

    // var query_string = $(this).serialize() // returns all the data in your form

    // $.ajax({
    //     method: "POST",
    //     url: "login",
    //     data: query_string,
    // }).done(function(data, status){

    //     $('#answer_div').html(data.Message);
    //     $('#answer_div').append("<br><br>");
    //     $('#nav').append(data.username);

    //     });
    // });

///// Logout /////
//     $('#nav').on('click', "#logout", function(event){
//     event.preventDefault();

//     // var query_string = $(this).serialize() // returns all the data in your form

//     $.ajax({
//         method: "POST",
//         url: "logout",
//         // data: query_string,
//     }).done(function(data, status){

//     $('#answer_div').html(" <h2> Goodbye, See you soon!</h2>");
//     $('#answer_div').append(data.Message);
//   location.reload();

//     });
// });



///// Form /////
    $('.form_button').on('click', function(event){
    	event.preventDefault();
        var template = $('#form_template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);
    });

///// Form - Education toggle/////
    $("#answer_div").on('click', 'input[name="CHECKBOX"]',function(event){
        var $is_checked = $(this).is(':checked')

        if ($is_checked === true) {
          // display current_edu_level
          $("#highest_edu_level").css("display", "none");
          $("#current_edu_level").css("display", "block");
        } else {
          // display highest_edu_level
          $("#highest_edu_level").css("display", "block");
          $("#current_edu_level").css("display", "none");
        };
    });


});
