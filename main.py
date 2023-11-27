# pylint: disable=missing-module-docstring
import tabula

pdf_path = "./pdf_files/salaries.pdf"

tables: list = tabula.read_pdf(pdf_path, pages='1-458')

total = 0
times_run = 0

for table in tables:
    for _, row in table.iterrows():
        for item in row:
            if isinstance(item, str) and "." in item:
                total += float(item.replace(',', ''))
                times_run += 1

print(f"This is the total: {total}")
print(f"times run: {times_run}")
