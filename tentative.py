import datetime

objectives = []

def daily_start():

    now = datetime.date.today()
    #pass # Objective: find how to write this timestamp in a file. Til then, I'll store everything in a list.

    print('''*******************************************

    Date: {a}-{b}-{c}

    Hi there!
    Declare your objectives below. When you are done, type "Enter" with no input.
    Hajime!'''.format(a={now.year}, b={now.month}, c={now.day}))

    taking_items()

    # recap
    print('You listed:')
    for item in objectives:
        print(item)
    print("Gosh, that's a lot ! Better get started now. Go ! <3")

def taking_items():
    item = None
    while item != '':
        item = input('What do you plan on doing today? >>> ')
        if item != '':
            objectives.append(item)
    declaration_over = True

daily_start()
