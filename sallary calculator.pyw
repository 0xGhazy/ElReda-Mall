
# A simple GUI python application to calculate the net sallary.
# Coded for elredamall.com - it's free and open source :)
# Coded by: Hossam hamdy (0xGhazy).

import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic
from openpyxl import Workbook
from openpyxl.workbook import Workbook
from datetime import date
import xlsxwriter
from cores import functions
import sallary_report


os.chdir(os.path.dirname(__file__))
with open("data center\hours.txt", "r") as obj:
    _HOURS_ = int(obj.read())


class ApplicationUI(QtWidgets.QMainWindow):
    """ Main application Window """

    def __init__(self: "ApplicationUI") -> None:
        super(ApplicationUI, self).__init__()
        uic.loadUi(r"design\UI.ui", self)           # loading .ui design file.
        self.show()                                 # display the GUI.
        self.handleButtons()                        # loading the buttons events.


    def handleButtons(self: "ApplicationUI") -> None:
        """ Handling all buttons in the application """
        self.generate_report.clicked.connect(self.generateReportBTN)
        self.refresh_btn.clicked.connect(self.refresh)
        self.generate_finall_report.clicked.connect(self.generatFinallReport)


    def generateReportBTN(self: "ApplicationUI") -> None:
        """ Function to get a new employee record for a day """

        # Reading user's inputs
        name = self.employee_name.text()
        sallary = self.employee_sallary.text()
        rewards = self.rewards.text()
        addational = self.additional_sallary.text()
        regularity_value = self.regularity.text()
        movements_value = self.movements.text()
        delay_hours = self.delay_hours.text()
        absence_days = self.absence_days.text()
        borrow_value = self.borrow.text()
        deduction_value = self.deduction.text()
        other_deduction = self.other_deduction.text()
        services_value = self.services.text()

        if  len(name) == 0 or len(sallary) == 0:
            functions.win10_display_notification("[-] Error Message", "You cann't leave 'name' or 'main salary' fields empty")
            exit()
        else:
            self.report = sallary_report.SallaryReport(name,
                            sallary,
                            rewards,
                            addational,
                            regularity_value,
                            movements_value,
                            delay_hours,
                            absence_days,
                            borrow_value,
                            deduction_value,
                            other_deduction,
                            services_value
                        )

            try:
                record_content = f"{str(name)},{str(sallary)},{str(rewards)},{str(addational)},{str(regularity_value)},{str(movements_value)},{str(delay_hours)},{str(absence_days)},{str(borrow_value)},{str(deduction_value)},{str(other_deduction)},{str(services_value)}\n"
                with open(r"{0}\data center\records.txt".format(os.getcwd()), "a+") as record:
                    record.write(record_content)
            except Exception as error_message:
                print(f"[-] \n{error_message}\n")


    def refresh(self: "ApplicationUI") -> None:
        """ Function to clear all text records """
        self.employee_name.clear()
        self.employee_sallary.clear()
        self.rewards.clear()
        self.additional_sallary.clear()
        self.regularity.clear()
        self.delay_hours.clear()
        self.absence_days.clear()
        self.borrow.clear()
        self.deduction.clear()
        self.other_deduction.clear()
        self.services.clear()


    def generatFinallReport(self) -> None:
        """
        """


        # reading the csv file.
        with open (r"{0}\data center\records.txt".format(os.getcwd()), "r") as csv_file:
            csv_content = csv_file.readlines()

        # sheet headers
        headers = [
            'اسم الموظف',
            'الراتب الاساسي',
            'المكافأت',
            'الراتب الأضافي',
            'انتظام',
            'الانتقالات',
            'التأخير (عدد الساعات)',
            'الغياب',
            'السلف',
            'الخصم',
            'اخري',
            'التأمينات',
            'اجمالي المستحقات',
            'اجمالي المقتطعات',
            'الراتب الصافي',
        ]

        file_name = f'Report-{date.today()}.xlsx'
        workbook = xlsxwriter.Workbook(file_name) # Create a workbook
        workbook_name = r"{0}\data center\{1}".format(os.getcwd(), file_name)
        wb = Workbook()
        page = wb.active
        page.title = 'Sheet1'
        page.append(headers)    # write the headers to the first line

        # Resolving csv lines content
        for line in csv_content:
            finall_quiry = []
            main_sallary = 0
            net_sallary = 0
            total_cut = 0
            total_add = 0
            get_delay = 0
            get_absence = 0
            pay_per_day = 0
            pay_per_hour = 0
            line = line.strip("\n").split(",")

            finall_quiry.append(line[0])            # name      ----> (+)
            finall_quiry.append(float(line[1]))     # main sallary
            finall_quiry.append(float(line[2]))     # rewards
            finall_quiry.append(float(line[3]))     # addational sallary
            finall_quiry.append(float(line[4]))     # regularity_value
            finall_quiry.append(float(line[5]))     # movements ----> (-)
            finall_quiry.append(int(line[6]))       # delay_hours
            finall_quiry.append(int(line[7]))       # absence_days
            finall_quiry.append(float(line[8]))     # borrow_value
            finall_quiry.append(float(line[9]))     # deduction_value
            finall_quiry.append(float(line[10]))    # other deductions
            finall_quiry.append(float(line[11]))    # services_value

            # Calculation for excel sheet 
            global _HOURS_
            main_sallary = float(line[1])
            pay_per_day = (main_sallary / 30)
            pay_per_hour = pay_per_day / _HOURS_
            get_delay = pay_per_hour * int(line[6])
            get_absence = pay_per_day * int(line[7])
            total_add = float(main_sallary) + float(line[2]) + float(line[3]) + float(line[4]) + float(line[5])
            finall_quiry.append(str("{:.2f}".format(total_add)))    # total addational
            total_cut = get_delay + get_absence + float(line[8]) + float(line[9]) + float(line[10]) + float(line[11])
            finall_quiry.append(str("{:.2f}".format(total_cut)))    # total cut
            net_sallary = total_add - total_cut
            finall_quiry.append(str("{:.2f}".format(net_sallary)))
            
            page.append(finall_quiry)   # appending data to xlsx file

        wb.save(filename = workbook_name)
        functions.win10_display_notification("[+] Confirmation message", "The report has been created and you can find it at /data center/Report-xxxx-xx-xx")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ApplicationUI()
    app.exec_()
