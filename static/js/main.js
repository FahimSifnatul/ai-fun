
$(document).ready(function(){

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

	// clicking input card header
	$("#input_card_header").click(function(){
		$("#input_card").css({"animation" : "flip-forward 3s forwards"});
		$("#input_card_header").css({"animation" : "flip-forward 3s forwards"});
		$("#input_card_body").css({"animation" : "flip-forward 3s forwards"});
		$("#input_card_footer").css({"animation" : "flip-forward 3s forwards"});
		//$("#input_card_back").css({"animation" : "flip-backward 3s forwards"});
	});
})