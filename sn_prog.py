print('WELCOME to \"THE SIMPLE NOTES!\"')
with open('notes.txt', mode='a+',
                 encoding='utf-8') as f:
    while True:
        cmd = input('\nSelect an action:\n\
shw - show all notes,\n\
add - add a new note, \n\
ext - for quit the program.\n>> :')
        if cmd == 'shw':
            f.seek(0, 0)
            content = f.readlines()
            if content != []:
                for note in content:
                    print(f'(*) {note}')
            else:
                print('The file is empty.')
        elif cmd == 'add':
            f.seek(0, 2)
            new_note = input('>> Enter a new note:\n>> :')
            f.write(new_note+'\n')
        elif cmd == 'ext':
            print('--Bye--!')
            break
        else:
            print('Error command...Press \"ext\" for quit.')           
