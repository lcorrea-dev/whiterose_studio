var validator = $('#wwu-form-id').validate({
    rules: {
        txtName: {
            required: true,
            maxlength: 35,
        },
        txtPortfolio: {
            required: true,
            url: true,
        },
        txtEmail: {
            required: true,
            email: true,
        },
        txtAbout: {
            required: true,
            minlength: 100,
        },
    },
    messages: {
        txtName: {
            required:
                '<i class="fas fa-exclamation-triangle"></i> Please enter your full name  ',
            maxlength:
                '<i class="fas fa-exclamation-triangle"></i> Max. 35 characters  ',
        },
        txtPortfolio: {
            required:
                '<i class="fas fa-exclamation-triangle"></i> Please enter a link to your portfolio',
            url:
                '<i class="fas fa-exclamation-triangle"></i> Please enter a valid url',
        },
        txtEmail: {
            required:
                '<i class="fas fa-exclamation-triangle"></i> Please enter a contact mail',
            email:
                '<i class="fas fa-exclamation-triangle"></i> Please enter a valid mail',
        },
        txtAbout: {
            required:
                '<i class="fas fa-exclamation-triangle"></i> Please enter your description',
            minlength:
                '<i class="fas fa-exclamation-triangle"></i> Min. 100 characters',
        },
    },
    showErrors: function (errorMap, errorList) {
        var errors = this.numberOfInvalids();
        this.defaultShowErrors();

        if (errors === 1) {
            $('#summaryErrors').html(
                '<i class="fas fa-exclamation-triangle"></i> ' +
                    ' 1 field is invalid, please correct the error above'
            );
            document.getElementById('summaryErrors').style.display = 'block';
            return;
        } else if (errors > 1) {
            $('#summaryErrors').html(
                '<i class="fas fa-exclamation-triangle"></i> ' +
                    errors +
                    ' fields are invalids, please correct the errors above'
            );
            document.getElementById('summaryErrors').style.display = 'block';
            return;
        } else {
            $('#summaryErrors').text('');
            document.getElementById('summaryErrors').style.display = 'none';
        }
    },
});

function alphaOnly(event) {
    var key = event.keyCode;
    return (
        (key >= 65 && key <= 90) ||
        key == 8 ||
        key == 9 || // Shift
        key == 13 || // Enter
        key == 32 // Space
    );
}

function formatUrl(url) {
    var basic = url.value.replace('https://', '');
    basic = basic.replace('https:/', '');

    basic = basic.replace('http://', '');
    basic = basic.replace('http:/', '');

    if (basic == '') {
        return;
    }
    url.value = 'https://' + basic;
}
