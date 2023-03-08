import fitz
file='test.pdf'

pdf=fitz.open(file)
# image_list=pdf.getPageImageList(0)
#
# for image in image_list:
#     xref=image[0]
#     pix=fitz.Pixmap(pdf, xref)
#     if pix.n<5:
#         pix.writePNG(f'{xref}.png')
#     else:
#         pix1=fitz.open(fitz.csRGB,pix)
#         pix1.writePNG(f'{xref}.png')
#         pix1=None
#     pix=None
# print(len(image_list),'detected')

pdf_page=pdf.loadPage(0)
text=pdf_page.getText()

text=text.split("\n")

print(text[4] + ":"+text[5])
print(text[22] + ":"+text[23].replace("�মাঃ","মোঃ"))
print(text[24] + ":"+text[25])

#
# # text=text.split("Name(English)")
# print(text)
