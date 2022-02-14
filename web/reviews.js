$.getJSON('http://galleywest.sdf.org/reviews.json', function(data) {
	
	for (var i=0; i<Object.keys(data).length; i++) {
		addReviewToMainPage(data[i], i)
		$(".mainholder").append("<hr class='review-split'>")
	}
});


function addReviewToMainPage(review, divid) {
	
	// Create the instance of the DIV for this review
	var divclass = "review-" + divid
	var divstr = "<div class='review " + divclass + "'></div>"
	var dotclass = "." + divclass
	$(".mainholder").append(divstr)
	
	// Add all of the things
	$("<h3 class='Title'></h3>").text(review["Title"]).appendTo(dotclass)
	$("<h5 class='Genres'></h5>").text(review["Genres"]).appendTo(dotclass)
	$("<h5 class='Platform'></h5>").text(review["Platform"]).appendTo(dotclass)
	$("<p class='Rating'></p>").text(review["Rating"]).appendTo(dotclass)
	$("<p class='Notes'></p>").text(review["Notes"]).appendTo(dotclass)
}


