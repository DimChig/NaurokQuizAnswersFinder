# NaurokQuizAnswersFinder

This project is a quiz answer finder for "Naurok," a Ukrainian quiz site similar to Kahoot. Most of the test questions are publicly accessible, so by searching with the right query, you can often find the answers. This code automates that process.

## About the Project

- **Purpose**: Developed for quickly finding answers to quiz questions on Naurok by searching online.
- **Background**: My first project using Google Search and Python.
- **Origin**: Created when I was 15yo (in 10th grade).
- **Development Time**: Built in around 3 days, working 1-2 hours a day.
- **Libraries Used**: `requests`, `BeautifulSoup`, `googlesearch`, `tkinter`, `difflib`.

## How It Works

1. **Google Search**: The program initiates a Google search with a given query, filtering results to Naurok’s site using `"site:naurok.com.ua"`.
2. **Parsing Results**: It retrieves relevant tests and extracts questions and answers using an HTML parser.
3. **Sorting by Relevance**: The results are sorted by similarity score, making it easy to find the most relevant answer.
4. **GUI Display**: All data is displayed in a Tkinter GUI, providing quick access to answers.

This project taught me how to use Google search techniques and HTML parsing effectively. It’s a practical tool for quickly finding answers on Naurok.

## Program Screenshot

![Program Screenshot](screen1.jpg?raw=true)
