// The below code is taken from the Boutique Ado walkthrough

// Update quantity on click
$('.update-link').click(function(e) {
    var form = $(this).prev('.update-form');
    form.submit();
})

// Remove item and reload on click
$('.remove-item').click(function(e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id').split('remove_')[1];
    var colour = $(this).data('colour');
    var url = `/basket/remove/${itemId}`;
    var data = {'csrfmiddlewaretoken': csrfToken, 'colour': colour};

    $.post(url, data)
        .done(function() {
            location.reload();
        });
})
