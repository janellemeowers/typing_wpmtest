from tkinter import *
import random
import tkinter

window = Tk()

window.title("Typing Speed Test")
window.geometry('550x200')
window.config(padx=50, pady=50)


def restart():
    # Remove results
    result_label.destroy()
    restart_button.destroy()

    # re-setup writing labels.
    writing_texts()


def add_second():
    # Increase counter by one sec
    global seconds_passed
    seconds_passed += 1
    time_left = 60 - seconds_passed
    # update time label
    time_left_label.configure(text=f'{time_left} Seconds Left')

    # every one second, continue
    if typing:
        window.after(1000, add_second)


def stop_test():
    global typing
    typing = False

    # Calculating the amount of words
    total_words = len(label_written.cget('text').split(' '))

    # Remove labels
    time_left_label.destroy()
    label_type.destroy()
    current_letter_label.destroy()
    label_written.destroy()
    type_entry.destroy()

    # Display the test results
    global result_label
    result_label = Label(text=f'Words per Minute: {total_words}', fg='blue')
    result_label.place(relx=0.5, rely=0.3, anchor=CENTER)

    # restart button
    global restart_button
    restart_button = Button(text=f'Retry', command=restart)
    restart_button.place(relx=0.5, rely=0.6, anchor=CENTER)


#it is binded to window.bind event, takes event param, default is none
def key_pressed(event=None):
    try:
        #if current key = text in first spot, first spot in text
        if event.char.lower() == label_type.cget('text')[0].lower():
            # shift to write text over by 1
            label_type.configure(text=label_type.cget('text')[1:])
            # Add letter to the left/gray typed
            label_written.configure(text=label_written.cget('text') + event.char.lower())
            # set the next Letter
            current_letter_label.configure(text=label_type.cget('text')[0])
    except tkinter.TclError:
        pass


def writing_texts():
    #remove start button
    start_btn.destroy()

    random_selection = [
        'A random statement can inspire authors and help them start writing. It challenges the author to use their imagination because the sentences subject is utterly ambiguous. The random sentence may be creatively used in a variety of ways by writers. The statement is most frequently used to start a tale. Another choice is to include it into the narrative. The issue of using it to conclude a tale is far more challenging. In all of these scenarios, the writer is compelled to use their imagination because they have no idea what words will come out of the tool.',
        'Python Code aims to teach beginning and intermediate programmers Python through tutorials, recipes, articles, and problem-solving techniques while also disseminating information globally. Everyone in the globe will be able to learn how to code for free thanks to Python Code. Python is a general-purpose, high-level, interpreted programming language. Code readability is prioritised in its design philosophy, which makes heavy use of indentation. Python uses garbage collection and has dynamic typing. It supports a variety of programming paradigms, including procedural, object-oriented, and functional programming as well as structured programming (especially this). Due to its extensive standard library, it is frequently referred to as a "batteries included" language.',
        'We begin with the imports as usual. We must import tkinter since we utilise it to create the user interface. In order to subsequently modify the typefaces on our components, we additionally import the font module from tkinter. The partial function is obtained from functools and is a brilliant function that accepts another function as a first argument, along with certain args and kwargs, and returns a reference to this function with those arguments. When we wish to add one of our functions to a command argument of a button or key binding, this is extremely helpful.',
        'A computer programmer is a person who writes computer programmes, frequently for bigger pieces of software. They are also known as software developers, software engineers, programmers, or coders. A programmer is a person who uses a particular programming language to construct or write computer software or applications. The majority of programmers have substantial computer and coding expertise across a wide range of platforms and programming languages, including SQL, Perl, XML, PHP, HTML, C, C++, and Java. The terms "programmer" and "software engineer" may be used to describe the same position at various businesses because there is no industry-wide vocabulary standard. Usually, a "programmer" or "software developer" will concentrate on translating a precise specification into computer code.'
    ]
    # Choose one of the texts randomly
    text = random.choice(random_selection).lower()

    global type_entry
    type_entry = Entry(width=20)
    type_entry.place(relx=0.5, rely=0.5, anchor=S)


    # already written text
    global label_written
    #starts at 0 bc blank
    label_written = Label(text=text[:0], fg='grey')
    # x & y relative pos (nsew anchor)
    label_written.place(relx=0.6, rely=0.6, anchor=E)

    # text to be written, upcoming text
    global label_type
    label_type = Label(text=text)
    label_type.place(relx=0.6, rely=0.6, anchor=W)

    # which letter to press
    global current_letter_label
    current_letter_label = Label(text=text[0], fg='blue')
    current_letter_label.place(relx=0.5, rely=0.7, anchor=N)

    # Starts timer at 60
    global time_left_label
    time_left_label = Label(text=f'60 Seconds', fg='red')
    time_left_label.place(relx=.5, rely=1, anchor=N)

    global typing
    typing = True
    window.bind('<Key>', key_pressed)

    global seconds_passed
    seconds_passed = 0

    # Binding functions after a certain amount of time.
    window.after(60000, stop_test) #after 60 seconds
    window.after(2000, add_second) #account for 2 sec delay to load


starting_text = Label(text="How fast can you type?", font="Arial, 14", fg="blue")
starting_text.place(relx=.5, rely=-0.1, anchor=N)

start_btn = Button(text="START", command=writing_texts)
start_btn.place(relx=0.5, rely=0.5, anchor=S)





window.mainloop()
