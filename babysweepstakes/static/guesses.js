the_due_date = new Date("2015-12-22");

update_early_late = function(early_late_elem, parent) {
    if (early_late_elem.is('option')) {
        early_late = parseInt(early_late_elem.val(), 10);
    }
    else {
        early_late = parseInt(early_late_elem.text(), 10);
    }
    due_date = new Date(the_due_date.getTime() + early_late * 24 * 60 * 60 * 1000);
    date_text = 'Invalid Date' != due_date ? due_date.toDateString() : '';
    $('.due_date', parent).text(date_text);
};

$('tr.guess').each(function() {
    update_early_late($('.early_late', this), this);
});
$('form.guess').each(function() {
    update_early_late($('.early_late option:selected', this), this);
});
$('form.guess .early_late').change(function() {
    parent = $(this).parent();
    update_early_late($('.early_late option:selected', parent), parent);
});

update_weight = function(parent) {
    pounds = parseInt($('.pounds', parent).val(), 10);
    ounces = parseInt($('.ounces', parent).val(), 10);
    all_ounces = pounds * 16 + ounces;
    all_grams = all_ounces * 28.3495;
    kilos = Math.floor(all_grams / 1000);
    grams = Math.floor(all_grams % 1000);
    metric_text = !isNaN(kilos) ? '' + kilos + '.' + grams + 'kg' : '';
    $('.kilos_and_grams', parent).text(metric_text);
};

$('.guess').each(function() {
    update_weight($(this).parent());
});
$('.guess .pounds').change(function() {
    update_weight($(this).parent());
});
$('.guess .ounces').change(function() {
    ounces = $(this).val();
    pounds_elem = $(this).parent().find('.pounds');
    pounds = parseInt(pounds_elem.val(), 10);
    if (ounces >= 16) {
        pounds_elem.val(pounds + 1);
        $(this).val(0);
    }
    else if (ounces < 0) {
        if (pounds > 0) {
            pounds_elem.val(pounds - 1);
            $(this).val(15);
        }
        else {
            $(this).val(0);
        }
    }
    update_weight($(this).parent());
});
