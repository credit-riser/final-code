import csv
import random
import names


def dataanalysis(aftercredit, spending):

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
    size = 1000
    for i in range(size):
        data.append(['car', random.randrange(100, 700, 10)])

    for i in range(size):
        data.append(['rent', random.randrange(600, 8000, 10)])

    for i in range(size):
        data.append(['utilities', random.randrange(70, 500, 10)])

    for i in range(size):
        data.append(['miscellaneous', random.randrange(5, 1000, 1)])

    for i in range(size):
        data.append(['cell phone', random.randrange(20, 200, 1)])

    for i in range(size):
        data.append(['groceries', random.randrange(50, 1500, 1)])

    for i in range(size):
        data.append(['eating out', random.randrange(10, 2000, 10)])

    for i in range(size):
        data.append(['loan', random.randrange(10, 8000, 10)])

    for i in range(size):
        data.append(['gasoline', random.randrange(20, 500, 1)])

    for i in range(size):
        data.append(['pets', random.randrange(5, 1000, 10)])

    for i in range(size):
        data.append(['movies', random.randrange(3, 3000, 10)])

    for i in range(size):
        data.append(['sports games', random.randrange(100, 1000, 10)])

    for i in range(size):
        data.append(['renovation', random.randrange(100, 10000, 10)])

    for i in range(size):
        data.append(['medical', random.randrange(10, 1000, 10)])

    random.shuffle(data)
    inputdata = {}
    counter = 0
    dataname = "default"
    while counter < len(data):
        input = {}
        name = names.get_full_name()
        while name in inputdata.keys():
            name = names.get_full_name()
        randomvalue = random.randrange(5, 10, 1)
        counter2 = 0
        credit = 711.0
        check = True
        check1 = True
        counter4 = 0
        while counter2 < int(randomvalue):
            if counter < len(data) and not data[counter][0] in input:
                input[data[counter][0]] = (data[counter][1])
                if creditcalc[data[counter][0]]["medium"] < data[counter][1]:
                    check1 = False
                    counter4 += 1
                    credit -= creditcalc[data[counter][0]]["higher"] * \
                        (creditcalc[data[counter][0]]
                         ["medium"] - data[counter][1])
                    if not data[counter][0] in spending.keys():
                        check = False
                elif creditcalc[data[counter][0]]["medium"] > data[counter][1]:
                    credit += creditcalc[data[counter][0]]["lower"] * \
                        (creditcalc[data[counter][0]]
                         ["medium"] - data[counter][1])
            else:
                break
            counter += 1
            counter2 += 1
        inputdata[name] = {}
        inputdata[name]['before'] = input
        inputdata[name]['beforecredit'] = credit
        if check == True and check1 == False and counter4 == len(spending.keys()) and dataname == "default":
            dataname = name
    additionalcredit = 0.0
    lessmoney = []
    for element in spending.keys():
        if creditcalc[element]["medium"] < spending[element]:
            extra = (spending[element] - creditcalc[element]["medium"])
            lessmoney.append("cut $" + str(extra) + " on " + str(element))
            additionalcredit -= creditcalc[element]["higher"]*extra
    additionalcredit1 = 0.0
    lessmoney1 = []
    if dataname != "default":
        for element in inputdata[dataname]['before'].keys():
            if creditcalc[element]["medium"] < inputdata[dataname]['before'][element]:
                extra = (inputdata[dataname]['before'][element] -
                         creditcalc[element]["medium"])
                lessmoney1.append("cutting $" + str(extra) +
                                  " on " + str(element))
                additionalcredit1 -= creditcalc[element]["higher"]*extra
    finalvalue = "If you "
    counter3 = 0
    for element in lessmoney:
        finalvalue += element
        if len(lessmoney) > counter3 + 1:
            finalvalue += " and "
        counter3 += 1
    finalvalue += ", your credit score will increase from " + \
        str(aftercredit) + " to " + str(aftercredit + additionalcredit)
    if dataname != "default":
        finalvalue += " just like some other user who increased their credit by " + \
            str(int(additionalcredit1)) + " by "
        counter3 = 0
        for element in lessmoney1:
            finalvalue += element
            if len(lessmoney) > counter3 + 1:
                finalvalue += " and "
            counter3 += 1
    finalvalue += "."
    return finalvalue
