#! /usr/pkg/bin/python3.10
# 

import os
import json
import datetime
import platform

BLOG_PATH = "/www/gm/g/galleywest"
REVIEWS = f"{BLOG_PATH}/reviews"

def readfile(filename) -> str:
	with open(filename, "r") as f:	
		filecontents = f.read().strip()
		return filecontents

def readreview(reviewfile) -> str:
	propername = f"{REVIEWS}/{reviewfile}"
	return readfile(propername)

def get_review_title(review) -> str:
	return review.split("\n")[0].split("#")[-1].strip()

def get_review_subject(review, subject) -> str:
	review_lines = review.split("\n")
	notes_lines = ""
	for i in range(len(review_lines)):
		if f"- {subject}:" in review_lines[i]:
			if subject == "Notes": # If we are gathering the notes, then grab all
				notes_lines += "<br>".join(review_lines[i:])  # of the remaining lines in the file
			else:
				return review_lines[i].split(f"- {subject}:")[-1].strip()

	return notes_lines.replace(f"- {subject}:", "").strip()

def get_review_subjects(review) -> list[str]:
	review_lines = review.split("\n")
	subjects = []
	for line in review_lines:
		if line.startswith("-"):
			subjline = line.split(":")[0].replace("- ", "")
			return subjline


def create_review_object(review) -> dict[str, str]:
	subjects = ["Genres", "Platform", "Start", "End", "Rating", "Notes"]
	review_object = {}
	review_lines = review.split("\n")
	review_title = get_review_title(review)
	review_object["Title"] = review_title

	for subject in subjects:
		review_object[subject] = get_review_subject(review, subject)
	return review_object

def create_info_object() -> str:
	infoobj = {}
	infoobj["update_time"] = str(datetime.datetime.now())
	infoobj["platform"] = platform.system()
	return infoobj

if __name__ == "__main__":
	blog_contents = sorted(os.listdir(REVIEWS))
	blog_json = {}
	
	counter = 0	
	for rawreview in blog_contents:
		review = readreview(rawreview)
		blog_json[counter] = create_review_object(review)
		counter += 1
	
	# Save reviews
	savefile = f"{BLOG_PATH}/reviews.json" 
	with open(savefile, "w") as f:
		f.write(json.dumps(blog_json))
		f.close()
	os.chmod(savefile, 0o755)

	# Save extra info
	infofile = f"{BLOG_PATH}/information.json"
	with open(infofile, "w") as f:
		f.write(json.dumps(create_info_object()))
		f.close()
	os.chmod(infofile, 0o755)

