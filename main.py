import requests
import tkinter as tk


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(text, text=quote)


window = tk.Tk()
window.title("Kanye Says")
window.config(pady=50, padx=50)

canvas = tk.Canvas(window)
canvas.config(width=300, height=500)
image = tk.PhotoImage(file="background.png")
canvas.create_image(150, 200, image=image)
text = canvas.create_text(150, 200, text="Click the button", font=("Arial", 30, "bold"), width=250)
canvas.grid(row=0, column=0)

button_image = tk.PhotoImage(file="kanye.png")
button = tk.Button(image=button_image, command=get_quote)
button.grid(row=1, column=0)



window.mainloop()
