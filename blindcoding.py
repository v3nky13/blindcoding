from tkinter import *
from tkinter import ttk
from datetime import datetime

qnnum = 0
questions = [
    ['Even or Odd', 'Given a number n, print whether its "Even" or "Odd"\n\nSample input:\nn = 6\n\nSample output:\nEven\n\nExplanation:\n6 is Even'],
    ['Palindrome or not', 'Given a string s, print whether its "Palindrome" or\n"Not Palindrome"\n\nSample input:\ns = "malayalam"\n\nSample output:\nPalindrome\n\nExplanation:\nReverse of malayalam is malayalam'],
    ['Find factorial', 'Given a number n, find its factorial\n\nSample input:\nn = 5\n\nSample output:\n120\n\nExplanation:\nFactorial of 5 is 120'],
    ['Check for prime', 'Given a number n, print whether its "Prime" or "Not Prime"\n\nSample input:\nn = 7\n\nSample output:\nPrime\n\nExplanation:\n7 is Prime'],
    ['Print pattern', 'Given a number n, print a right-aligned, right-angled\ntriangle of n rows\n\nSample input:\nn = 5\n\nSample output:\n    *\n   **\n  ***\n ****\n*****\n\nExplanation:\nIt\'s a right-aligned, right-angled triangle with 5 rows'],
]

def main() -> None:
    root = Tk()
    root.title('Blind Coding')
    root.attributes('-fullscreen', True)
    root.iconbitmap("data/blind.ico")

    root.call('source', 'data/Azure/azure.tcl')
    root.call('set_theme', 'dark')
    style = ttk.Style(root)
    style.configure('azure-dark')
    style.configure('TButton', font=('consolas', 14, 'italic'), foreground='black')
    style.configure("Rounded.TLabel", borderwidth=10, relief="solid", foreground="#5f0", background="#222", bordercolor="black", padding=5)

    # welcome
    welcome = Frame(root, padx=10, pady=10)
    welcome.place(relx=0.5, rely=0.5, anchor=CENTER)

    blind_coding_lbl = ttk.Label(welcome, text='Blind Coding', font=('consolas', 30))
    blind_coding_lbl.pack(pady=(0, 20))

    name = ttk.Label(welcome, text='Your name:', font=('consolas', 16))
    name.pack(padx=10, pady=10)

    name_entry = ttk.Entry(welcome, font=('consolas', 12))
    name_entry.pack(padx=10, pady=10)

    def update_timer():
        nonlocal remaining_time
        minutes, seconds = divmod(remaining_time, 60)
        timer.configure(text=f"{minutes:02}:{seconds:02}")

        if remaining_time < 60:
            style.configure("Rounded.TLabel", foreground="#f30")

        if remaining_time > 0:
            remaining_time -= 1
            timer.after(1000, update_timer)
        else:
            qn.pack_forget()
            donemsg.configure(text="Time's up!")
            thankyou.place(relx=0.5, rely=0.5, anchor=CENTER)

    remaining_time = 20 * 60

    def welcome_to_firstqn():
        global start_time
        nonlocal name_entry, welcome, qn

        update_timer()

        with open("data/res.bc", 'a') as f:
            f.write('Name: ' + name_entry.get() + '\nStart time: ' + str(datetime.now()) + '\n\n')

        welcome.place_forget()
        qn.pack(fill='both', expand=True)

    enter_button = ttk.Button(welcome, text='Start', width=8, command=welcome_to_firstqn)
    enter_button.pack(padx=10, pady=10)

    # questions
    def change_qn():
        global qnnum, questions
        nonlocal qn, qn_no, qn_title, qn_desc, qn_text, thankyou, next_submit_button

        with open("data/res.bc", 'a') as f:
            f.write(f'Question {qnnum + 1}:\nSubmit time: {datetime.now()}\n' + qn_text.get("1.0", "end-1c") + '\n')

        if qnnum == len(questions) - 1:
            qn.pack_forget()
            thankyou.place(relx=0.5, rely=0.5, anchor=CENTER)
            return
        
        if qnnum == len(questions) - 2:
            next_submit_button.configure(text='Submit')
        
        qnnum += 1
        qn_no.configure(text=f'Question {qnnum + 1}')
        qn_title.configure(text=f'{questions[qnnum][0]}')
        qn_desc.configure(text=f'{questions[qnnum][1]}')
        qn_text.delete(1.0, END)

    qn = Frame(root, padx=10, pady=10)
    qn.grid_rowconfigure(0, weight=1)
    qn.grid_columnconfigure(0, weight=1)
    qn.grid_columnconfigure(1, weight=2)

    # left
    qn_left = LabelFrame(qn, padx=10, pady=10)
    qn_left.grid(row=0, column=0, sticky='nsew', padx=5)

    timer = ttk.Label(qn_left, text='15:00', font=('consolas', 24), style='Rounded.TLabel')
    timer.pack(pady=5, anchor='nw')

    qn_no = ttk.Label(qn_left, text=f'Question {qnnum + 1}', font=('consolas', 24))
    qn_no.pack(pady=5)

    qn_title = ttk.Label(qn_left, text=f'{questions[qnnum][0]}', font=('consolas', 20))
    qn_title.pack(padx=5, pady=5, anchor='w')
    
    qn_desc = ttk.Label(qn_left, text=f'{questions[qnnum][1]}', font=('consolas', 14), width=60)
    qn_desc.pack(padx=5, pady=5, anchor='w')

    # right
    qn_right = Frame(qn)
    qn_right.grid(row=0, column=1, columnspan=2, sticky='nsew')

    def change_highlight_color(event):
        qn_text.tag_configure("sel", background="#fff", foreground="#fff")

    qn_text = Text(qn_right, font=('consolas', 14), bg='#222', fg='#222')
    qn_text.bind("<<Selection>>", change_highlight_color)
    qn_text.pack(fill='both', expand=True)

    next_submit_button = ttk.Button(qn_right, text='Next', width=10, command=change_qn)
    next_submit_button.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-12)

    # thankyou
    thankyou = Frame(root)

    donemsg = ttk.Label(thankyou, text='You\'ve completed all questions!', font=('consolas', 16))
    donemsg.pack()

    thankmsg = ttk.Label(thankyou, text='Thank you for participating :)', font=('consolas', 16))
    thankmsg.pack()

    quit = ttk.Button(thankyou, text='Quit', width=8, command=root.quit)
    quit.pack(pady=20)

    root.mainloop()

if __name__ == '__main__':
    main()