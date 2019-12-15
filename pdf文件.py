

from PyPDF2 import PdfFileReader,PdfFileWriter,PdfFileMerger


def main():
    # 获取一个PdfFileReader对象
    pdf_input = PdfFileReader(open('mdb.pdf','rb'))
    pge_num = pdf_input.getNumPages()     # 得到页码数
    print(pge_num)
    print(pdf_input.getDocumentInfo())    # 得到文档信息
    # 返回PageObject对象
    pages_from_row = [pdf_input.getPage(i) for i in range(pdf_input.getNumPages())]

    # 获取一个PdfFileWriter对象
    pdf_output = PdfFileWriter()
    # 将PageObject添加到PdfFileWriter
    for page in pages_from_row:
        pdf_output.addPage(page)
    # 输出到文件中
    pdf_output.write(open('mdbt.pdf','wb'))

    # 合并两个pdf文件
    merger = PdfFileMerger()
    merger.append(PdfFileReader(open('mdb.pdf','rb')))
    merger.append(PdfFileReader(open('mdbt.pdf', 'rb')))
    merger.write(open('mdb-merger.pdf','wb'))


if __name__ == '__main__':
    main()

