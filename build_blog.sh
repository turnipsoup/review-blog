#!/usr/bin/env bash
#

if [[ -z $1 ]]; then
    echo "Usage: $0 </path/to/blog/root>"
    echo "\t Ensure your reviews are in /path/to/blog/root/reviews"
    exit 1
fi

BLOG_PATH=$1
INDEX_FILE="$BLOG_PATH/index.html"
AWK_FILE="$BLOG_PATH/create_website.awk"
#AWK_FILE=awk/create_website.awk

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

PAGE_FOOTER="<center><i>All rights reserved to the author. Page last modifed at $(date). Served from $(cat /etc/release | head -n 1 | awk '{print $1}').</i></center>"

rm $INDEX_FILE

echo $TOP_OF_HTML_FILE >> $INDEX_FILE

for i in $(ls -d $BLOG_PATH/reviews/*); do 
    awk -f $AWK_FILE $i >> $INDEX_FILE; 
done

echo $END_OF_HTML_FILE >> $INDEX_FILE
echo $PAGE_FOOTER >> $INDEX_FILE

chmod 755 $INDEX_FILE
