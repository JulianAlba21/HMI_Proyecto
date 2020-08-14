import xlsxwriter
import var

class TomarDatos():
    def __init__(self, nombre=" "):

        #Se crea el libro con un nombre especifico y se crea una hoja de trabajo
        self.nombre=nombre
        self.workbook= xlsxwriter.Workbook(self.nombre + '.xlsx')
        self.worksheet=self.workbook.add_worksheet()

        self.worksheet.set_column('G:G',60)
        self.worksheet.set_zoom(150)

        self.worksheet.write_string('A1', 'TE') #se escribe w valor 1 en excel
        self.worksheet.write_string('B1', 'TG') #se escribe w valor 2 en excel
        self.worksheet.write_string('C1', 'TC') #se escribe w valor 3 en excel
        self.worksheet.write_string('D1', 'TS') #se escribe w valor 4 en excel
        self.worksheet.write_string('E1', 'Frec') #se escribe w Freceuncia en excel
        self.worksheet.write_string('F1', 'TE') #se escribe valor 1 en excel
        self.worksheet.write_string('F2', 'TG') #se escribe valor 2 en excel
        self.worksheet.write_string('F3', 'TC') #se escribe valor 3 en excel
        self.worksheet.write_string('F4', 'TS') #se escribe valor 4 en excel
        self.worksheet.write_string('F5', 'Frec') #se escribe Frecuencia en excel

    def GrafValores(self,row=0):

        self.worksheet.add_sparkline('G1',{'range':'Sheet1!A1:A'+str(row), 'series_color':'#00FEF2'})
        self.worksheet.add_sparkline('G2',{'range':'Sheet1!B1:B'+str(row), 'series_color':'#FCF103'})
        self.worksheet.add_sparkline('G3',{'range':'Sheet1!C1:C'+str(row), 'series_color':'#FF0000'})
        self.worksheet.add_sparkline('G4',{'range':'Sheet1!D1:D'+str(row), 'series_color':'#5A1280'})
        self.worksheet.add_sparkline('G5',{'range':'Sheet1!E1:E'+str(row), 'series_color':'#5A1280'})
        
    def cerrarLibro(self):

        self.workbook.close()
