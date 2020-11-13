$('#subscribe-form-id').validate({
    rules: {
        txtEmail: {
            required: true,
            email: true,
        },
    },
    messages: {
        txtEmail: {
            required:
                '<i class="fas fa-exclamation-triangle"></i> Please enter a mail',
            email:
                '<i class="fas fa-exclamation-triangle"></i> Please enter a valid mail',
        },
    },
    errorElement: 'div',
    errorLabelContainer: '.errorTxt',
});
