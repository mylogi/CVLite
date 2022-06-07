# from PIL import Image, ImageFont, ImageDraw, PdfImagePlugin, PSDraw
#
# img = Image.open("CV.jpg")
# font = ImageFont.truetype('arial.ttf', 24)
#
# draw = ImageDraw.Draw(img)
#
# text = 'Hello world Hello world Hello world Hello world Hello world Hello world Hello world Hello world'
#
# draw.text((0, 150), text, (0, 0, 0), font=font, stroke_fill=20)
# img.save('CV1.png')

# from PIL import Image, ImageDraw, ImageFont
#
# # create empty image
# img = Image.new(size=(400, 300), mode='RGB')
# draw = ImageDraw.Draw(img)
#
# # draw white rectangle 200x100 with center in 200,150
# draw.rectangle((200 - 100, 150 - 50, 200 + 100, 150 + 50), fill='white')
# draw.line(((0, 150), (400, 150)), 'gray')
# draw.line(((200, 0), (200, 300)), 'gray')
#
# # find font size for text `"Hello World"` to fit in rectangle 200x100
# selected_size = 1
# for size in range(1, 150):
#     arial = ImageFont.FreeTypeFont('arial.ttf', size=size)
#     w, h = arial.getsize("Hello World hfggjjgdkjdfk gfjgkfgjfkgj ggjfkgj \n gfgkfgkfglfgkflgkfdfnd \n lfkdlfkdlfdkfldfd")  # older versions
#     # left, top, right, bottom = arial.getbbox("Hello World")  # needs PIL 8.0.0
#     # w = right - left
#     # h = bottom - top
#     print(w, h)
#
#     if w > 200 or h > 100:
#         break
#
#     selected_size = size
#
#     print(arial.size)
#
# # draw text in center of rectangle 200x100
# arial = ImageFont.FreeTypeFont('arial.ttf', size=selected_size)
#
# # draw.text((200-w//2, 150-h//2), "Hello World", fill='black', font=arial)  # older versions
# # img.save('center-older.png')
#
# draw.text((200, 150), "Hello World hfggjjgdkjdfk gfjgkfgjfkgj ggjfkgj \n gfgkfgkfglfgkflgkfdfnd \n lfkdlfkdlfdkfldfd", fill='black', anchor='mm', font=arial)
# img.save('center-newer.png')

# from fpdf import FPDF
#
#
# class PDF(FPDF):
#     def header(self):
#         # Setting font: helvetica bold 15
#         self.set_font("helvetica", "B", 15)
#         # Calculating width of title and setting cursor position:
#         width = self.get_string_width(self.title) + 6
#         self.set_y(50)
#         self.set_x(50)
#         # Setting colors for frame, background and text:
#         self.set_draw_color(0, 80, 180)
#         self.set_fill_color(230, 230, 0)
#         self.set_text_color(220, 50, 50)
#         # Setting thickness of the frame (1 mm)
#         self.set_line_width(2)
#         # Printing title:
#         self.cell(
#             width,
#             9,
#             self.title,
#             border=1,
#             align="C",
#             fill=True,
#         )
#         # Performing a line break:
#         self.ln(10)
#
#     def footer(self):
#         # Setting position at 1.5 cm from bottom:
#         self.set_y(-15)
#         # Setting font: helvetica italic 8
#         self.set_font("helvetica", "I", 8)
#         # Setting text color to gray:
#         self.set_text_color(128)
#         # Printing page number
#         self.cell(0, 10, f"Page {self.page_no()}", align="C")
#
#     def chapter_title(self, num, label):
#         # Setting font: helvetica 12
#         self.set_font("helvetica", "", 12)
#         # Setting background color
#         self.set_fill_color(200, 220, 255)
#         # Printing chapter name:
#         self.cell(
#             0,
#             6,
#             f"Chapter {num} : {label}",
#             align="L",
#             fill=True,
#         )
#         # Performing a line break:
#         self.ln(4)
#
#     def chapter_body(self, filepath):
#         # Reading text file:
#         with open(filepath, "rb") as fh:
#             txt = fh.read().decode("latin-1")
#         # Setting font: Times 12
#         self.set_font("Times", size=12)
#         # Printing justified text:
#         self.set_y(100)
#         self.set_x(50)
#         self.multi_cell(50, 5, txt)
#         # Performing a line break:
#         self.ln()
#         # Final mention in italics:
#         self.set_font(family='',style="I")
#         self.cell(0, 5, "(end of excerpt)")
#
#     def print_chapter(self, num, title, filepath):
#         self.add_page()
#         self.chapter_title(num, title)
#         self.chapter_body(filepath)
#
#
# pdf = PDF()
# pdf.set_title("20000 Leagues Under the Seas")
# pdf.set_author("Jules Verne")
# pdf.print_chapter(1, "A RUNAWAY REEF", "20k_c1.txt")
# pdf.print_chapter(2, "THE PROS AND CONS", "20k_c1.txt")
# pdf.output("tuto3.pdf")