# from os import write
#
# from fpdf import FPDF
#
# data_for_cv: dict = {
#     'name': 'Michael',
#     'surname': 'іііівіфввфі',
#     'number': '+380997526973',
#     'email': 'mp.gplay@gmail.com',
#     'linkedin': 'https://www.linkedin.com/in/michael-pashkov/',
# }
#
#
# class PDF(FPDF):
#     x_pos = 0
#     y_pos = 0
#
#     def footer(self):
#         # Setting position at 1.5 cm from bottom:
#         self.set_y(-15)
#         # Setting font: helvetica italic 8
#         self.set_font("helvetica", "B", 8)
#         # Setting text color to gray:
#         # self.set_text_color()
#         # Printing page number
#         self.cell(0, 10, "CVLite", align="C")
#
#     def chapter_title(self):
#         # Setting font: helvetica 12
#         self.set_font("helvetica", "", 16)
#         # Setting background color
#         width = self.get_string_width(self.title) + 150
#         self.set_y(20)
#         self.set_x(50)
#         # self.set_draw_color(0, 80, 180)
#         self.set_fill_color(241, 234, 226)
#         # Printing chapter name:
#         self.cell(
#             width,
#             12,
#             "",
#             align="C",
#             fill=True,
#         )
#
#     def add_name(self):
#         self.set_font("DejaVu", style='', size=24)
#         self.set_y(24)
#         self.set_x(125)
#         self.cell(
#             w=0,
#             h=6,
#             txt=f"{data_for_cv['name'].upper()}",
#             align="l",
#             fill=False,
#         )
#         self.set_y(34)
#         self.set_x(125)
#         self.set_font("DejaVu", style='', size=24)
#         self.cell(
#             w=0,
#             h=6,
#             txt=f"{data_for_cv['surname'].upper()}",
#             align="l",
#             fill=False,
#         )
#         self.set_font("helvetica", size=12)
#
#     def add_cv_position(self):
#         self.set_font("helvetica", style='', size=14)
#         self.set_y(49)
#         self.set_x(125)
#         self.cell(
#             w=0,
#             h=6,
#             txt="JOB CV POSITION",
#             align="l",
#             fill=False,
#         )
#
#     def add_about_you(self):
#         self.set_font("helvetica", style='', size=12)
#         self.set_y(60)
#         self.set_x(89)
#         self.multi_cell(
#             w=110,
#             h=10,
#             txt='about me about me about me about me about me about me about me about me about me about me about me about me about me about me about me about me about me about me about me about me about me about me about me about me about me about me about me about',
#             align="l",
#         )
#
#     def add_hard_skills(self):
#         self.set_font("helvetica", style='', size=14)
#         self.set_y(117)
#         self.set_x(125)
#         self.cell(
#             w=0,
#             h=6,
#             txt="HARD SKILLS",
#             align="l",
#             fill=False,
#         )
#
#     def add_hard_skill(self):
#         self.set_font("helvetica", style='', size=12)
#         self.set_y(127)
#         self.set_x(89)
#         self.multi_cell(
#             w=110,
#             h=10,
#             txt='text text text text text text text text text text text text text text text text text text text text text text text text text text',
#             align="l",
#         )
#
#     def add_experience(self):
#         self.set_font("helvetica", style='', size=14)
#         self.set_y(205)
#         self.set_x(125)
#         self.cell(
#             w=0,
#             h=6,
#             txt="EXPERIENCE",
#             align="l",
#             fill=False,
#         )
#
#     def add_experience_sample(self):
#         self.set_font("helvetica", style='', size=12)
#         self.set_y(215)
#         self.set_x(89)
#         self.multi_cell(
#             w=110,
#             h=10,
#             txt='text text text text text text text text text text text text text text text text text text text text text text text text text text',
#             align="l",
#         )
#
#     def add_number(self):
#         self.set_font("helvetica", style='B', size=12)
#         self.set_y(85)
#         self.set_x(10)
#         self.cell(
#             w=0,
#             h=6,
#             txt="Phone:",
#             align="l",
#             fill=False,
#         )
#         self.set_y(85)
#         self.set_x(26)
#         self.set_font("helvetica", style='', size=12)
#         self.cell(
#             w=0,
#             h=6,
#             txt=f"{data_for_cv['number']}",
#             align="l",
#             fill=False,
#         )
#         self.set_font("helvetica", size=12)
#
#     def add_email(self):
#         self.set_font("helvetica", style='B', size=12)
#         self.set_y(95)
#         self.set_x(10)
#         self.cell(
#             w=0,
#             h=6,
#             txt="Email:",
#             align="l",
#             fill=False,
#         )
#         self.set_y(95)
#         self.set_x(26)
#         self.set_font("helvetica", style='', size=12)
#         self.cell(
#             w=0,
#             h=6,
#             txt=f"{data_for_cv['email']}",
#             align="l",
#             fill=False,
#         )
#         self.set_font("helvetica", size=12)
#
#     def add_liked_in_url(self):
#         self.set_font("helvetica", size=12)
#         self.set_y(105)
#         self.set_x(10)
#         self.cell(
#             w=18,
#             h=6,
#             txt="LinkedIn",
#             align="l",
#             fill=False,
#             link=data_for_cv['linkedin'],
#             border=1
#         )
#
#     def add_language_skills(self):
#         self.set_font("helvetica", style='', size=14)
#         self.set_y(120)
#         self.set_x(10)
#         self.cell(
#             w=0,
#             h=6,
#             txt="LANGUAGE SKILLS",
#             align="l",
#             fill=False,
#         )
#
#     def add_languages(self):
#         self.set_font("helvetica", style='B', size=12)
#         self.set_y(135)
#         self.set_x(10)
#         self.cell(
#             w=0,
#             h=6,
#             txt="English:",
#             align="l",
#             fill=False,
#         )
#         self.set_y(135)
#         self.set_x(30)
#         self.set_font("helvetica", style='', size=12)
#         self.cell(
#             w=0,
#             h=6,
#             txt='English text',
#             align="l",
#             fill=False,
#         )
#         self.set_font("helvetica", size=12)
#
#     def add_soft_skills(self):
#         self.set_font("helvetica", style='', size=14)
#         self.set_y(160)
#         self.set_x(10)
#         self.cell(
#             w=0,
#             h=6,
#             txt="SOFT SKILLS",
#             align="l",
#             fill=False,
#         )
#
#     def add_soft_skill(self):
#         self.set_font("helvetica", style='', size=12)
#         self.set_y(175)
#         self.set_x(10)
#         self.multi_cell(
#             w=70,
#             h=10,
#             txt='text text text text text text text text text text text text text text text text text text text text text text text text text text text text',
#             align="l",
#         )
#
#     def create_cv_template(self):
#         self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
#         self.add_page()
#         self.chapter_title()
#         self.add_name()
#         self.add_cv_position()
#         self.add_about_you()
#         self.add_hard_skills()
#         self.add_hard_skill()
#         self.add_experience()
#         self.add_experience_sample()
#         self.add_number()
#         self.add_email()
#         self.add_liked_in_url()
#         self.add_language_skills()
#         self.add_languages()
#         self.add_soft_skills()
#         self.add_soft_skill()
#         self.image('new_avatar_170.png', 10, 10)
#
#
# pdf = PDF()
# pdf.set_title("P PP PP PP PP")
# pdf.create_cv_template()
# x = pdf.output("media/tuto342235.pdf")
