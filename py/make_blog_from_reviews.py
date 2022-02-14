#! /usr/pkg/bin/python3.10
# 

import os
import json

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
	for line in review_lines:
		if f"- {subject}:" in line:
			if subject == "Notes": # If we are gathering the notes, then grab all
				notes_lines += line  # of the remaining lines in the file
			else:
				return line.split(f"- {subject}:")[-1].strip()

	return notes_lines.replace(f"- {subject}:", "").strip()

def get_review_subjects(review) -> list[str]:
	review_lines = review.split("\n")
	subjects = []
	for line in review_lines:
		if line.startswith("-"):
			subjline = line.split(":")[0].replace("- ", "")
			return subjline


def create_review_object(review):
	subjects = ["Genres", "Platform", "Start", "End", "Rating", "Notes"]
	review_object = {}
	review_lines = review.split("\n")
	review_title = get_review_title(review)
	review_object["Title"] = review_title

	for subject in subjects:
		review_object[subject] = get_review_subject(review, subject)
	return review_object

if __name__ == "__main__":
	blog_contents = sorted(os.listdir(REVIEWS))
	blog_json = {}
	
	counter = 0	
	for rawreview in blog_contents:
		review = readreview(rawreview)
		blog_json[counter] = create_review_object(review)
		counter += 1
	
	savefile = f"{BLOG_PATH}/reviews.json" 
	with open(savefile, "w") as f:
		f.write(json.dumps(blog_json))
		f.close()
	os.chmod(savefile, 0o755)

