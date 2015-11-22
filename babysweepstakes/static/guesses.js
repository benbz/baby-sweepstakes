the_due_date = new Date("2015-12-22");

update_early_late = function(parent) {
    early_late_elem = $('.early_late', parent);
    if (early_late_elem.is('input')) {
        early_late = parseInt(early_late_elem.val(), 10);
    }
    else {
        early_late = parseInt(early_late_elem.text(), 10);
    }
    due_date = new Date(the_due_date.getTime() + early_late * 24 * 60 * 60 * 1000);
    $('.due_date', parent).text(due_date.toDateString());
};

$('.guess').each(function() {
    update_early_late(this);
});
$('.guess .early_late').change(function() {
    update_early_late($(this).parent());
});

update_weight = function(parent) {
    pounds = parseInt($('.pounds', parent).val(), 10);
    ounces = parseInt($('.ounces', parent).val(), 10);
    all_ounces = pounds * 16 + ounces;
    all_grams = all_ounces * 28.3495;
    kilos = Math.floor(all_grams / 1000);
    grams = Math.floor(all_grams % 1000);
    $('.kilos_and_grams', parent).text('' + kilos + '.' + grams + 'kg');
};

$('.guess').each(function() {
    update_weight($(this).parent());
});
$('.guess .pounds').change(function() {
    update_weight($(this).parent());
});
$('.guess .ounces').change(function() {
    update_weight($(this).parent());
});
