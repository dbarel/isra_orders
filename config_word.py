from docx import Document
from docx.shared import Pt
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import RGBColor


def setup_doc() -> [Document, WD_STYLE_TYPE]:
    """creating word document style and fonts"""
    document = Document()

    # word doc styles:
    rtl_style = document.styles.add_style('rtl', WD_STYLE_TYPE.PARAGRAPH)
    rtl_style.paragraph_format.alignment = 2

    font = rtl_style.font
    font.name = 'Arial'
    font.size = Pt(12)

    rtl2_style = document.styles.add_style('rtl2', WD_STYLE_TYPE.PARAGRAPH)
    rtl2_style.paragraph_format.alignment = 2
    font2 = rtl2_style.font
    font2.name = 'Arial'
    font2.size = Pt(11)
    font2.italic = True

    rtl_style = document.styles.add_style('rtl_red', WD_STYLE_TYPE.PARAGRAPH)
    rtl_style.paragraph_format.alignment = 2

    font_red = rtl_style.font
    font_red.name = 'Arial'
    font_red.size = Pt(12)
    font_red.bold = True
    font_red.color.rgb = RGBColor(0xFF, 0x00, 0x00)
    return document, rtl2_style
