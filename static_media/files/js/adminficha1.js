(function($){
	$(document).ready(function(){
    
    $('#id_producto_no_maderable').change(function(){	
    		if (($("#id_producto_no_maderable").val()) == 1) {
    			$('.field-tipo_producto').fadeIn(500).css('display', 'block');
    		}else{
    			$('.field-tipo_producto').fadeOut("slow").css('display', 'none');
    		}
		});
        
	});
})(jQuery || django.jQuery);

