import tabula

pdf_path = "c:/Users/cello/OneDrive/Documents/example_syllabus.pdf"
dfs = tabula.read_pdf(pdf_path, pages='all')
print(len(dfs))
tabula.convert_into(pdf_path, "output.csv", output_format="csv", pages='all')
