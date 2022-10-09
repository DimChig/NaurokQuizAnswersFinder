import NaurokAnswerGetter
import PomahachAnswerGetter


from googlesearch import search

from difflib import SequenceMatcher


def getSimilarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


class RelatedResult:
    def __init__(self, value, question):
        self.value = value
        self.question = question

def getStrikeText(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

def searchAnswers(findby, site_filter):
    query_size = 3  # search results
    pause_delay = 3  # time between queries

    site_naurok = "naurok.com.ua"
    site_pomahach = "pomahach.com"

    most_related_results = []
    max_similarity_value = (float)(0)
    max_question_similarity = None
    max_answer_similarity = None

    query = ("\"" + findby + "\" " + site_filter).strip()
    #tld=co.in
    s = query + "\n"
    links = []
    for j in search(query, tld="com", num=query_size, stop=query_size, pause=pause_delay):
        links.append(str(j)[0:100])
        if site_naurok in str(j):
            url = str(j).replace(".html", "") + "/print"
            quests = NaurokAnswerGetter.getQuests(url, site_naurok)
            if len(quests) == 0:
                continue
            # load correct answers
            # for q in quests:
            #     print("", q.idx, ") ", q.question)
            #     for a in q.answers:
            #         print("\t", a.letter, ") ", a.text, " -> ", a.isCorrect)


            for q in quests:
                dist = getSimilarity(q.question, findby)

                if dist > max_similarity_value:
                    max_similarity_value = dist
                    max_question_similarity = q
                    max_answer_similarity = None

                for a in q.answers:
                    dist = getSimilarity(a.text, findby)

                    if dist > max_similarity_value:
                        max_similarity_value = dist
                        max_question_similarity = None
                        max_answer_similarity = a

            q = max_question_similarity
            if max_answer_similarity is not None:
                q = max_answer_similarity.question

            if q is not None:
                most_related_results.append(RelatedResult(max_similarity_value, q))


        if site_pomahach in str(j):
            quest = PomahachAnswerGetter.getQuestion(str(j), site_pomahach)
            if quest is None:
                continue
            dist = getSimilarity(quest.question, findby)

            if dist > max_similarity_value:
                max_similarity_value = dist
                max_question_similarity = quest
                max_answer_similarity = None

            for a in quest.answers:
                dist = getSimilarity(a.text, findby)

                if dist > max_similarity_value:
                    max_similarity_value = dist
                    max_question_similarity = None
                    max_answer_similarity = a

            if quest is not None:
                most_related_results.append(RelatedResult(max_similarity_value, quest))


    most_related_results.sort(key=lambda x: x.value, reverse=True)

    s += "\n"
    for q in most_related_results:

        s += str((int)(q.value * 100)) + ", " + q.question.site_source + ":\n"
        s += q.question.question + "\n"

        q.question.answers.sort(key=lambda x: x.isCorrect, reverse=True)
        for a in q.question.answers:
            if a.isCorrect:
                s += "\t" + str(a.text) + " (" + str(a.letter) + ")\n"
            else:
                s += "\t" + getStrikeText(a.text) + " (" + str(a.letter) + ")\n"
            #print(color, "\t", a.text + "\033[0m")
        s += "\n\n"
    s += "\n\n\n"
    for link in links:
        s += link + "\n"
    return s
