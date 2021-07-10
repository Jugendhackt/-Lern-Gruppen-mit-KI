from flask import Flask, render_template, request

app = Flask(__name__)
counterFragen = 0

@app.route("/", methods=['GET', 'POST'])

def index():
    global counterFragen


    fragen = ["welchen Schultyp besuchst du? ", "Zu welcher Altergruppe gehörst du?", "Ich brauche Hilfe in..."
            ,"Welcher Lerntyp bist du?", "Mein/e Hobbies sind eher...","meine Stärken sind","meine Schwächen sind"]

    print(counterFragen)
    fragenNummer = "Frage " + str(counterFragen + 1)
    if counterFragen == 0:
        möglichkeiten = ["Gymnasium", "Realschule", "Hauptschule", "Gesammtschule"]
        test = """<input type="checkbox" id="3" name="hello" value="Frage 3">
                    <label for="3">""" + möglichkeiten[3] + """</label><br><br>"""

    print(request.form.getlist('hello'))

    if "close2" in request.form:
        print("Hello2")
    elif "Bestätigen" in request.form:

        init = 1
        counterFragen = counterFragen + 1

        if counterFragen == 1:
            möglichkeiten = ["10-13", "14-16", "17-18"]
            test = ""

        if counterFragen == 2:
            möglichkeiten = ["Deutsch", "Englisch", "Mathematik","Französisch"]
            test = """<input type="checkbox" id="3" name="hello" value="Frage 3">
            <label for="3">"""+möglichkeiten[3]+"""</label><br><br>"""
        if counterFragen == 3:
            möglichkeiten = ["durch Hören", "durch Lesen", "durch physisches Anfassen"]
            test = ""
        if counterFragen == 4:
            möglichkeiten = ["Sport orientiert", "intelektuell orientiert", "künstlerisch","Ich habe keine Hobbies"]
            test = """<input type="checkbox" id="3" name="hello" value="Frage 3">
            <label for="3">"""+möglichkeiten[3]+"""</label><br><br>"""


        fragenNummer = "Frage " + str(counterFragen + 1)

    return render_template("index.html", Tittel=fragenNummer, content=fragen[counterFragen],
                           möglichkeiten=möglichkeiten, test = test)


if __name__ == "__main__":
    app.run()
