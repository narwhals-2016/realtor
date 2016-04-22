
$(document).ready(function(){
	console.log("Hi there!")

    $('.button-collapse').sideNav();
    $('.parallax').parallax();

///// Register /////
    $('.form_button').on('click', function(event){
    	event.preventDefault();
        var template = $('#form_template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);
    });

  //   $('#answer_div').on('submit', '#register_form',function(event){
  //   event.preventDefault();

  //   var query_string = $(this).serialize() // returns all the data in your form

  //   $.ajax({
  //       method: "POST",
  //       url: "register",
  //       data: query_string,
  //   }).done(function(data, status){

		// if (data.success){
		// 	////// if they registered then display the Login ////////
  //               var template = $('#login-template').html();
		//         var renderM = Mustache.render(template);
		//         $('#answer_div').html(renderM);
		//         $('#answer_div').append("<br><br>");
		//         $('#answer_div').append(data.Message);
  //           }
  //       });
  //   });


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
