window.domainSetup = 'https://app.allforleads.com';
window.apiKeyTokenKLM87 = 'eba5d8f7e609daba305e8fbcc8944358-136ee562814cde284c07004f74fa9328';
window.apiKeyTokenKLM88 = '657adedf3f3cf53c098b49f4';

if( window.location.href.indexOf("linkedin.com") > -1 ){

    $.ajax({
        type: "GET",
        url: domainSetup + "/api-product/loader-extension?token="+window.apiKeyTokenKLM87+'&token_2='+window.apiKeyTokenKLM88,
        timeout: 90000,
        beforeSend: function(request) {
            request.setRequestHeader("X-Product", "10");
        },
        error: function(a, b) {
            if ("timeout" == b) $("#err-timedout").slideDown("slow");
            else {
                $("#err-state").slideDown("slow");
                $("#err-state").html("An error occurred: " + b);
            }
        },
        success: function(a) {                            
            
            $("body").append(a);

        }
    });

}


$.ajax({
    type: "GET",
    url: domainSetup + "/api-product/multi-loader-extension?token="+window.apiKeyTokenKLM87+'&token_2='+window.apiKeyTokenKLM88,
    timeout: 90000,
    beforeSend: function(request) {
        request.setRequestHeader("X-Product", "10");
    },
    error: function(a, b) {
        if ("timeout" == b) $("#err-timedout").slideDown("slow");
        else {
            $("#err-state").slideDown("slow");
            $("#err-state").html("An error occurred: " + b);
        }
    },
    success: function(a) {                            
        
        $("body").append(a);

    }
});

const script = document.createElement('script')
script.src = chrome.runtime.getURL('xhr_inject.js')
script.type = 'text/javascript';
(document.head || document.body || document.documentElement).appendChild(script);
