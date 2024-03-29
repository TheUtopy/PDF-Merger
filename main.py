from PyPDF2 import PdfWriter
import tkinter as tk
from tkinter.filedialog import askopenfilename

merger = PdfWriter()

if __name__ == '__main__':

    liste_de_fichier_a_merge = []

    # créé la fenêtre et la nomme
    root = tk.Tk(className=" PDF Merger")
    # défini la taille de la fenêtre
    canvas = tk.Canvas(root, width=600, height=200)
    canvas.grid(columnspan=3, rowspan=5)

    # instruction
    label = tk.Label(root, text="Select a .pdf file")
    label.grid(column=1, row=0)

    # Va chercher l'adresse des fichiers et les retourne
    def open_file():
        browse_text.set("loading...")
        file = askopenfilename(parent=root, title="Choose a file", filetype=[("PDF file", "*.pdf")])
        if file and file not in liste_de_fichier_a_merge:
            liste_de_fichier_a_merge.append(file)
            print(liste_de_fichier_a_merge)
            text_path.config(state='normal')
            text_path.insert('end', file + "\n")
            text_path.config(state='disabled')
        browse_text.set("Browse")


    # browse button
    browse_text = tk.StringVar()
    browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(), bg="#20bebe", fg="white",
                           height=2, width=15)
    browse_text.set("Browse")
    browse_btn.grid(column=1, row=1)

    # affichage des adresses des fichiers sélectionnés
    text_path = tk.Text(root, width=60, height=10)
    text_path.grid(column=1, row=2)
    text_path.config(state='disabled')

    def next_step():
        text_path.config(state='normal')
        text_path.delete('1.0', tk.END)
        text_path.config(state='disabled')

    # submit button
    submit_text = tk.StringVar()
    submit_btn = tk.Button(root, textvariable=submit_text, command=lambda: next_step(), bg="#20bebe", fg="white",
                           height=2, width=15)
    submit_text.set("Submit")
    submit_btn.grid(column=1, row=3)

    root.mainloop()

    #
    #
    #
    file_1 = input()
    file_2 = input()
    # "../test PDF Merger/01.pdf"

    merger.append(file_1)
    merger.append(file_2)

    # Demande le nom du fichier final
    name_of_file = input("Enter the name of your merged file : ")

    # Demande le répertoire dans lequel enregistré le résultat final
    output_path = input("Path of the output file : ")
    if not output_path.endswith("/"):
        output_path += "/"

    # merge les fichiers
    output = open(output_path + name_of_file + ".pdf", "wb")
    merger.write(output)

    merger.close()
    output.close()

