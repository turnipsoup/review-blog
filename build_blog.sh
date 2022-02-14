#!/usr/bin/env bash
#

if [[ -z $1 ]]; then
    echo "Usage: $0 </path/to/blog/root>"
    echo "\t Ensure your reviews are in /path/to/blog/root/reviews"
    exit 1
fi

BLOG_PATH=$1
INDEX_FILE="$BLOG_PATH/index2.html"
#AWK_FILE="$BLOG_PATH/create_website.awk"
AWK_FILE=awk/create_website.awk

TOP_OF_HTML_FILE="
<link rel='stylesheet' type='text/css' href='reviews.css'/>

<html>
	<body>
		<h1>Galley's Game Reviews</h1>
		<hr class='title-rule'>
		<div class='mainholder'>
"

END_OF_HTML_FILE="
        </div>
    </body>
</html>
"

rm $INDEX_FILE

echo $TOP_OF_HTML_FILE >> $INDEX_FILE

for i in $(ls -d reviews/*); do 
    awk -f $AWK_FILE $i >> $INDEX_FILE; 
done

echo $END_OF_HTML_FILE >> $INDEX_FILE