import customtkinter as ctk
from morse import encode_text, decode_morse


ctk.set_appearance_mode("dark")

app = ctk.CTk()

app.title("Morse Code Converter")
app.geometry("700x650")


def open_morse_pad():
    pad_window = ctk.CTkToplevel()
    pad_window.title("Morse Pad")
    pad_window.geometry("350x500")

    morse_label = ctk.CTkLabel(
        pad_window,
        text="Current Morse"
    )
    morse_label.grid(row=0, column=0, columnspan=2, pady=10)

    morse_output = ctk.CTkTextbox(
        pad_window,
        width=300,
        height=100
    )
    morse_output.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

    morse_output.configure(state="disabled")

    def add_dot():
        morse_output.configure(state="normal")
        morse_output.insert("end", ".")
        morse_output.configure(state="disabled")
        update_decoded_text()

    def add_dash():
        morse_output.configure(state="normal")
        morse_output.insert("end", "-")
        morse_output.configure(state="disabled")
        update_decoded_text()

    def add_letter_space():
        morse_output.configure(state="normal")
        morse_output.insert("end", " ")
        morse_output.configure(state="disabled")
        update_decoded_text()

    def add_word_space():
        morse_output.configure(state="normal")
        morse_output.insert("end", " / ")
        morse_output.configure(state="disabled")
        update_decoded_text()

    def clear_morse():
        morse_output.configure(state="normal")
        morse_output.delete("1.0", "end")
        morse_output.configure(state="disabled")
        update_decoded_text()

    def update_decoded_text():

        morse_text = morse_output.get(
            "1.0",
            "end"
        ).strip()

        decoded_text = decode_morse(
            morse_text
        )

        decoded_output.configure(
            state="normal"
        )

        decoded_output.delete(
            "1.0",
            "end"
        )

        decoded_output.insert(
            "1.0",
            decoded_text
        )

        decoded_output.configure(
            state="disabled"
        )

    button_frame = ctk.CTkFrame(pad_window)
    button_frame.grid(
        row=2,
        column=0,
        columnspan=2,
        pady=10
    )

    decoded_label = ctk.CTkLabel(
        pad_window,
        text="Decoded Text"
    )

    decoded_label.grid(
        row=3,
        column=0,
        columnspan=2,
        pady=10
    )

    decoded_output = ctk.CTkTextbox(
        pad_window,
        width=300,
        height=80
    )

    decoded_output.grid(
        row=4,
        column=0,
        columnspan=2,
        padx=20,
        pady=10
    )
    decoded_output.configure(state="disabled")

    dot_button = ctk.CTkButton(
        button_frame,
        text=".",
        command=add_dot,
        width=120
    )

    dot_button.grid(
        row=0,
        column=0,
        padx=10
    )

    dash_button = ctk.CTkButton(
        button_frame,
        text="-",
        command=add_dash,
        width=120
    )

    dash_button.grid(
        row=0,
        column=1,
        padx=10
    )

    letter_space_button = ctk.CTkButton(
        button_frame,
        text="Letter Space",
        command=add_letter_space,
        width=120
    )

    letter_space_button.grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )

    word_space_button = ctk.CTkButton(
        button_frame,
        text="Word Space",
        command=add_word_space,
        width=120
    )

    word_space_button.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )

    clear_button = ctk.CTkButton(
        button_frame,
        text="Clear",
        command=clear_morse,
        width=250
    )
    clear_button.grid(
        row=2,
        column=0,
        columnspan=2,
        padx=10,
        pady=10
    )


def encode_button_clicked():
    text = input_box.get("1.0", "end").strip()

    morse_result = encode_text(text)

    output_box.configure(state="normal")

    output_box.delete("1.0", "end")
    output_box.insert("1.0", morse_result)

    output_box.configure(state="disabled")

    status_label.configure(
        text="Encoded successfully"
    )


def decode_button_clicked():
    morse = input_box.get("1.0", "end").strip()

    text_result = decode_morse(morse)

    output_box.configure(state="normal")

    output_box.delete("1.0", "end")
    output_box.insert("1.0", text_result)

    output_box.configure(state="disabled")

    status_label.configure(
        text="Decoded successfully"
    )


def copy_output():
    text = output_box.get("1.0", "end").strip()

    app.clipboard_clear()
    app.clipboard_append(text)

    status_label.configure(
        text="Copied to clipboard"
    )


title_label = ctk.CTkLabel(
    app,
    text="Morse Code Converter",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=20)


input_label = ctk.CTkLabel(
    app,
    text="Input"
)
input_label.pack()


input_box = ctk.CTkTextbox(
    app,
    width=500,
    height=100
)
input_box.pack(pady=10)


button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10)


def clear_boxes():
    input_box.delete("1.0", "end")

    output_box.configure(state="normal")
    output_box.delete("1.0", "end")
    output_box.configure(state="disabled")

    status_label.configure(
        text="Cleared"
    )


encode_button = ctk.CTkButton(
    button_frame,
    text="Encode",
    command=encode_button_clicked,
    width=180
)
encode_button.grid(
    row=0,
    column=0,
    padx=10,
    pady=5
)

decode_button = ctk.CTkButton(
    button_frame,
    text="Decode",
    command=decode_button_clicked,
    width=180
)

decode_button.grid(
    row=0,
    column=1,
    padx=10,
    pady=5
)


clear_button = ctk.CTkButton(
    button_frame,
    text="Clear",
    command=clear_boxes,
    width=180
)

clear_button.grid(
    row=1,
    column=0,
    padx=10,
    pady=5
)


copy_button = ctk.CTkButton(
    button_frame,
    text="Copy Output",
    command=copy_output,
    width=180
)

copy_button.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)


output_label = ctk.CTkLabel(
    app,
    text="Output"
)
output_label.pack()


output_box = ctk.CTkTextbox(
    app,
    width=500,
    height=100
)
output_box.pack(pady=10)
output_box.configure(state="disabled")


status_label = ctk.CTkLabel(
    app,
    text="Ready"
)

status_label.pack(pady=10)


morse_pad_button = ctk.CTkButton(
    app,
    text="Open Morse Pad",
    command=open_morse_pad,
    width=220
)

morse_pad_button.pack(pady=10)


app.mainloop()
