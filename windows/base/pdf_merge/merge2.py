from pathlib import Path
import PyPDF2
import os
writer = PyPDF2.PdfWriter() 

pdf_dirs = Path.cwd() / 'merge'

# 使用 glob 方法查找以 '.pdf' 结尾的所有 PDF 文件
pdf_files = list(pdf_dirs.glob('*.pdf'))  

# 将文件列表按数字顺序排列
pdf_files.sort() 
for file in pdf_files:
    print(os.path.basename(file))

for file in pdf_files:
    fp = open(file, "rb")
    reader = PyPDF2.PdfReader(fp)
    writer.add_page(reader.pages[0])
    fp.close()

with Path.cwd().joinpath('merge.pdf').open('wb') as f:
    writer.write(f)