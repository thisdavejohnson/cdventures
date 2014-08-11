#########################
#
# The data format should be:
#   0 - firstName
#   1 - lastName
#   2 - birthday
#   3 - avgHoursWorked
#   4 - addressFirstLine
#   5 - addressSecondLine
#   6 - city
#   7 - state
#   8 - zipcode
#   9 - race
#  10 - flsaStatus
#  11 - veteranStatus
#  12 - milStatus
#
#########################

import xlrd 
from compliance.models import Organization, Employee

class ExcelParser(object, excel_name):
    @transaction.commit_on_success        
    def read_excel(self):
        wb = xlrd.open_workbook(excel_name)
        org = Organization.objects.get(pk=1)
        
        # get the first sheet
        sheet = wb.sheet_by_index(0)
        
        for row_index in range(sheet.nrows):
            
            # create a new Employee object
            employee = Employee()
            employee.organization = organization

            employee.firstName = sheet.cell(row_index,0).value
            employee.lastName = sheet.cell(row_index,1).value
            employee.birthday = sheet.cell(row_index,2).value
            employee.avgHoursWorked = sheet.cell(row_index,3).value
            employee.addressFirstLine = sheet.cell(row_index,4).value
            employee.addressSecondLine = sheet.cell(row_index,5).value
            employee.city = sheet.cell(row_index,6).value
            employee.state = sheet.cell(row_index,0).value
            employee.zipcode = sheet.cell(row_index,0).value
            employee.race = sheet.cell(row_index,0).value
            employee.zipcode = sheet.cell(row_index,0).value
            employee.flsaStatus = sheet.cell(row_index,0).value
            employee.veteranStatus = sheet.cell(row_index,0).value
            employee.milStatus = sheet.cell(row_index,0).value
                
                
        
        
        