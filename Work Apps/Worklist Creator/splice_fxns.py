TEMPLATE = "Positions.txt"
WORKLIST1 = "Names1.txt"
WORKLIST2 = "Names2.txt"

def splice_wells(start1, end1, start2, end2):
    """Takes starting and end well positions for two lists and combines their
    elements alternatingly into a third list that is written to 'Positions Output.txt'
    """
    start1 = start1 + '\n'
    end1 = end1 + '\n'
    start2 = start2 + '\n'
    end2 = end2 + '\n'

    with open(TEMPLATE, "r") as file:
        plate_template1 = file.readlines()

    with open(TEMPLATE, "r") as file:
        plate_template2 = file.readlines()

    set3 = []

    for i, j in enumerate(plate_template1):
        if j == start1:
            plate_template1 = plate_template1[i:]

    for i, j in enumerate(plate_template1):
        if j == end1:
            plate_template1 = plate_template1[:i] + [end1]

    for i, j in enumerate(plate_template2):
        if j == start2:
            plate_template2 = plate_template2[i:]

    for i, j in enumerate(plate_template2):
        if j == end2:
            plate_template2 = plate_template2[:i] + [end2]

    for i in plate_template1:
        set3.append(" ")

    for i in plate_template2:
        set3.append(" ")

    x = 0

    while x < (len(set3) / 2):
        set3[2*x] = plate_template1[x]
        set3[2*x+1] = plate_template2[x]
        x = x + 1

    with open("Positions Output.txt", "w") as file:
        file.writelines(set3)

    print("its working")


def splice_name(worklist1=WORKLIST1, worklist2=WORKLIST2):
    """Takes two lists of sample names (default 'Names1/2.txt') and combines
    them alternatingly into a third list that is written to'Names Output.txt'
    """

    with open(worklist1, "r") as file:
        names1 = file.readlines()

    with open(worklist2, "r") as file:
        names2 = file.readlines()

    set3 = []
    x = 0

    for i in names1:
        set3.append(" ")

    for i in names2:
        set3.append(" ")

    while x < (len(set3) / 2):
        set3[2 * x] = names1[x]
        set3[2 * x + 1] = names2[x]
        x = x + 1

    with open("Names Output.txt", "w") as file:
        file.writelines(set3)

