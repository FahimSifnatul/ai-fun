const menu_list  = ["image_to_text", "roots_of_polynomial_eq"];

// custom delay function
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function SET(selected_menu)
{
	// To hide all menu contents except the selected one
	for(var menu of menu_list)
	{
		if(menu != selected_menu)
		{
			$("#input_"+menu).hide();
			$("#output_"+menu).hide();
		}
		else
		{
			$("#input_"+menu).show();
			$("#output_"+menu).show();
		}
	}

	// To change menu name
	if(selected_menu == "image_to_text")
	{
		$("#menu").html("Image to Text");
	} 
	else if(selected_menu == "roots_of_polynomial_eq")
	{
		$("#menu").html("Roots of Polynomial Eq");
	}
	return 0;
}


$(document).ready(function(){

	// To preview image_to_text image
	$("#image_to_text_image").change(function(){
		
		let reader = new FileReader();	
		reader.onload = function () {
        	let dataURL = reader.result;
        	$("#image_to_text_preview").attr("src", dataURL);
    	}
    	let file = $("#image_to_text_image").prop("files")[0];
    	reader.readAsDataURL(file);
	});

})