from PyPDF2 import PdfFileMerger

pdfs = ['P1-P2 trimer thresh=10A.pdf', 'P1-P3 trimer thresh=10A.pdf', 'P2-P3 trimer thresh=10A.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("total_thresh=10A_aa_trimer_peptide.pdf")
merger.close()