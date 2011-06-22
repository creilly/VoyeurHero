$.each(['up','down','clear'],function(ind, type) {
	$('.post_{0}_vote'.format(type)).click(voter(type));
});
