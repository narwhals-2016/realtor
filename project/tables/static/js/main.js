
$(document).ready(function(){
	console.log("Hi there!")

    $('.button-collapse').sideNav();
    $('.parallax').parallax();
    $('.carousel').carousel();
    $('.slider').slider();


// window.onhashchange = function (e) {
//     if (window.location.hash === "#" || window.location.hash === "") {
//         calendar_view.show();
//         event_form_view.hide();
//     } else if (window.location.hash === "#form") {
//         calendar_view.hide();
//         event_form_view.show();
//     }
// };


///// Register /////
    $('#nav').on('click', "#register", function(event){
      event.preventDefault();
        var template = $('#register-template').html();
        var renderM = Mustache.render(template, {});
        $('#answer_div').html(renderM);
        window.scrollTo(0, 0);
    });

    $('#answer_div').on('submit', '#register_form',function(event){
    event.preventDefault();

    var query_string = $(this).serialize() // returns all the data in your form

    $.ajax({
        method: "POST",
        url: "register",
        data: query_string,
    }).done(function(data, status){
    // console.log(data.Message)

    if (data.success){
      ////// if they registered then display the Login ////////
            var template = $('#login-template').html();
            var renderM = Mustache.render(template);
            $('#answer_div').html(renderM);
            window.scrollTo(0, 0);
            // $('#answer_div').append(data.Message);
            }
      else {
        // console.log (data.errors)
        var template = $('#register-template').html();
        var renderM = Mustache.render(template, data.errors);
        $('#answer_div').html(renderM);
        window.scrollTo(0, 0);
      }

        });
    });


/////// Login /////
    $('#nav').on('click', "#login", function(event){
      event.preventDefault();
        var template = $('#login-template').html();
        var renderM = Mustache.render(template, {'id_username':'account_circle','id_password':'verified_user'});
        $('#answer_div').html(renderM);
        window.scrollTo(0, 0);
    });

    $('#answer_div').on('submit', '#login_form',function(event){
      event.preventDefault();
      console.log("clicked login")

      var query_string = $(this).serialize() //returns all the data in your form
      // console.log(query_string)

      $.ajax({
          method: "POST",
          url: "login",
          data: query_string,
      }).done(function(data, status){

          if (data.success){
          ////// if they login correctly ////////
            console.log("HERE")
            document.location.href="/";
            window.scrollTo(0, 0);
          } 
          else{
            // crazy code to select for the error formating
            var template = $('#login-template').html();
            var errorNames = Object.keys(data.errors).reduce(function(previousValue, currentValue, currentIndex, array){
              return (previousValue ? previousValue + ',':'') + 'input[name="'+currentValue+'"]'
            }, '');
            var renderM = Mustache.render(template, $.extend(data.errors,{'id_username':'account_circle','id_password':'verified_user'}));
            $('#answer_div').html(renderM);

            var inputs = $('#login_form').find(errorNames);
            inputs.addClass('invalid');
            $.each(inputs, function(idx, el){
              $($(el).next()).css("white-space", "nowrap");
              $($(el).next()).css("overflow", "hidden;");
            });

            // prints errors that are not missing fields to the end of the form
            $('.tall .container').append(data.errors["__all__"][0]);
            $('.tall .container').css("color", "red");

            window.scrollTo(0, 0);
          }

      });
    });

///// Logout /////
    $('#nav').on('click', "#logout", function(event){
    event.preventDefault();

    // var query_string = $(this).serialize() // returns all the data in your form

    $.ajax({
        method: "POST",
        url: "logout",
        // data: query_string,
    }).done(function(data, status){

    // $('#answer_div').html(" <h2> Goodbye, See you soon!</h2>");
    document.location.href="/";
    window.scrollTo(0, 0);

    });
});


///// Form /////
    $('.form_button').on('click', function(event){
    	event.preventDefault();
        var template = $('#form_template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);
        window.scrollTo(0, 0);
    });

    $('#answer_div').on('submit', '#search_form',function(event){
    event.preventDefault();

    var query_string = $(this).serialize() //returns all the data in your form
    console.log(query_string)

    $.ajax({
        method: "POST",
        url: "search",
        data: query_string,
    }).done(function(data, status){

    if (data.success){
        ////// if submit form correctly ////////
        $('#ja_search').addClass("hide");
          console.log("HERE")

          var template = $('#results-template').html();
          var renderM = Mustache.render(template);
          $('#answer_div').append(renderM);
          window.scrollTo(0, 0);
          }

        });
    });


///// Back Button /////
    $('#answer_div').on('click', '#back_button',function(event){
      event.preventDefault();
        $('#ja_search').attr("class","show");
        $('#ja_results').addClass("hide");
        console.log("DONE!")
    });



///// Form - Education toggle/////
    $("#answer_div").on('click', 'input[id="CHECKBOX"]',function(event){
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


///// Form - Price Range Adjuster/////
    $("#answer_div").on('click', 'input[id="purchase"]',function(event){
        var $is_checked = $(this).is(':checked')

        // purchase //
        if ($is_checked === true) {
          $(price_range_title).html("Price Range (in thousands)")
          $("#price_range").attr("min","250");
          $("#price_range").attr("max","2000");
        };
    });

    $("#answer_div").on('click', 'input[id="rent"]',function(event){
        var $is_checked = $(this).is(':checked')

        // rent //
        if ($is_checked === true) {
          $(price_range_title).html("Price Range")
          $("#price_range").attr("min","500");
          $("#price_range").attr("max","2000");
        };
    });

});
