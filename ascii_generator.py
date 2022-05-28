import tkinter as tk
import requests

def download_ascii():
    if text_input.get:
        user_input = text_input.get()
        payload = {"text": user_input}
        r = requests.get("http://artii.herokuapp.com/make", params=payload)
        text_response = r.text
    else:
        text_response = "Add a word!"
    
    text_widget = tk.Text()
    text_widget.insert(tk.End, text_response)
    text_widget.grid(row=3, column=0, sticky="WE", padx="10",pady="10")

window = tk.Tk()
window.geometry("900x600")
window.resizable(False, False)
window.title("Ascii downloader")
window.grid_columnconfigure(0, weight=1)

welcome_label = tk.Label(window, text="welcome!", font=("Helvetica", 15))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)

text_input = tk.Entry(width=60)
text_input.grid(row=1, column=0)

download_button = tk.Button(text="Press to download", command=download_ascii, width=60)
download_button.grid(row=2, column=0)

if __name__ == "__main__":
    window.mainloop()
    