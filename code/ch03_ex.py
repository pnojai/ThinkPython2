print('Define right_justify()...')
def right_justify(s):
    right_margin = 70
    s_length = len(s)
    pad = ' ' * (right_margin - s_length)
    print(pad + s)

print('Testing right_justify()...')
right_justify('monty')
right_justify('jai')
right_justify('0123456789'*7)

print('Define do_twice()...')
def do_twice(f, arg):
    f(arg)
    f(arg)

print('Define print_spam()...')
def print_spam(s):
    print('spam'+': '+s)

print('Testing do_twice()...')    
do_twice(print_spam, 'spud')

print('Define do_four()...')
def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

print('Testing do_four()...')
do_four(print, 'PnoJai')

print('Exercises 3.3 and 3.4...')

def PrintGridHorizontalBorder(CornerChar, FillHorizontalChar, CellWidth, ColCount):
    i = 1

    while i <= ColCount:
        #print(i)
        print(CornerChar + FillHorizontalChar*(CellWidth - 1), end='')
        if i == ColCount:
            print(CornerChar)

        i += 1

def PrintGridVerticalBorders(FillVerticalChar, CellWidth, CellHeight, ColCount):
    j = 2 #Initialize counter for beginning 2nd row of cell fill
    while j <= CellHeight:
        #repeat CellHeight times
        i = 1
        while i <= ColCount:
            print(FillVerticalChar + ' '*(CellWidth - 1), end='')
            if i == ColCount:
                print(FillVerticalChar)
                
            i += 1
        #end repeat
        j += 1
    #end j

def PrintGrid(CornerChar, FillHorizontalChar, FillVerticalChar, CellWidth, CellHeight, ColCount, RowCount):
    print('CornerChar: ' + CornerChar)
    print('FillHorizontalChar: ' + FillHorizontalChar)
    print('FillVerticalChar: ' + FillVerticalChar)
    print('CellWidth: ' + str(CellWidth))
    print('CellHeight: ' + str(CellHeight))
    print('ColCount: ' + str(ColCount))
    print('RowCount: ' + str(RowCount))

    i = 1
    while i <= RowCount:
        PrintGridHorizontalBorder(CornerChar, FillHorizontalChar, CellWidth, ColCount)
        PrintGridVerticalBorders(FillVerticalChar, CellWidth, CellHeight, ColCount)

        if i == RowCount:
            PrintGridHorizontalBorder(CornerChar, FillHorizontalChar, CellWidth, ColCount)

        i += 1
        
PrintGrid('+', '-', '|', 5, 5, 2, 2)
PrintGrid('+', '-', '|', 5, 5, 3, 3)
PrintGrid('+', '-', '|', 10, 10, 4, 4)

def PrintGridInter():
    '''
    PrintGridInter: Interactive form of PrintGrid().
    Prompts user for arguments:
    CornerChar, FillHorizontalChar, FillVerticalChar,
    CellWidth, CellHeight, ColCount, RowCount
    '''

    CornerChar = input('Type the character to use for corners...')
    FillHorizontalChar = input('Type the character to use for horizontal fills...')
    FillVerticalChar = input('Type the character to use for vertical fills...')
    CellWidth = int(input('How wide do you want the cells to be...'))
    CellHeight = int(input('How high do you want the cells to be...'))
    ColCount = int(input('How many columns do you want the grid to have...'))
    RowCount = int(input('How many rows  do you want the grid to have...'))

    i = 1
    while i <= RowCount:
        PrintGridHorizontalBorder(CornerChar, FillHorizontalChar, CellWidth, ColCount)
        PrintGridVerticalBorders(FillVerticalChar, CellWidth, CellHeight, ColCount)

        if i == RowCount:
            PrintGridHorizontalBorder(CornerChar, FillHorizontalChar, CellWidth, ColCount)

        i += 1

PrintGridInter()
