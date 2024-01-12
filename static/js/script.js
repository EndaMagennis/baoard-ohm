/* jshint esversion: 8, jquery: true, scripturl: true */

// initialise document
$(document).ready(function() {
    console.log("Document ready");
    // add like button functionality
    $(document).on('click', '#like-button', function(e) {
        console.log("Like button clicked");
        
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: "{% url 'feed:like' %}",
            data: {
                post_id: $("#like-button").val(),
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                action: "POST"
            },
            success: function(json) {
                console.log(response);
                $("#like-count").innerHTML = json["result"];
                console.log(json);
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
                
            }
        });
    });
    
});