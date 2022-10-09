import requests
from bs4 import BeautifulSoup
quests = []

def getQuestion(url, site_source):
    resp = requests.get(url)
    if resp.status_code != 200:
        print("STATUS " + str(resp.status_code),":\n\t" + url)
        return None

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

    #fill question
    if len(soup.select(".panel-body")) == 0: return None
    question = soup.select(".panel-body")[0].text.strip()
    quest = Quest(site_source, 0, question, [])
    cnt = 1
    for e in list(soup.select("#spoiler-1 .list-group")[0].select("li")):
        answer = e.text.replace("\n","").strip()
        quest.answers.append(Answer(quest, answer, cnt, False))
        cnt += 1
    for e in list(soup.select("#spoiler-1 .list-group")[0].select("li.list-group-item-success")):
        correct_answer = e.text.replace("\n","").strip()
        for a in quest.answers:
            if a.text == correct_answer:
                a.isCorrect = True

    return quest
