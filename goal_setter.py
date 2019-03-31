import datetime

objectives = []

def daily_start():

    mylog = open('mylog.txt',mode='a')
    now = str(datetime.date.today())
    mylog.write("\n\n\n>>>" + now + "\n")

    print('''*******************************************

    Date: {a}

    Hi there!
    Declare your objectives below. When you are done, type "Enter" with no input.
    Hajime!

    '''.format(a=now))

    taking_items()

    # recap
    for item in objectives:
        mylog.write("- " + item + "\n")
    print(f"{len(objectives)} objectives were added to the log for today.")


def taking_items():
    item = None
    while item != '':
        item = input('What do you plan on doing today? >>> ')
        if item != '':
            objectives.append(item)
    declaration_over = True

daily_start()
