// Submete informações de marcação
var form = document.querySelector('form')
form.addEventListener('submit', e => {
    e.preventDefault()

    var user = document.getElementsByName('user')[0]
    user = user.value

    var answers = []
    var answersList = document.querySelectorAll('[data-answer]')
    answersList.forEach(answer => {
        answers.push(answer.value)
    });

    navigator.geolocation.getCurrentPosition(function(position) {
        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude

        var formdata = new FormData();
        // formdata.append('postural_analysis_markup', JSON.stringify(postural_analysis_markup)); // marcações
        // formdata.append('selected_images_to_show_at_resume', selected_images_to_show_at_resume);
        // formdata.append('selected_images_to_show_at_report', selected_images_to_show_at_report);
        formdata.append('csrfmiddlewaretoken', form['csrfmiddlewaretoken'].value);
        formdata.append('user', user);
        formdata.append('latitude', latitude);
        formdata.append('longitude', longitude);
        formdata.append('answers', JSON.stringify(answers));

        $.ajax({
            type: 'POST',
            url: form.action,
            data: formdata,
            processData: false,
            contentType: false,
            success: function(response) {
                window.location.replace(window.location.origin);
            },
        });
    })
})