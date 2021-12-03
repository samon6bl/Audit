from docxtpl import DocxTemplate,RichText
ds = DocxTemplate('word1.docx')
context = {'sb' : RichText("林康琪",color='FF0000',bold=True,underline=True,size=40,font="Simson"),"SB":"林son"}
ds.render(context)
ds.save("SB.docx")
