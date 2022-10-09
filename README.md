# NaurokQuizAnswersFinder
There is a quiz site (like kahoot.it) but ukrainian version called "Naurok". All tests are commonly in open source, so you can google your question and find similar questions with correct answers. This is exactly what this code does

About project:
- This was my first work with google search and python
- I created this program for completing my tests when i was 15 years old (10th grade)
- It took me around 3 days to make it (1-2 hours a day)
- I used python libraries: requests, BeautifulSoup, googlesearch, tkinter, difflib

Project development:
- With given query I initiate a google search, and find all matches using site filters (such as "site:naurok.com.ua")
- I receive list of tests, and find all most similar questions with answers (using html parser)
- Sort by similarity score and display all data in tkinter gui
- This is very usefull for fast answers finding
This was a very good project for me to learn how to use google searches and html parsers

Program screenshot:

![](screen1.jpg?raw=true)
