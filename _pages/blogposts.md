---
title: "Blog Posts"
permalink: /blogs/
author_profile: false
redirect_from:
  - /resume
  - /about/
  - /about.html
---

# Copying from one Google sheet to another google sheet
I am wondering why I cannot paste only values from one google sheet to another google sheet. I can paste the formualas (ctrl + v) works but (ctrl+ shift + v) does not work.

For example, consider I have a google spreadsheet file named as "Sheet1" with multiple sheets inside it, named "Alpha" and "Beta". I wanted to paste only the values of "Alpha" sheet to a new google spreadsheet file named as "Sheet2".

If I copy all the contents of "Alpha" sheet and do ctrl + shift + v in "Sheet2", it does not work. But if I do ctrl + v, it works but I am getting different values because of reference error.

Resolving this issue. Create a new temporary sheet "temp" in "Sheet1". I had to copy the contents of "Alpha" and do ctrl + shift + v in "temp". Then right click on "temp" and select "Copy to" and then "Existing spreadsheet" and select "Sheet2" going through all of my directories. Such a hassale process..!!

Why can't we do ctrl + shift + v in "Sheet2" directly? Why do we have to create a temporary sheet and then copy to "Sheet2"?
