import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
quests = []

def getQuests(url, site_source):
    headers = CaseInsensitiveDict()
    session = "f6t8moh0rhm6ev7qittmnnqgdp" #random account
    headers["Cookie"] = "PHPSESSID=" + session


    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        #print("STATUS " + str(resp.status_code),":\n\t" + url)
        return []
    if resp.url == "https://naurok.com.ua/login":
        print("LOGIN FAILED")
        return []

    data = resp.text

    class Quest:
        def __init__(self, site_source, idx, question, answers):
            self.site_source = site_source
            self.idx = idx
            self.question = question
            self.answers = answers

    class Answer:
        def __init__(self, question, text, letter, isCorrect):
            self.question = question
            self.text = text
            self.letter = letter
            self.isCorrect = isCorrect

    soup = BeautifulSoup(data, "html.parser")
    questions = []

    #fill questions
    for e in list(soup.select(".questions-list .question-view-item")):
        idx = (int)(e.select(".q-num")[0].text.replace("\n","").replace(".", "").strip())
        question = e.select(".no-padding")[0].find("p").text.strip()

        quest = Quest(site_source, idx, question, [])

        answer_block = e.select(".no-padding .question-options")[0]
        for a in list(answer_block.select(".text-only-option")):
            text = a.select(".option-text p")[0].text.replace("\n","").strip()
            letter = a.select(".option-letter")[0].text.replace(")", "").strip()
            quest.answers.append(Answer(quest, text, letter, False))

        questions.append(quest)

    for e in list(soup.select(".answer-key div")):
        #print("Answer: ",e.text)
        s = e.text

        q_idx = (int)(s.split(".")[0].strip())
        letters = s.split(".")[1].strip().split("(")[0].strip().split(" ")
        #assign
        for q in questions:
            if q.idx == q_idx:
                for letter in letters:
                    b = False
                    for a in q.answers:
                        if a.letter == letter:
                            a.isCorrect = True
                            b = True
                            break
                    if b == False:
                        q.answers.append(Answer(q, "Зображення", letter, True))
    return questions

