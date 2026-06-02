import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()

app.title("Morse Code Converter")
app.geometry("600x400")


title_label = ctk.CTkLabel(
    app,
    text="Morse Code Converter",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=20)


app.mainloop()
