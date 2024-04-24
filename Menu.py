import tkinter as tk
from tkinter import filedialog

def open_file():
    def upload():
        file_path = filedialog.askopenfilename()
        if file_path:
            process_file(file_path)

    def process_file(file_path):
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
                try:
                    decoded_content = content.decode('utf-8')
                except UnicodeDecodeError:
                    try:
                        decoded_content = content.decode('latin-1')
                    except UnicodeDecodeError:
                        print("No se pudo decodificar el archivo con ninguna codificación conocida.")
                        return
                frequencies = calculate_frequency(decoded_content)
                print("Frecuencia de caracteres:")
                print(frequencies)
                show_frequencies(frequencies)  # Llama a la función para mostrar frecuencias
        except FileNotFoundError:
            print("Archivo no encontrado.")

    def calculate_frequency(text):
        frequency = {}
        for char in text:
            if char.isalpha() or char.isspace():  # Contar caracteres alfabéticos y espacios
                if char in frequency:
                    frequency[char] += 1
                else:
                    frequency[char] = 1
        return frequency

    def show_frequencies(frequencies):
        frequency_window = tk.Toplevel()  
        frequency_window.title("Frecuencia de Caracteres")
        frequency_window.geometry('300x200')

        label_title = tk.Label(frequency_window, text="Frecuencia de Caracteres", font="arial 12 bold")
        label_title.pack(pady=10)

        for char, freq in frequencies.items():
            label_freq = tk.Label(frequency_window, text=f"{char}: {freq}")
            label_freq.pack()

    upload_window = tk.Tk()
    upload_window.title("Abrir Archivo")
    upload_window.geometry('520x300')

    label_text = tk.Label(upload_window, text="Seleccione un archivo para abrir", font="arial 12 bold")
    label_text.place(relx=0.5, rely=0.4, anchor="center")
    open_button = tk.Button(upload_window, text="Abrir archivo", command=upload)
    open_button.place(relx=0.5, rely=0.6, anchor="center")
    upload_window.mainloop()

def compress():
    print("Función de compresión")

def decompress():
    print("Función de descompresión")

def main():
    window = tk.Tk()
    window.title("ACT 07 - Entrega 1 Huffman")
    window.geometry('520x300')

    # Etiqueta inicial

    label = tk.Label(window, text="¿Qué quieres hacer?", font="arial 12")
    label.pack(padx=20, pady=20)

    # Botones
    button_open_file = tk.Button(window, text="Examinar", command=open_file)
    button_open_file.pack(pady=5)

    button_compress = tk.Button(window, text="Comprimir", command=compress)
    button_compress.pack(pady=5)

    button_decompress = tk.Button(window, text="Descomprimir", command=decompress)
    button_decompress.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    main()