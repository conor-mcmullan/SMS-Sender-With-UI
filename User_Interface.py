from tkinter import *
import nexmo

fields = ('SENDER', 'RECIPIENT', 'TEXT', 'NO_SMS')


def get_field_data(entries, field):
    data = str(entries[field].get()).strip()
    print(str(field) + " :\t" + str(field))
    return data


def clear_all_fields(entries):
    for field in fields:
        entries[field].delete(0, END)


def clear_field(entries, field):
    entries[field].delete(0, END)


def set_field_value(entries, field, data):
    clear_field(entries, field)
    entries[field].insert(0, data)


def reset_all_fields(entries):
    for field in fields:
        entries[field].delete(0, END)
        entries[field].insert(0, 'Please enter the ' + str(field) + ' ...')


def makeform(root, fields):
    entries = {}
    for field in fields:
        root.configure(background="light blue")
        row = Frame(root)
        lab = Label(row, width=10, text=field + ": ", anchor='w', fg="blue", background="light blue")
        ent = Entry(row)
        ent.insert(0, '')
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, padx=0)
        entries[field] = ent
    return entries


def client_single_send_msg(e):
    client = nexmo.Client(key='75be68b3', secret='PSZllQ7yRF1Hhedd')
    client.send_message({
        'from': get_field_data(e, 'SENDER'),
        'to': get_field_data(e, 'RECIPIENT'),
        'text': get_field_data(e, 'TEXT')
    })


def send_for_x_times(e):
    x = int(get_field_data(e, 'NO_SMS'))
    try:
        if isinstance(x, int):
            if x > 0 and x < 11:
                for i in range(x):
                    client_single_send_msg(e)
        else:
            raise TypeError
    except TypeError as TE:
        print("Exception Raised:\n" + str(TE))
        set_field_value(e, 'NO_SMS', 'Maximum of 10')


if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))

    b1 = Button(root, text='SEND', command=(lambda e=ents: send_for_x_times(e)))
    b1.configure(background="light green")
    b1.pack(side=LEFT, padx=5, pady=5)

    b2 = Button(root, text='CLEAR', command=(lambda e=ents: clear_all_fields(e)))
    b2.configure(background="light green")
    b2.pack(side=LEFT, padx=5, pady=5)

    b3 = Button(root, text='RESET', command=(lambda e=ents: reset_all_fields(e)))
    b3.configure(background="light green")
    b3.pack(side=LEFT, padx=5, pady=5)

    b4 = Button(root, text='QUIT', command=root.quit)
    b4.configure(background="light green")
    b4.pack(side=LEFT, padx=5, pady=5)

    root.mainloop()
