def GetEmpName():
    empname = input("Enter employee name: ")
    return empname

def GetDatesWorked():
    from_date = input("Enter from date (mm/dd/yyyy): ")
    to_date = input("Enter to date(mm/dd/yyyy): ")
    return from_date, to_date

def GetHoursWorked():
    hours = float(input ("Enter total hours worked: "))
    return hours

def GetHourlyRate():
    hourlyrate = float(input ("Enter employee's hourly rate: "))
    return hourlyrate

def GetTaxRate():
    taxrate = float(input ("Enter the tax rate in percentage: "))
    return taxrate

def CalculateTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(DetailsPrinted):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
while True:
 rundate = input ("Enter start date for report (MM/DD/YYYY) or All for all data in file: ")
 if (rundate.upper() == "ALL"):
     break
 try:
     rundate = datetime.strptime(rundate, "%m/%d/%Y")
     break
 except ValueError:
     print("Invalid date format. Try again.")
     print()
     continue
 while True:
     if not EmpDetail:
         break
fromdate = EmpList[0]
if (str(rundate).upper() != "ALL"):
    checkdate = datetime.strptime(fromdate, "%m/%d/%Y")
    if (checkdate < rundate):
        todate = EmpList[1]
        empname = EmpList[2]
        hours = float(EmpList[3])
        hourlyrate = float(EmpList[4])
        taxrate = float(EmpList[5])
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        EmpTotals["TotEmp"] = TotEmployees
        EmpTotals["TotHrs"] = TotHours
        EmpTotals["TotGrossPay"] = TotGrossPay
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNetPay"] = TotNetPay
        DetailsPrinted = True
if (DetailsPrinted):
    PrintTotals (EmpTotals)
else:
    print("No detail information to print")
def PrintTotals(EmpTotals):
    print()
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Hours Worked: {EmpTotals["TotHrs"]:,.2f}')
    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]:,.2f}')
    print(f'Total Income Tax: {EmpTotals["TotTax"]:,.2f}')
    print(f'Total Net Pay: {EmpTotals["TotNetPay"]:,.2f}')

if __name__ == "__main__":
    EmpTotals = []
    DetailsPrinted = False
    while True:
     empname = GetEmpName()
     if (empname.upper() == "END"):
         break
     fromdate, todate = GetDatesWorked()
     hours = GetHoursWorked()
     hourlyrate = GetHourlyRate()
     taxrate = GetTaxRate()
printinfo(DetailsPrinted)


