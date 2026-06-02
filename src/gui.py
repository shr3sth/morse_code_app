import customtkinter as ctk
from morse import encode_text, decode_morse


ctk.set_appearance_mode("dark")

app = ctk.CTk()

app.title("Morse Code Converter")
app.geometry("700x650")


def encode_button_clicked():
    text = input_box.get("1.0", "end").strip()

    morse_result = encode_text(text)

    output_box.configure(state="normal")

    output_box.delete("1.0", "end")
    output_box.insert("1.0", morse_result)

    output_box.configure(state="disabled")


def decode_button_clicked():
    morse = input_box.get("1.0", "end").strip()

    text_result = decode_morse(morse)

    output_box.configure(state="normal")

    output_box.delete("1.0", "end")
    output_box.insert("1.0", text_result)

    output_box.configure(state="disabled")


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


encode_button = ctk.CTkButton(
    button_frame,
    text="Encode",
    command=encode_button_clicked
)
encode_button.pack(side="left", padx=10)

decode_button = ctk.CTkButton(
    button_frame,
    text="Decode",
    command=decode_button_clicked
)

decode_button.pack(side="left", padx=10)


clear_button = ctk.CTkButton(
    button_frame,
    text="Clear",
    command=clear_boxes
)

clear_button.pack(side="left", padx=10)


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

app.mainloop()
