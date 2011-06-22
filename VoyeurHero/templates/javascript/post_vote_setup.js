{% include "javascript/ajax_csrf_code.js" %}
{% include "javascript/string_format.js" %}
	function handle_voter(type,id) {
		var fun = function(data) {
			mapper = {
				up: 'Bodacious',
				down: 'Bogus',
				clear: 'No Vote'
			}
			jqString = '[class="post_vote"][value="{0}"]'.format(id);
			post = $(jqString);
			$('.post_vote_score',post).text(data.score.score);
			$('.post_vote_num_votes',post).text(data.score.num_votes);
			$('.post_vote_user_description',post).text(mapper[type]);
		}
		return fun;
	}
    
    function voter(type){
        var fun = function(event){
            id = event.target.parentElement.value;
            $.ajax({
                dataType: 'json',
                type: 'POST',
                url: '/post_vote/' + id + '/' + type + 'vote/',
                success: handle_voter(type,id)
            });
        }
        return fun;
    }
