

from PyPDF2 import PdfFileReader,PdfFileWriter


def main():
    # PdfFileReader对象
    pdf_input = PdfFileReader('mdb.pdf','rb')
    pge_num = pdf_input.getNumPages()     # 得到页码数
    print(pge_num)
    print(pdf_input.getDocumentInfo())    # 得到文档信息





if __name__ == '__main__':
    main()

