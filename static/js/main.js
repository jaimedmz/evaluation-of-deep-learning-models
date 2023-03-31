$(document).ready(function () {
    // Init
    $('.image-section').hide();
    $('.loader').hide();
    $('.img-prueba').show();
    $('#result').hide();
    $('#expected').hide();
    $('.modelEmpty').show();
    $('.alemanDatabase').hide();   
    $('.belgiumDatabase').hide();
    $('.chinaDatabase').hide();
    

    $('#option_dataBase').change(function (e) {
        if ($(this).val() == "1") {
            $('.modelEmpty').hide();
            $('.alemanDatabase').show();
            $('.belgiumDatabase').hide();
            $('.chinaDatabase').hide();
            $('#option_model_Aleman').change(function (e) {
            if ($(this).val() === "1") {
                $('#btn-predict').click(function () {
                    var form_data = new FormData($('#upload-file')[0]);
            
                    // Show loading animation
                    $(this).hide();
                    $('.loader').show();
            
                    // Make prediction by calling api /predict
                    $.ajax({
                        type: 'POST',
                        url: '/predictColor__Model1_GTSRB',
                        data: form_data,
                        contentType: false,
                        cache: false,
                        processData: false,
                        async: true,
                        success: function (data) {
                            // Get and display the result
                            
                            $('#result').fadeIn(600);
                            $('#expected').fadeIn(600);
                            $('.img-prueba').hide();
                            $('#btn-predict').show();
                            $('#result').text(data);
                            console.log('Success!');
                        },
                    });
                });
                $('#btn-predict').click(function () {
                    var form_data = new FormData($('#upload-file')[0]);
                    // Make prediction by calling api /predict
                    $.ajax({
                        type: 'POST',
                        url: '/predictExpectedModels_GTSRB',
                        data: form_data,
                        contentType: false,
                        cache: false,
                        processData: false,
                        async: true,
                        success: function (data) {
                            // Get and display the result
                            $('.loader').hide();
                            $('#expected').fadeIn(600);
                            $('.img-prueba').hide();
                            $('#btn-predict').show();
                            $('#expected').text(data);
                            console.log('Success!');
                        },
                    });
                });


            }
            else if($(this).val() == "2"){
                $('#btn-predict').click(function () {
                    var form_data = new FormData($('#upload-file')[0]);
            
                    // Show loading animation
                    $(this).hide();
                    $('.loader').show();      
                    // Make prediction by calling api /predict
                    $.ajax({
                        type: 'POST',
                        url: '/predictColor__Model2_GTSRB',
                        data: form_data,
                        contentType: false,
                        cache: false,
                        processData: false,
                        async: true,
                        success: function (data) {
                            // Get and display the result
                           
                            $('#result').fadeIn(600);
                            $('#expected').fadeIn(600);
                            $('.img-prueba').hide();
                            $('#btn-predict').show();
                            $('#result').text(data);
                            console.log('Success!');
                        },
                    });
                });
            
                $('#btn-predict').click(function () {
                    var form_data = new FormData($('#upload-file')[0]);
                    // Make prediction by calling api /predict
                    $.ajax({
                        type: 'POST',
                        url: '/predictExpectedModels_GTSRB',
                        data: form_data,
                        contentType: false,
                        cache: false,
                        processData: false,
                        async: true,
                        success: function (data) {
                            // Get and display the result
                            $('.loader').hide();
                            $('#expected').fadeIn(600);
                            $('.img-prueba').hide();
                            $('#btn-predict').show();
                            $('#expected').text(data);
                            console.log('Success!');
                        },
                    });
                });
            }
            else if($(this).val() == "3"){
                $('#btn-predict').click(function () {
                    var form_data = new FormData($('#upload-file')[0]);
            
                    // Show loading animation
                    $(this).hide();
                    $('.loader').show();      
                    // Make prediction by calling api /predict
                    $.ajax({
                        type: 'POST',
                        url: '/predictColor__Model3_GTSRB',
                        data: form_data,
                        contentType: false,
                        cache: false,
                        processData: false,
                        async: true,
                        success: function (data) {
                            // Get and display the result
                            
                            $('#result').fadeIn(600);
                            $('#expected').fadeIn(600);
                            $('.img-prueba').hide();
                            $('#btn-predict').show();
                            $('#result').text(data);
                            console.log('Success!');
                        },
                    });
                });
            
                $('#btn-predict').click(function () {
                    var form_data = new FormData($('#upload-file')[0]);
                    // Make prediction by calling api /predict
                    $.ajax({
                        type: 'POST',
                        url: '/predictExpectedModels_GTSRB',
                        data: form_data,
                        contentType: false,
                        cache: false,
                        processData: false,
                        async: true,
                        success: function (data) {
                            // Get and display the result
                            $('.loader').hide();
                            $('#expected').fadeIn(600);
                            $('.img-prueba').hide();
                            $('#btn-predict').show();
                            $('#expected').text(data);
                            console.log('Success!');
                        },
                    });
                });
            }
            else if($(this).val() == "4"){
                $('#btn-predict').click(function () {
                    var form_data = new FormData($('#upload-file')[0]);
            
                    // Show loading animation
                    $(this).hide();
                    $('.loader').show();      
                    // Make prediction by calling api /predict
                    $.ajax({
                        type: 'POST',
                        url: '/predictColor__Model4_GTSRB',
                        data: form_data,
                        contentType: false,
                        cache: false,
                        processData: false,
                        async: true,
                        success: function (data) {
                            // Get and display the result
                            
                            $('#result').fadeIn(600);
                            $('#expected').fadeIn(600);
                            $('.img-prueba').hide();
                            $('#btn-predict').show();
                            $('#result').text(data);
                            console.log('Success!');
                        },
                    });
                });
            
                $('#btn-predict').click(function () {
                    var form_data = new FormData($('#upload-file')[0]);
                    // Make prediction by calling api /predict
                    $.ajax({
                        type: 'POST',
                        url: '/predictExpectedModels_GTSRB',
                        data: form_data,
                        contentType: false,
                        cache: false,
                        processData: false,
                        async: true,
                        success: function (data) {
                            // Get and display the result
                            $('.loader').hide();
                            $('#expected').fadeIn(600);
                            $('.img-prueba').hide();
                            $('#btn-predict').show();
                            $('#expected').text(data);
                            console.log('Success!');
                        },
                    });
                });
            }
            else if($(this).val() == "5"){
                $('#btn-predict').click(function () {
                    var form_data = new FormData($('#upload-file')[0]);
            
                    // Show loading animation
                    $(this).hide();
                    $('.loader').show();      
                    // Make prediction by calling api /predict
                    $.ajax({
                        type: 'POST',
                        url: '/predictGrayscale_Model1_GTSRB',
                        data: form_data,
                        contentType: false,
                        cache: false,
                        processData: false,
                        async: true,
                        success: function (data) {
                            // Get and display the result
                           
                            $('#result').fadeIn(600);
                            $('#expected').fadeIn(600);
                            $('.img-prueba').hide();
                            $('#btn-predict').show();
                            $('#result').text(data);
                            console.log('Success!');
                        },
                    });
                });
            
                $('#btn-predict').click(function () {
                    var form_data = new FormData($('#upload-file')[0]);
                    // Make prediction by calling api /predict
                    $.ajax({
                        type: 'POST',
                        url: '/predictExpectedModels_GTSRB',
                        data: form_data,
                        contentType: false,
                        cache: false,
                        processData: false,
                        async: true,
                        success: function (data) {
                            // Get and display the result
                            $('.loader').hide();
                            $('#expected').fadeIn(600);
                            $('.img-prueba').hide();
                            $('#btn-predict').show();
                            $('#expected').text(data);
                            console.log('Success!');
                        },
                    });
                });
            }
            else if($(this).val() == "6"){
                $('#btn-predict').click(function () {
                    var form_data = new FormData($('#upload-file')[0]);
            
                    // Show loading animation
                    $(this).hide();
                    $('.loader').show();      
                    // Make prediction by calling api /predict
                    $.ajax({
                        type: 'POST',
                        url: '/predictGrayscale_Model2_GTSRB',
                        data: form_data,
                        contentType: false,
                        cache: false,
                        processData: false,
                        async: true,
                        success: function (data) {
                            // Get and display the result
                          
                            $('#result').fadeIn(600);
                            $('#expected').fadeIn(600);
                            $('.img-prueba').hide();
                            $('#btn-predict').show();
                            $('#result').text(data);
                            console.log('Success!');
                        },
                    });
                });
            
                $('#btn-predict').click(function () {
                    var form_data = new FormData($('#upload-file')[0]);
                    // Make prediction by calling api /predict
                    $.ajax({
                        type: 'POST',
                        url: '/predictExpectedModels_GTSRB',
                        data: form_data,
                        contentType: false,
                        cache: false,
                        processData: false,
                        async: true,
                        success: function (data) {
                            // Get and display the result
                            $('.loader').hide();
                            $('#expected').fadeIn(600);
                            $('.img-prueba').hide();
                            $('#btn-predict').show();
                            $('#expected').text(data);
                            console.log('Success!');
                        },
                    });
                });
            }
            else if($(this).val() == "7"){
                $('#btn-predict').click(function () {
                    var form_data = new FormData($('#upload-file')[0]);
            
                    // Show loading animation
                    $(this).hide();
                    $('.loader').show();      
                    // Make prediction by calling api /predict
                    $.ajax({
                        type: 'POST',
                        url: '/predictGrayscale_Model3_GTSRB',
                        data: form_data,
                        contentType: false,
                        cache: false,
                        processData: false,
                        async: true,
                        success: function (data) {
                            // Get and display the result
                           
                            $('#result').fadeIn(600);
                            $('#expected').fadeIn(600);
                            $('.img-prueba').hide();
                            $('#btn-predict').show();
                            $('#result').text(data);
                            console.log('Success!');
                        },
                    });
                });
          
                $('#btn-predict').click(function () {
                    var form_data = new FormData($('#upload-file')[0]);
                    // Make prediction by calling api /predict
                    $.ajax({
                        type: 'POST',
                        url: '/predictExpectedModels_GTSRB',
                        data: form_data,
                        contentType: false,
                        cache: false,
                        processData: false,
                        async: true,
                        success: function (data) {
                            // Get and display the result
                            $('.loader').hide();
                            $('#expected').fadeIn(600);
                            $('.img-prueba').hide();
                            $('#btn-predict').show();
                            $('#expected').text(data);
                            console.log('Success!');
                        },
                    });
                });
            }
            else if($(this).val() == "8"){
                $('#btn-predict').click(function () {
                    var form_data = new FormData($('#upload-file')[0]);
            
                    // Show loading animation
                    $(this).hide();
                    $('.loader').show();      
                    // Make prediction by calling api /predict
                    $.ajax({
                        type: 'POST',
                        url: '/predictGrayscale_Model4_GTSRB',
                        data: form_data,
                        contentType: false,
                        cache: false,
                        processData: false,
                        async: true,
                        success: function (data) {
                            // Get and display the result
                           
                            $('#result').fadeIn(600);
                            $('#expected').fadeIn(600);
                            $('.img-prueba').hide();
                            $('#btn-predict').show();
                            $('#result').text(data);
                            console.log('Success!');
                        },
                    });
                });
            
                $('#btn-predict').click(function () {
                    var form_data = new FormData($('#upload-file')[0]);
                    // Make prediction by calling api /predict
                    $.ajax({
                        type: 'POST',
                        url: '/predictExpectedModels_GTSRB',
                        data: form_data,
                        contentType: false,
                        cache: false,
                        processData: false,
                        async: true,
                        success: function (data) {
                            // Get and display the result
                            $('.loader').hide();
                            $('#expected').fadeIn(600);
                            $('.img-prueba').hide();
                            $('#btn-predict').show();
                            $('#expected').text(data);
                            console.log('Success!');
                        },
                    });
                });
            }
            else {
            }
        })
        }
        if ($(this).val() == "2") {
            $('.modelEmpty').hide();
            $('.belgiumDatabase').show();
            $('.alemanDatabase').hide();   
            $('.chinaDatabase').hide();
        }
        if ($(this).val() == "3") {
            $('.modelEmpty').hide();
            $('.chinaDatabase').show();
            $('.alemanDatabase').hide();
            $('.belgiumDatabase').hide();
        }
        else{     
        }
        
      })
/*
      var dir = "pruebaimagenes/";
        var fileextension = ".png";
        $.ajax({
            //This will retrieve the contents of the folder if the folder is configured as 'browsable'
            url: dir,
            success: function (data) {
                //List all .png file names in the page
                $(data).find("a:contains(" + fileextension + ")").each(function () {
                    var filename = this.href.replace(window.location.host, "").replace("http://", "");
                    $("body").append("<img src='" + dir + filename + "'>");
                });
            }
        });
*/
    // Upload Preview
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview').hide();
                $('.img-prueba').hide();
                $('#imagePreview').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('.img-prueba').hide();
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        $('#expected').text('');
        $('#expected').hide();
        readURL(this);
    });
/*
    // Predict
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);

        // Show loading animation
        $(this).hide();
        $('.loader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loader').hide();
                $('#result').fadeIn(600);
                $('#expected').fadeIn(600);
                $('.img-prueba').hide();
                $('#btn-predict').show();
                $('#result').text(data);
                console.log('Success!');
            },
        });
    });

    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);
        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/predictExpected',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loader').hide();
                $('#expected').fadeIn(600);
                $('.img-prueba').hide();
                $('#btn-predict').show();
                $('#expected').text(data);
                console.log('Success!');
            },
        });
    });
*/
});
