BEGIN {print "<div class='review'>"}
    /####/ {printf "<h3 class='Title'>%s</h3>\n", $2}
    /- Genres:/ {$1=$2=""; printf "<h5 class='Genres'>%s</h5>\n", substr($0, 3)}
    /- Platform:/ {$1=$2=""; printf "<h5 class='Platform'>%s</h5>\n", substr($0, 3)}
    /- Rating:/ {$1=$2=""; rating = sprintf("<p class='Rating'><i>---%s---</i></p>", substr($0, 3))}
    /- Notes: / {print "<div class='Notes'>"; divend = "</div>"}
    /- Notes:/,/!./ { sub(/- Notes: /, ""); printf "%s\n", $0;}
END {print divend; print rating; print "</div><hr class='review-split'>"}