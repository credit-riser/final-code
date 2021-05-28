from flask import Flask, render_template, request
import requests
import io
import random
import names
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
# import matplotlib.pyplot as plt
# import numpy as np
from flask_table import Table, Col

app = Flask(__name__)
globalScore = 0
globalSatisfaction = ""
globalTransactions = "transact"

customerBefore = 0
customerAfter = 0
sampleBefore = 0
sampleAfter = 0
itemsCustomer = []
itemsSample = []


class ItemTable(Table):
    name = Col('Item')
    description = Col('Cutting Cost')

class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
# items = [Item('Name1', 'Description1'),
#          Item('Name2', 'Description2'),
#          Item('Name3', 'Description3')]
# # Or, equivalently, some dicts
# items = [dict(name='Name1', description='Description1'),
#          dict(name='Name2', description='Description2'),
#          dict(name='Name3', description='Description3')]

tableCustomer = ItemTable(itemsCustomer)
tableSample = ItemTable(itemsSample)


@app.route('/home')
def home1():
        global itemsCustomer 
        global itemsSample
        global tableCustomer
        global tableSample

        itemsCustomer = []
        itemsSample = []
        tableCustomer = ItemTable(itemsCustomer)
        tableSample = ItemTable(itemsSample)
        return render_template('index.html')

@app.route('/about')
def about():
        global itemsCustomer 
        global itemsSample
        global tableCustomer
        global tableSample

        itemsCustomer = []
        itemsSample = []
        tableCustomer = ItemTable(itemsCustomer)
        tableSample = ItemTable(itemsSample)
        return render_template('about.html')

@app.route('/')
def home():
    global itemsCustomer 
    global itemsSample
    global tableCustomer
    global tableSample

    itemsCustomer = []
    itemsSample = []
    tableCustomer = ItemTable(itemsCustomer)
    tableSample = ItemTable(itemsSample)
    return render_template('index.html', news={})

def dataanalysis(aftercredit, spending):
    global customerBefore
    global customerAfter
    global sampleBefore
    global sampleAfter
    inputdata = {'Helen Barnes': {'before': {'car': 200, 'utilities': 490, 'pets': 145, 'rent': 6470, 'miscellaneous': 241}, 'beforecredit': 652.5049999999999}, 'Steven Madsen': {'before': {'car': 110, 'gasoline': 406, 'loan': 3560, 'eating out': 50, 'utilities': 350}, 'beforecredit': 698.5600000000001}, 'Mary Lefevre': {'before': {'loan': 110}, 'beforecredit': 715.0}, 'Jovita Ricks': {'before': {'loan': 6900, 'pets': 455}, 'beforecredit': 688.51}, 'Terry Lane': {'before': {'pets': 305, 'sports games': 100}, 'beforecredit': 720.88}, 'Scott Slover': {'before': {'sports games': 530, 'pets': 565, 'eating out': 1260, 'utilities': 350, 'car': 440}, 'beforecredit': 682.39}, 'Eugene Leger': {'before': {'car': 170, 'cell phone': 163, 'gasoline': 308, 'loan': 2390, 'rent': 5690}, 'beforecredit': 651.34}, 'Ricky Fisher': {'before': {'rent': 1600, 'medical': 830, 'renovation': 7720, 'cell phone': 116, 'loan': 610}, 'beforecredit': 598.4}, 'Linda Schwarz': {'before': {'medical': 870, 'gasoline': 494}, 'beforecredit': 658.74}, 'James Natale': {'before': {'medical': 550, 'miscellaneous': 929, 'eating out': 1010, 'utilities': 90, 'gasoline': 186, 'movies': 1213, 'sports games': 370}, 'beforecredit': 675.825}, 'Eric Johnston': {'before': {'groceries': 644, 'miscellaneous': 125}, 'beforecredit': 707.995}, 'Michael Austin': {'before': {'miscellaneous': 889, 'utilities': 450, 'rent': 3420}, 'beforecredit': 676.805}, 'Clifford Bronner': {'before': {'miscellaneous': 827, 'medical': 640, 'sports games': 580, 'pets': 295, 'loan': 710}, 'beforecredit': 670.525}, 'Donald Liao': {'before': {'pets': 535,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'eating out': 1160, 'renovation': 6740}, 'beforecredit': 648.58}, 'Bobby Busby': {'before': {'renovation': 7690, 'groceries': 883, 'car': 280, 'movies': 2563}, 'beforecredit': 612.8100000000001}, 'Leona Carpenter': {'before': {'movies': 1893, 'rent': 3440, 'gasoline': 95}, 'beforecredit': 671.32}, 'Mary Michell': {'before': {'gasoline': 435, 'sports games': 500, 'rent': 2410, 'renovation': 1950, 'groceries': 347}, 'beforecredit': 674.53}, 'Jennifer Moon': {'before': {'gasoline': 236, 'medical': 610}, 'beforecredit': 682.06}, 'Brandi Norwood': {'before': {'medical': 840, 'loan': 4910, 'groceries': 1348, 'rent': 2990, 'movies': 103, 'pets': 245, 'utilities': 180}, 'beforecredit': 624.3199999999999}, 'Quinton Hall': {'before': {'movies': 1183, 'renovation': 1040}, 'beforecredit': 699.77}, 'Tamiko Faust': {'before': {'movies': 2763, 'eating out': 1650}, 'beforecredit': 682.82}, 'Adrian Hernandez': {'before': {'movies': 143, 'miscellaneous': 448, 'medical': 160}, 'beforecredit': 705.83}, 'Mildred Carrasquillo': {'before': {'medical': 50, 'renovation': 3640, 'pets': 735, 'movies': 1163, 'groceries': 1329}, 'beforecredit': 654.33}, 'Virginia Kurylo': {'before': {'renovation': 4620, 'movies': 513, 'rent': 5660, 'eating out': 70, 'miscellaneous': 60, 'cell phone': 125, 'car': 280, 'pets': 585, 'utilities': 150}, 'beforecredit': 620.4599999999999}, 'Earl Bell': {'before': {'groceries': 977, 'cell phone': 28, 'renovation': 2020, 'sports games': 670, 'eating out': 600, 'miscellaneous': 308, 'utilities': 350, 'loan': 90}, 'beforecredit': 684.2700000000002}, 'Barry Koopmans':
                {'before': {'groceries': 792, 'renovation': 1800, 'rent': 1120, 'gasoline': 483, 'miscellaneous': 408, 'eating out': 1220}, 'beforecredit': 680.9799999999999}, 'Michelle Honokaupu': {'before': {'groceries': 1156, 'car': 520, 'utilities': 180, 'movies': 1363}, 'beforecredit': 664.3}, 'Lester Vacheresse': {'before': {'groceries': 440, 'rent': 720, 'cell phone': 125, 'car': 490}, 'beforecredit': 691.9}, 'Angelica Whisenand': {'before': {'car': 310, 'cell phone': 130}, 'beforecredit': 705.0}, 'Frieda Moss': {'before': {'cell phone': 72, 'gasoline': 326, 'utilities': 460, 'medical': 440, 'pets': 485, 'eating out': 1290, 'groceries': 476}, 'beforecredit': 675.9}, 'Latoya Lindauer': {'before': {'cell phone': 77}, 'beforecredit': 711.3}, 'Eddie Wells': {'before': {'cell phone': 128}, 'beforecredit': 706.2}, 'David Fawcett': {'before': {'cell phone': 154, 'loan': 4310, 'sports games': 120, 'gasoline': 434}, 'beforecredit': 692.0400000000001}, 'Alesia Mcnair': {'before': {'sports games': 780, 'car': 210}, 'beforecredit': 700.3}, 'Caroline Brown': {'before': {'sports games': 600, 'eating out': 980}, 'beforecredit': 702.12}, 'Michael Bernard': {'before': {'sports games': 920, 'miscellaneous': 436, 'renovation': 5870, 'medical': 160, 'loan': 3300}, 'beforecredit': 628.45}}
    data = []
    creditcalc = {
        "car": {
            "medium": 300,
            "lower": .05,
            "higher": -.1
        },
        "rent": {
            "medium": 1100,
            "lower": .01,
            "higher": -.01
        },
        "utilities": {
            "medium": 215,
            "lower": .03,
            "higher": -.03
        },
        "miscellaneous": {
            "medium": 100,
            "lower": .01,
            "higher": -.005
        },
        "cell phone": {
            "medium": 80,
            "lower": .1,
            "higher": -.1
        },
        "groceries": {
            "medium": 500,
            "lower": .01,
            "higher": -.02
        },
        "eating out": {
            "medium": 100,
            "lower": .03,
            "higher": -.001
        },
        "loan": {
            "medium": 510,
            "lower": .01,
            "higher": -.003
        },
        "gasoline": {
            "medium": 150,
            "lower": .03,
            "higher": -.04
        },
        "pets": {
            "medium": 40,
            "lower": .01,
            "higher": -.008
        },
        "movies": {
            "medium": 100,
            "lower": .04,
            "higher": -.01
        },
        "sports games": {
            "medium": 400,
            "lower": .04,
            "higher": -.04
        },
        "renovation": {
            "medium": 1000,
            "lower": .01,
            "higher": -.01
        },
        "medical": {
            "medium": 100,
            "lower": .05,
            "higher": -.05
        },
    }
    size = 10
    
    dataname = "Helen Barnes"
    additionalcredit = 0.0
    lessmoney = []
    for element in spending.keys():
        if creditcalc[element]["medium"] < spending[element]:
            extra = (spending[element] - creditcalc[element]["medium"])
            lessmoney.append("cut $" + str(extra) + " on " + str(element))
            itemsCustomer.append(dict(name=str(element), description=str(extra)))
            additionalcredit -= creditcalc[element]["higher"]*extra
    additionalcredit1 = 0.0
    lessmoney1 = []
    if dataname != "default":
        for element in inputdata[dataname]['before'].keys():
            if creditcalc[element]["medium"] < inputdata[dataname]['before'][element]:
                sampleBefore = inputdata[dataname]['beforecredit']
                extra = (inputdata[dataname]['before'][element] -
                         creditcalc[element]["medium"])
                lessmoney1.append(", cutting $" + str(extra) +
                                  " on " + str(element))
                itemsSample.append(dict(name=str(element), description=str(extra)))
                additionalcredit1 -= creditcalc[element]["higher"]*extra
                sampleAfter = sampleBefore + additionalcredit1
                if sampleAfter > 850:
                    sampleAfter = 850
    finalvalue = "If you "
    counter3 = 0
    for element in lessmoney:
        finalvalue += element
        if len(lessmoney) > counter3 + 1:
            finalvalue += " and "
        counter3 += 1
    customerAfter = float(str(aftercredit + additionalcredit))
    if customerAfter > 850:
        customerAfter = 850
    finalvalue += ", your credit score will increase from " + \
        str(aftercredit) + " to " + str(aftercredit + additionalcredit)
    if dataname != "default":
        finalvalue += " just like some other user who increased their credit by " + \
            str(int(additionalcredit1)) + " by "
        counter3 = 0
        for element in lessmoney1:
            finalvalue += element
            if len(lessmoney) > counter3:
                finalvalue += " "
            counter3 += 1
    finalvalue += "."
    print(inputdata)
    return finalvalue

@app.route('/info/',methods=['POST']) 
def displayinfo():
    global customerBefore
    global customerAfter
    global sampleBefore
    global sampleAfter
    score = int(request.form['score'])
    satisfaction = request.form['satisfaction']
    transactions = request.form['transact']
    satisfactionScore = 0
    if("like" in satisfaction or "happy" in satisfaction or "good" in satisfaction or "love" in satisfaction):
        satisfactionScore = 1
    elif("bad" in satisfaction or "not" in satisfaction or "hate" in satisfaction):
        satsifactionScore = -1
    else:
        satisfactionScore = 0

    #initial credit score
    initScore = score
    #bad transactions
    transList = transactions.split(", ")
    transDict = {}
    
    for trans in transList:
        newDict = trans.split(": ")
        item = newDict[0]
        cost = int(newDict[1])
        transDict[item]=cost
    #credit: 680, car: 600, rent: 6000, utilities: 200
    newTransactions= dataanalysis(score, transDict)
    customerBefore = score
        
    scoreQuality = ""
    stockdict = {}
    if(score<300 or score>850):
        stockdict[0] = "Please enter a credit score in the range of 300 to 850."
    elif(score>800 and satisfactionScore == 1):
        stockdict[0] = "Your credit score is above 800 and you are happy with it. Great job!"
    elif(score>700 and satisfactionScore == 1):
        stockdict[0] = "Your score is above 700 and you are happy with it. Well done."
    elif(score < 700):
        stockdict[0] = "Your credit score is less than 700, so there is room for improvement."
        stockdict[1] = "Here is a set of transactions you can do to improve your credit score:"
        stockdict[2] = newTransactions
    else:
        stockdict[0] = "Your credit score is good, but you would like to improve it."
        stockdict[1] = "Here is a set of transactions you can do to improve your credit score:"
        stockdict[2] = newTransactions
    
    # print(stockdict)
    #Send the articles to the html file to display in a user-friendly format
    tableCustomer = ItemTable(itemsCustomer)
    tableSample = ItemTable(itemsSample)
    return render_template('results.html',news=stockdict, tableCustomer=tableCustomer, tableSample=tableSample)

@app.route('/info/home')
def home_info():
        global itemsCustomer 
        global itemsSample
        global tableCustomer
        global tableSample

        itemsCustomer = []
        itemsSample = []
        tableCustomer = ItemTable(itemsCustomer)
        tableSample = ItemTable(itemsSample)

        return render_template('index.html')

@app.route('/info/about')
def about_info():
        global itemsCustomer 
        global itemsSample
        global tableCustomer
        global tableSample

        itemsCustomer = []
        itemsSample = []
        tableCustomer = ItemTable(itemsCustomer)
        tableSample = ItemTable(itemsSample)
        return render_template('about.html')

# table = ItemTable(items)
# print(table.__html__())

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    global customerBefore
    global customerAfter
    global sampleBefore
    global sampleAfter
    print('customerBefore: ', customerBefore)
    print('customerAfter: ', customerAfter)
    print('sampleBefore: ', sampleBefore)
    print('sampleAfter: ', sampleAfter)
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    # xs = range(100)
    xs = ['Before', 'After']
    # ys = [random.randint(1, 50) for x in xs]
    ysCustomer = [customerBefore, customerAfter]
    # ysCustomer = [100, 200]
    axis.plot(xs, ysCustomer, label='You', color='red')
    ysSample = [sampleBefore, sampleAfter]
    # ysSample = [120, 220]
    axis.plot(xs, ysSample, label='Similar Customer')
    axis.set_title('Change in Credit Score with Credit Riser over Time')
    axis.set_xlabel('Stages')
    axis.set_ylabel('Credit Score')
    axis.legend()
    axis.autoscale()
    # axis.set_ylim([500, 800])
    # axis.show()
    return fig
    # x = np.linspace(0.0, 5.0, 501)

    # fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True, sharey=True)
    # ax1.plot(x, np.cos(6*x) * np.exp(-x))
    # ax1.set_title('damped')
    # ax1.set_xlabel('time (s)')
    # ax1.set_ylabel('amplitude')

    # ax2.plot(x, np.cos(6*x))
    # ax2.set_xlabel('time (s)')
    # ax2.set_title('undamped')

    # fig.suptitle('Different types of oscillations', fontsize=16)
# from flask import Flask,render_template,request
# import requests
# import io
# import random
# import names
# from flask import Response
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# # import matplotlib.pyplot as plt
# # import numpy as np

# app = Flask(__name__)
# globalScore = 0
# globalSatisfaction = ""
# globalTransactions = "transact"

# @app.route('/')
# def home():
#     return render_template('index.html', news={})

# def dataanalysis(aftercredit, spending):
#     inputdata = {'Helen Barnes': {'before': {'car': 200, 'utilities': 490, 'pets': 145, 'rent': 6470, 'miscellaneous': 241}, 'beforecredit': 652.5049999999999}, 'Steven Madsen': {'before': {'car': 110, 'gasoline': 406, 'loan': 3560, 'eating out': 50, 'utilities': 350}, 'beforecredit': 698.5600000000001}, 'Mary Lefevre': {'before': {'loan': 110}, 'beforecredit': 715.0}, 'Jovita Ricks': {'before': {'loan': 6900, 'pets': 455}, 'beforecredit': 688.51}, 'Terry Lane': {'before': {'pets': 305, 'sports games': 100}, 'beforecredit': 720.88}, 'Scott Slover': {'before': {'sports games': 530, 'pets': 565, 'eating out': 1260, 'utilities': 350, 'car': 440}, 'beforecredit': 682.39}, 'Eugene Leger': {'before': {'car': 170, 'cell phone': 163, 'gasoline': 308, 'loan': 2390, 'rent': 5690}, 'beforecredit': 651.34}, 'Ricky Fisher': {'before': {'rent': 1600, 'medical': 830, 'renovation': 7720, 'cell phone': 116, 'loan': 610}, 'beforecredit': 598.4}, 'Linda Schwarz': {'before': {'medical': 870, 'gasoline': 494}, 'beforecredit': 658.74}, 'James Natale': {'before': {'medical': 550, 'miscellaneous': 929, 'eating out': 1010, 'utilities': 90, 'gasoline': 186, 'movies': 1213, 'sports games': 370}, 'beforecredit': 675.825}, 'Eric Johnston': {'before': {'groceries': 644, 'miscellaneous': 125}, 'beforecredit': 707.995}, 'Michael Austin': {'before': {'miscellaneous': 889, 'utilities': 450, 'rent': 3420}, 'beforecredit': 676.805}, 'Clifford Bronner': {'before': {'miscellaneous': 827, 'medical': 640, 'sports games': 580, 'pets': 295, 'loan': 710}, 'beforecredit': 670.525}, 'Donald Liao': {'before': {'pets': 535,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'eating out': 1160, 'renovation': 6740}, 'beforecredit': 648.58}, 'Bobby Busby': {'before': {'renovation': 7690, 'groceries': 883, 'car': 280, 'movies': 2563}, 'beforecredit': 612.8100000000001}, 'Leona Carpenter': {'before': {'movies': 1893, 'rent': 3440, 'gasoline': 95}, 'beforecredit': 671.32}, 'Mary Michell': {'before': {'gasoline': 435, 'sports games': 500, 'rent': 2410, 'renovation': 1950, 'groceries': 347}, 'beforecredit': 674.53}, 'Jennifer Moon': {'before': {'gasoline': 236, 'medical': 610}, 'beforecredit': 682.06}, 'Brandi Norwood': {'before': {'medical': 840, 'loan': 4910, 'groceries': 1348, 'rent': 2990, 'movies': 103, 'pets': 245, 'utilities': 180}, 'beforecredit': 624.3199999999999}, 'Quinton Hall': {'before': {'movies': 1183, 'renovation': 1040}, 'beforecredit': 699.77}, 'Tamiko Faust': {'before': {'movies': 2763, 'eating out': 1650}, 'beforecredit': 682.82}, 'Adrian Hernandez': {'before': {'movies': 143, 'miscellaneous': 448, 'medical': 160}, 'beforecredit': 705.83}, 'Mildred Carrasquillo': {'before': {'medical': 50, 'renovation': 3640, 'pets': 735, 'movies': 1163, 'groceries': 1329}, 'beforecredit': 654.33}, 'Virginia Kurylo': {'before': {'renovation': 4620, 'movies': 513, 'rent': 5660, 'eating out': 70, 'miscellaneous': 60, 'cell phone': 125, 'car': 280, 'pets': 585, 'utilities': 150}, 'beforecredit': 620.4599999999999}, 'Earl Bell': {'before': {'groceries': 977, 'cell phone': 28, 'renovation': 2020, 'sports games': 670, 'eating out': 600, 'miscellaneous': 308, 'utilities': 350, 'loan': 90}, 'beforecredit': 684.2700000000002}, 'Barry Koopmans':
#                 {'before': {'groceries': 792, 'renovation': 1800, 'rent': 1120, 'gasoline': 483, 'miscellaneous': 408, 'eating out': 1220}, 'beforecredit': 680.9799999999999}, 'Michelle Honokaupu': {'before': {'groceries': 1156, 'car': 520, 'utilities': 180, 'movies': 1363}, 'beforecredit': 664.3}, 'Lester Vacheresse': {'before': {'groceries': 440, 'rent': 720, 'cell phone': 125, 'car': 490}, 'beforecredit': 691.9}, 'Angelica Whisenand': {'before': {'car': 310, 'cell phone': 130}, 'beforecredit': 705.0}, 'Frieda Moss': {'before': {'cell phone': 72, 'gasoline': 326, 'utilities': 460, 'medical': 440, 'pets': 485, 'eating out': 1290, 'groceries': 476}, 'beforecredit': 675.9}, 'Latoya Lindauer': {'before': {'cell phone': 77}, 'beforecredit': 711.3}, 'Eddie Wells': {'before': {'cell phone': 128}, 'beforecredit': 706.2}, 'David Fawcett': {'before': {'cell phone': 154, 'loan': 4310, 'sports games': 120, 'gasoline': 434}, 'beforecredit': 692.0400000000001}, 'Alesia Mcnair': {'before': {'sports games': 780, 'car': 210}, 'beforecredit': 700.3}, 'Caroline Brown': {'before': {'sports games': 600, 'eating out': 980}, 'beforecredit': 702.12}, 'Michael Bernard': {'before': {'sports games': 920, 'miscellaneous': 436, 'renovation': 5870, 'medical': 160, 'loan': 3300}, 'beforecredit': 628.45}}
#     data = []
#     creditcalc = {
#         "car": {
#             "medium": 300,
#             "lower": .05,
#             "higher": -.1
#         },
#         "rent": {
#             "medium": 1100,
#             "lower": .01,
#             "higher": -.01
#         },
#         "utilities": {
#             "medium": 215,
#             "lower": .03,
#             "higher": -.03
#         },
#         "miscellaneous": {
#             "medium": 100,
#             "lower": .01,
#             "higher": -.005
#         },
#         "cell phone": {
#             "medium": 80,
#             "lower": .1,
#             "higher": -.1
#         },
#         "groceries": {
#             "medium": 500,
#             "lower": .01,
#             "higher": -.02
#         },
#         "eating out": {
#             "medium": 100,
#             "lower": .03,
#             "higher": -.001
#         },
#         "loan": {
#             "medium": 510,
#             "lower": .01,
#             "higher": -.003
#         },
#         "gasoline": {
#             "medium": 150,
#             "lower": .03,
#             "higher": -.04
#         },
#         "pets": {
#             "medium": 40,
#             "lower": .01,
#             "higher": -.008
#         },
#         "movies": {
#             "medium": 100,
#             "lower": .04,
#             "higher": -.01
#         },
#         "sports games": {
#             "medium": 400,
#             "lower": .04,
#             "higher": -.04
#         },
#         "renovation": {
#             "medium": 1000,
#             "lower": .01,
#             "higher": -.01
#         },
#         "medical": {
#             "medium": 100,
#             "lower": .05,
#             "higher": -.05
#         },
#     }
#     size = 10
    
#     dataname = "Helen Barnes"
#     additionalcredit = 0.0
#     lessmoney = []
#     for element in spending.keys():
#         if creditcalc[element]["medium"] < spending[element]:
#             extra = (spending[element] - creditcalc[element]["medium"])
#             lessmoney.append("cut $" + str(extra) + " on " + str(element))
#             additionalcredit -= creditcalc[element]["higher"]*extra
#     additionalcredit1 = 0.0
#     lessmoney1 = []
#     if dataname != "default":
#         for element in inputdata[dataname]['before'].keys():
#             if creditcalc[element]["medium"] < inputdata[dataname]['before'][element]:
#                 extra = (inputdata[dataname]['before'][element] -
#                          creditcalc[element]["medium"])
#                 lessmoney1.append(", cutting $" + str(extra) +
#                                   " on " + str(element))
#                 additionalcredit1 -= creditcalc[element]["higher"]*extra
#     finalvalue = "If you "
#     counter3 = 0
#     for element in lessmoney:
#         finalvalue += element
#         if len(lessmoney) > counter3 + 1:
#             finalvalue += " and "
#         counter3 += 1
#     finalvalue += ", your credit score will increase from " + \
#         str(aftercredit) + " to " + str(aftercredit + additionalcredit)
#     if dataname != "default":
#         finalvalue += " just like some other user who increased their credit by " + \
#             str(int(additionalcredit1)) + " by "
#         counter3 = 0
#         for element in lessmoney1:
#             finalvalue += element
#             if len(lessmoney) > counter3:
#                 finalvalue += " and "
#             counter3 += 1
#     finalvalue += "."
#     print(inputdata)
#     return finalvalue

# @app.route('/info/',methods=['POST']) 
# def displayinfo():
#     score = int(request.form['score'])
#     satisfaction = request.form['satisfaction']
#     transactions = request.form['transact']
#     satisfactionScore = 0
#     if("like" in satisfaction or "happy" in satisfaction or "good" in satisfaction):
#         satisfactionScore = 1
#     elif("bad" in satisfaction or "not" in satisfaction or "hate" in satisfaction):
#         satsifactionScore = -1
#     else:
#         satisfactionScore = 0

#     #initial credit score
#     initScore = score;
#     #bad transactions
#     transList = transactions.split(", ")
#     transDict = {}
    
#     for trans in transList:
#         newDict = trans.split(": ")
#         item = newDict[0]
#         cost = int(newDict[1])
#         transDict[item]=cost
        
#     #credit: 680, car: 600, rent: 6000, utilities: 200
#     newTransactions= dataanalysis(score, transDict)
        
#     scoreQuality = ""
#     stockdict = {}
#     if(score<0 or score>850):
#         stockdict[0] = "Please enter a credit score in the range of 0 to 850."
#     elif(score>800 and satisfactionScore == 1):
#         stockdict[0] = "Your credit score is above 800 and you are happy with it. Great job!"
#     elif(score>700 and satisfactionScore == 1):
#         stockdict[0] = "Your score is above 700 and you are happy with it. Well done."
#     elif(score < 700):
#         stockdict[0] = "Your credit score is less than 700, so there is room for improvement."
#         stockdict[1] = "Here is a set of transactions you can do to improve your credit score:"
#         stockdict[2] = newTransactions
#     else:
#         stockdict[0] = "Your credit score is good, but you would like to improve it."
#         stockdict[1] = "Here is a set of transactions you can do to improve your credit score:"
#         stockdict[2] = newTransactions
    
#     # print(stockdict)
#     #Send the articles to the html file to display in a user-friendly format
#     return render_template('results.html',news=stockdict)


# @app.route('/plot.png')
# def plot_png():
#     fig = create_figure()
#     output = io.BytesIO()
#     FigureCanvas(fig).print_png(output)
#     return Response(output.getvalue(), mimetype='image/png')

# def create_figure():
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)
#     xs = range(100)
#     ys = [random.randint(1, 50) for x in xs]
#     axis.plot(xs, ys)
#     axis.set_title('title')
#     axis.set_xlabel('x-axis')
#     axis.set_ylabel('y-axis')
#     return fig
#     # x = np.linspace(0.0, 5.0, 501)

#     # fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True, sharey=True)
#     # ax1.plot(x, np.cos(6*x) * np.exp(-x))
#     # ax1.set_title('damped')
#     # ax1.set_xlabel('time (s)')
#     # ax1.set_ylabel('amplitude')

#     # ax2.plot(x, np.cos(6*x))
#     # ax2.set_xlabel('time (s)')
#     # ax2.set_title('undamped')

#     # fig.suptitle('Different types of oscillations', fontsize=16)