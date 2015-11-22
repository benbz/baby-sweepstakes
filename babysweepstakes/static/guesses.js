the_due_date = new Date("2015-12-22");

update_guess = function(parent) {
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
    update_guess(this);
});
$('.guess .early_late').change(function() {
    update_guess($(this).parent());
});
