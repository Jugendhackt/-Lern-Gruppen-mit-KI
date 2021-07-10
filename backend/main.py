from flask import Flask, render_template, request
import json

app = Flask(__name__)
counterFragen = 0
antworten = []
def write_Json(antwortenLocal, name):
    aList = [{name: antwortenLocal}]
    jsonString = json.dumps(aList)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonString+"\n")
    jsonFile.close()

@app.route("/", methods=['GET', 'POST'])


def index():
    global counterFragen
    global antworten

    fragen = ["welchen Schultyp besuchst du? ", "Zu welcher Altergruppe gehörst du?", "Ich brauche Hilfe in..."
        , "Welcher Lerntyp bist du?", "Mein/e Hobbies sind eher...", "meine Stärken sind", "meine Schwächen sind"]

    print(counterFragen)
    fragenNummer = "Frage " + str(counterFragen + 1)
    if 0 == 0:
        möglichkeiten = ["Gymnasium", "Realschule", "Hauptschule", "Gesammtschule"]
        test = """<input type="checkbox" id="3" name="hello" value="Frage 3">
                    <label for="3">""" + möglichkeiten[3] + """</label><br><br>"""
    print(request.form.getlist('hello'))

    if "Bestätigen" in request.form:
        antwort = request.form.getlist('hello')
        print(int(antwort[0]))
        init = int(antwort[0])
        antworten.append(init)
        counterFragen = counterFragen + 1
        if counterFragen == 1:
            möglichkeiten = ["10-13", "14-16", "17-18"]
            test = ""

        if counterFragen == 2:
            möglichkeiten = ["Deutsch", "Englisch", "Mathematik", "Französisch"]
            test = """<input type="checkbox" id="3" name="hello" value="3">
            <label for="3">""" + möglichkeiten[3] + """</label>"""
        if counterFragen == 3:
            möglichkeiten = ["durch Hören", "durch Lesen", "durch physisches Anfassen"]
            test = ""
        if counterFragen == 4:
            möglichkeiten = ["Sport orientiert", "intelektuell orientiert", "künstlerisch", "Ich habe keine Hobbies"]
            test = """<input type="checkbox" id="3" name="hello" value="3">
            <label for="3">""" + möglichkeiten[3] + """</label>"""
        if counterFragen == 5:
            möglichkeiten = ["Ich kann schnell neues lernen", "Ich habe ein gutes Gedächtniss", "Ich kann gut zuhören",
                             "Ich bin organisiert"]
            test = """<input type="checkbox" id="3" name="hello" value="3">
            <label for="3">""" + möglichkeiten[3] + """</label>"""
        if counterFragen == 6:
            möglichkeiten = ["Ich kann mich schlecht/nicht konzentrieren", "Ich bin unorganisiert",
                             "Ich kann nicht gut zuhören", "Ich brauche viel Zeit beim Lernen"]
            test = """<input type="checkbox" id="3" name="hello" value="3">
            <label for="3">""" + möglichkeiten[3] + """</label>"""
        fragenNummer = "Frage " + str(counterFragen + 1)
        if counterFragen == 7:
            write_Json(antworten, "hans")

    return render_template("index.html", Tittel=fragenNummer, content=fragen[counterFragen],
                           möglichkeiten=möglichkeiten, test=test)


if __name__ == "__main__":
    app.run()
