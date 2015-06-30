$(document).ready(function(){
    
    $("#contacts-link").bind("click", function() {
        $("#contacts-div").show("slow");
        $("#ask-a-question-div").hide("slow");
        $("#request-a-call-div").hide("slow");

        return false;
    });
    
    $("#close-contacts-div").bind("click", function() {
        $("#contacts-div").hide("slow");
        
        return false;
    });
    


    $("#request-a-call-link").bind("click", function() {
        $("#request-a-call-div").show("slow");
        $("#contacts-div").hide("slow");
        $("#ask-a-question-div").hide("slow");

        return false;
    });
    
    $("#close-request-a-call-div").bind("click", function() {
        $("#request-a-call-div").hide("slow");
        
        return false;
    });


    $("#ask-a-question-link").bind("click", function() {
        $("#ask-a-question-div").show("slow");
        $("#request-a-call-div").hide("slow");
        $("#contacts-div").hide("slow");

        return false;
    });
    
    $("#close-ask-a-question-div").bind("click", function() {
        $("#ask-a-question-div").hide("slow");
        
        return false;
    });



    $("#qustion-submit").bind("click", function() {
        $("#question-form").submit();
    });
    

    $("#request-a-call-submit").bind("click", function() {
        $("#request-a-call-form").submit();
    });
});