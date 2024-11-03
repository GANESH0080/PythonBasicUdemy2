import openpyxl

# Created workbook object for WorkBook class
wk = openpyxl.Workbook()
#Printing the active sheet of created workbook
print("Original Sheet Name : " , wk.active.title)


# Created sheet object sh for active sheet
sh = wk.active
# Changing the sheet name and printing the sheetname
sh.title = "HelloGanesh"
print("Updated sheet name : " +sh.title)

# Trying to write data in A4 cell and saving the sheet
sh['A4'].value = "GaneshSalunkhe"
wk.save("D:\\RobotFramework\\PythonBasicsUdemy2\\WriteExcelData.xlsx")


# Creating new sheet using workbook object
wk.create_sheet("Ganesh_Sheet2")

#wk.save("D:\\RobotFramework\\PythonBasicsUdemy2\\WriteExcelData.xlsx")
sh1 = wk["Ganesh_Sheet2"]
sh1['A4'].value = "GaneshSalunkhesheet2"

#Trying to remove the sheet "HelloGanesh" and saving the file
wk.remove(wk["HelloGanesh"])
wk.save("D:\\RobotFramework\\PythonBasicsUdemy2\\WriteExcelData.xlsx")


