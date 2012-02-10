// set up jQuery UI widgets
$(function(){
    // Disabled because it screws with accordian
//    $('.ui-widget').hover(
//        function() { $(this).addClass('ui-state-hover'); },
//        function() { $(this).removeClass('ui-state-hover'); }
//    );
	$('.icon-button').hover(
		function() { $(this).addClass('ui-state-hover'); },
		function() { $(this).removeClass('ui-state-hover'); }
	);
	 
	 
    $('input.datepicker').datepicker({
        dateFormat: 'yy-mm-dd'
    });

    $('input.datetimepicker').datetimepicker({
        showSecond: true,
        dateFormat: 'yy-mm-dd',
        timeFormat: 'hh:mm:ss'
    });

    $('input.timepicker').timepicker({
        timeFormat: 'hh:mm:ss',
        showSecond: true
    });

    function getLabelFor(id){
        return $('label[for="'+id+'"]').text();
    };

    $('.model-edit-form select:empty')
        .append('<option value="__None"></option>');

    $('.model-edit-form select > option[value="__None"]:only-child').parent()
        .attr('disabled', 'disabled')
        .attr('data-placeholder', (
            function(index, attr){
                if (!attr){
                    return 'No '+getLabelFor(this.id)+' available to choose';
                }
            }));

    $('.model-edit-form select')
        .attr('data-placeholder', (
            function(index, attr){
                if (!attr){
                    return 'Choose '+getLabelFor(this.id)+'...';
                }
            }))
        .chosen({no_results_text: "No results matched",
                 allow_single_deselect: true});
});



