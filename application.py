#Importation of libraries required for web app creation and funtionality
import random
from flask import Flask, render_template,request,jsonify
app = Flask(__name__)


#Creation of home page
@app.route("/")
def main():
    return render_template("home.html")

#Creation of Select page
@app.route("/select.html")
def SelectOption():
    return render_template("select.html")

#Creation of Section1page
@app.route("/r1.html")
def SelectOption1():

#Section1 random phrase generator
    words = ["Mwashibukeni?",
    " Mwaikaleni?",
    "Mwapoleeni?",
    "Mwabombeni?",
    " Muli Shaani?",
    "Mwashibukashaani",
    "Mwaikalashaani",
    "Mwabombashaani",
    "kung'anda kulishaani ",
    "Eya Mukwai",
    "Bwino",
    "Ndifye Bwino",
    "Ninevo Brian",
    "Shani Naimwe",
    "Chawama uku monana",
    "Uyu Munandi Brian",
    "Ine Ninevo Martha, Ninevo Teacher",
    "Uyu Ni Maria, Ni News Reporter",
    "Nga iwe Niwevo nani Ishina"
    "nkashi wakwe aliba bwino",
    "amoneka nga tom",
    "ala sekesha sana",
    "uyu muntu na fwala jean na shirt",
    "ali kwata imishishi ishitali",
    "ninshitanshi",
    "milo naile pa mall",
    "na shitile utuputula",
    "nali kunanda nale wamya munanda",
                         ]
    data = random.choice(words)
    return render_template("r1.html", value = data)

#Creation of Section2Page
@app.route("/r2.html")
def SelectOption2():

#Section2 random page generator
    words = ["ndangala naba nandi",
    "bushe bala teya bola",
    "ala isa kumyesu",
    "wakwata ba nkashi wobe na ba ndume bobe",
    "ucita shani ifyo",
    "ukwete umwaka shinga",
    "bushe a fuma ku lusaka",
    "ichi cipuna",
    "a sambila mu shower noku suka ameno",
    "munandi","twaba five mu ndupwa wesu",
    "be kala ku lusaka",
    "ba ya na bus ku sukulu yonse",
    "aba ni bambuya bandi",
    "finshi ucita nga wa kombaka ku sukulu",
    "cinshi ico",
    "finshi fili muci bokoshi umo",
    "ninshitanshi wambo ku bomba",
    "mu bomba kwisa",
    "keith ali kwisa",
    "ni nani uyu",
    "nali temwa ama film",
    "umulumedo ale samfya motoka",
    "ale tamba tv",
    "ale belenga book ya ku sukulu",
    "ba teacher ba le lemba pa board",
    "ba tata ba tali",]
    data = random.choice(words)
    return render_template("r2.html", value = data)

#Creation of Section3Page
@app.route("/r3.html")
def SelectOption3():

#Section3 random page generator
    words = ["ndeya muku teya ama cards naba nandi",
    "nani uwalanganfulishaku ne chakulya",
    "ule umfwako shani lelo",
    "uli fye bwino",
    "james ali pona aikontolola nomu boko",
    "a fyelwe ku lusaka mu 1984",
    "Ni lilali mwa selele kuya ku ndola""elo nali umwaice",
    "fyakulya inshi mwa temwa",
    "Na temwa kapenta na beans",
    "wushe natasha ali temwa bola",
    "na mukwata ko efipyango",
    "wushe jessica ali upwa",
    "ifi fyakufwala na fi uma",
    "tafila umwa",
    "ali panse ale teya bola",
    "tuka kwata party",
    "chawama uku landa nobe",
    "uli mulubilo uku ya",
    "natotela sana kabili na temwa uku landa nobe",
    "kuti na kwipushako cimo",
    "bushe u bomba kuno",
    "bushe nau fisanga efyo wachila fwaya",
    "wa fuma kwi","na fuma ku  lusaka",
    "wali mwishiba alan",
    "Airtime namu kwata",]
    data = random.choice(words)
    return render_template("r3.html", value = data)

#Creation of Dictionary/reference page
@app.route("/reference.html")
def SelectOption4():
    return render_template("reference.html")

#Creation of Instructions page
@app.route("/instructions.html")
def SelectOption5():
    return render_template("instructions.html")




