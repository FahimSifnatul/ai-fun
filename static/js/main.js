
$(document).ready(function(){
	var present_menu = "menu";

	// To preview image_to_text image
	$("#image_to_text_image").change(function(){
		
		let reader = new FileReader();	
		reader.onload = function () {
        	let dataURL = reader.result;
        	$("#image_to_text_preview").css("background-image", "url('"+dataURL+"')");
    	}
    	let file = $("#image_to_text_image").prop("files")[0];
    	reader.readAsDataURL(file);
	});

	// clicking menu items
	$("#menu_image_to_text").click(function(){
		present_menu = "image_to_text";
		$("#menu").html("Image to Text");
		$("#image_to_text").show();
	});
})