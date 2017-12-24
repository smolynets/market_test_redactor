

function initLangSelector() {
    $('button.initLangSelector').click(function(event){
        var lan = $(this).val();
        $.cookie('django_language', lan, {'path': '/', 'expires': 365});
        location.reload(true);
        return true;
     });
    }


$(document).ready(function(){
    initLangSelector()
});