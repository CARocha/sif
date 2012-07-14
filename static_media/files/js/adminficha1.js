(function($){
	$(document).ready(function(){
    
    $('#id_producto_no_maderable').change(function(){	
    		if (($("#id_producto_no_maderable").val()) == 1) {
    			$('.field-tipo_producto').show("100");
    		}else{
    			$('.field-tipo_producto').hide("100");
    		}
		});
    $('#id_gobierno_gti').change(function(){	
    		if (($("#id_gobierno_gti").val()) == 1) {
    			$('.field-nombre_gti').show("100");
    		}else{
    			$('.field-nombre_gti').hide("100");
    		}
		});
    $('#id_organizado_3').change(function(){
        if ($('#id_organizado_3').is(':checked')){
        // if ($('#id_organizado_3') == "checked") {
            $('.field-organizacion').hide("100");
            $('.field-desde').hide("100");
        }else{
            $('.field-organizacion').show("100");
            $('.field-desde').show("100");
        }
    });
        
	});
})(jQuery || django.jQuery);