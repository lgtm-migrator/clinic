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
	if ($(".alert-danger").length > 0) {
		$("fieldset.module.aligned.wide").prepend("<ul class='errorlist'><li>枠を正しく入力してください。</li></ul>");
	}

	$('.btn').addClass('btn-no-radius');
	$('.btn-primary').addClass('btn-default btn-clinic btn-clinic-primary btn-no-radius').removeClass('btn-primary');
	$('#store_form #workingday_set-group .field-type select').css('pointerEvents','none');
	$('.label-tag > .required').each(function(index, el) {
		var t = $(this).html().trim();
		var required_ = $('<span>').html(' (*)').addClass('text-red text-strong').html();
		$(this).html(t.substr(0, t.length - 1) + ' <span class="text-red">*</span>' + ':');
	});
	$('.label-tag > label').each(function(index, el) {
		var t = $(this).html().trim();
		$(this).html(t.substr(0, t.length - 1));
	});

	$('.add-row').hide();
	// $('.vTextField, .vLargeTextField').addClass('form-control');

	$('.clinic_hack_first_column select:regex(#id_workingday_set-[0-9]-type)').each(function() {
		var date =  $(this).find('[selected=selected]').text();
		console.log(date)
	})

	$("#store_form").submit(function(event) {
		$(".errorlist").remove();
		var errors = false;
        $('.dynamic-holidayworking_set').each(function() {
			if ($(this).find('.form-control').first().val() == "") {
				$(this).find('.vIntegerField').each(function() {
					$(this).removeClass("alert-danger");
					if ($(this).val() != "") {
						$(this).addClass("alert-danger");
						if (!errors) {
							$("fieldset.module.aligned.wide").prepend("<ul class='errorlist'><li>特別な営業日が設定されていないため登録できません。</li></ul>");
						}
						errors = true;
					}
				})
			}

		})
		if (errors == true) {
			event.preventDefault();
		}
    });
    
});