import tkinter as tk
from tkinter import *
from chatbot import chat

BG_GRAY = "ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvatica 14"
FONT_BOLD = "Helvatica 13 bold"
bot_name = "Psycho"


class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="Enter Text...", color="#EAECEE", bold=True):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._set_placeholder)

        self._set_placeholder()

    def _clear_placeholder(self, event):
        if self['fg'] == self.placeholder_color:
            self.delete(0, tk.END)
            self.config(fg=self.default_fg_color)

    def _set_placeholder(self, event=None):
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(fg=self.placeholder_color)

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=950, height=650, bg=BG_COLOR)

        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)

        head_label.place(relwidth=1)

        line = Label(self.window, width=450, bg=BG_COLOR)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR,
                                fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        bottom_label = Label(self.window, bg=BG_COLOR, height=80)
        bottom_label.place(relwidth=1, rely=0.825)


        self.msg_entry = PlaceholderEntry(bottom_label, "Type your massage here....", color="#0e2433", bold=True)
        self.msg_entry.place(relheight=0.06, relwidth=0.74, rely=0.008, relx=0.011)
        self.msg_entry.bind("<Return>", self.on_enter_pressed)
        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD,
                             width=20, bg='#EAECEE',
                             command=lambda: self.on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    # functions to get message from sender
    def on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return
        self.msg_entry.delete(0, END)
        # actual message that we want to display (dh el hn7oto f text widget area
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {chat(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
