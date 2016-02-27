jQuery.expr[':'].regex = function(elem, index, match) {
    var matchParams = match[3].split(','),
        validLabels = /^(data|css):/,
        attr = {
            method: matchParams[0].match(validLabels) ? 
                        matchParams[0].split(':')[0] : 'attr',
            property: matchParams.shift().replace(validLabels,'')
        },
        regexFlags = 'ig',
        regex = new RegExp(matchParams.join('').replace(/^s+|s+$/g,''), regexFlags);
    return regex.test(jQuery(elem)[attr.method](attr.property));
}

$(document).ready(function() {
	$('.btn').addClass('btn-no-radius');
	$('.btn-primary').addClass('btn-default btn-clinic btn-clinic-primary btn-no-radius').removeClass('btn-primary');
	$('#store_form #workingday_set-group .field-type select').css('pointerEvents','none');
	$('.label-tag > .required').each(function(index, el) {
		var t = $(this).html().trim();
		var required_ = $('<span>').html(' (*)').addClass('text-red text-strong').html();
		$(this).html(t.substr(0, t.length - 1) + ' <span class="text-red text-strong">(*)</span>' + ':');
	});;

	$('.add-row').hide();
	// $('.vTextField, .vLargeTextField').addClass('form-control');

	$('.clinic_hack_first_column select:regex(#id_workingday_set-[0-9]-type)').each(function() {
		var date =  $(this).find('[selected=selected]').text();
		console.log(date)
	})
});