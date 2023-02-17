from PyPDF2 import PdfWriter

merger = PdfWriter()

if __name__ == '__main__':


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
