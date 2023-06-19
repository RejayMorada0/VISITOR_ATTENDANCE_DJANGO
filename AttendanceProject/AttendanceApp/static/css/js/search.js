$(document).ready(function() {
    var searchInput = $('#search-input');
    var searchResults = $('#search-results');

    searchInput.on('input', function() {
        var query = searchInput.val();
        if (query.length >= 2) {
            $.ajax({
                url: '/search_qrcode', // Replace with the actual URL for your search view
                data: {query: query},
                success: function(response) {
                    var search = response.search;
                    var resultsHtml = '';

                    if (search.length > 0) {
                        resultsHtml += '<ul>';
                        for (var i = 0; i < search.length; i++) {
                            resultsHtml += '<li>' + search[i].name + '</li>';
                        }
                        resultsHtml += '</ul>';
                    } else {
                        resultsHtml = '<p>No results found.</p>';
                    }

                    searchResults.html(resultsHtml);
                }
            });
        } else {
            searchResults.empty();
        }
    });
});
