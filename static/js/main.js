const menu_list  = ["image_to_text", "root_of_linear_eq"];

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
			$("#"+menu).hide();
		}
	}

	// To change menu name
	if(selected_menu == "image_to_text")
	{
		$("#menu").html("Image to Text");
	} 
	else if(selected_menu == "root_of_linear_eq") $("#menu").html("Root of Linear eq");
	
	// To show selected menu content
	$("#"+selected_menu).show();
	return 0;
}


$(document).ready(function(){

	// To preview image_to_text image
	$("#id_image_to_text").change(function(){
		
		let reader = new FileReader();	
		reader.onload = function () {
        	let dataURL = reader.result;
        	$("#image_to_text_preview").attr("src", dataURL);
    	}
    	let file = $("#id_image_to_text").prop("files")[0];
    	reader.readAsDataURL(file);
	});

})