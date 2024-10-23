import PyPDF2 as p
import os
folder=os.listdir("PDF")

merger=p.PdfMerger()

for pdf in folder:
    merger.append(f"PDF/{pdf}")

merger.write('out.pdf')
merger.close()