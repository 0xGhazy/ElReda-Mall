
# A simple GUI python application to calculate the net sallary.
# Coded for elredamall.com - it's free and open source :)
# Coded by: Hossam hamdy (0xGhazy).

import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
# try to import external modules.
# win10toast that control the windows10 notifications.
from win10toast import ToastNotifier
from openpyxl import Workbook
import csv
from datetime import date


def win10_display_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration = 3)


class SallaryReport(QtWidgets.QWidget):
    """a class that create a new window for reporting the net sallary for the employee """

    def __init__(self, name: str, sallary: float, rewards: float = 0, addational: float = 0,
                 regularity_value: float = 0, delay_hours: int = 0, absence_days: int = 0,
                 borrow_value: float = 0, deduction_value: float = 0, services_value: float = 0) -> None:

        super(QtWidgets.QWidget, self).__init__()
        os.chdir(os.path.dirname(__file__))
        uic.loadUi(r"design\report_interface.ui", self)
        self.show()

        # handling empty records
        if rewards == "":
            rewards = 0
        if addational == "":
            addational = 0
        if regularity_value == "":
            regularity_value = 0
        if delay_hours == "":
            delay_hours = 0
        if absence_days == "":
            absence_days = 0
        if borrow_value == "":
            borrow_value = 0
        if deduction_value == "":
            deduction_value = 0
        if services_value == "":
            services_value = 0

        # set values to the lbl in the window
        self.employee_name_lbl.setText(name)
        self.employee_sallary_lbl.setText(sallary)
        self.employee_rewards_lbl.setText(str(rewards))
        self.employee_additional_lbl.setText(str(addational))
        self.employee_regularity_lbl.setText(str(regularity_value))
        total_employee_rights = float(rewards) + float(addational) + float(regularity_value)
        self.total_eployee_rights.setText(str(total_employee_rights))
        self.employee_delay_lbl.setText(str(delay_hours))
        self.employee_absence_lbl.setText(str(absence_days))
        self.employee_borrow_lbl.setText(str(borrow_value))
        self.employee_deduction_lbl.setText(str(deduction_value))
        self.employee_services_lbl.setText(str(services_value))
        # some of important calculations.
        pay_per_day = (float(sallary) / 30)
        pay_per_hour = pay_per_day / 9
        get_delay = pay_per_hour * int(delay_hours)
        get_absence = pay_per_day * int(absence_days)
        get_borrow = float(borrow_value)
        get_deduction = float(deduction_value)
        get_service = float(services_value)
        employee_loan = get_delay + get_absence + get_borrow + get_deduction + get_service
        self.total_employee_loan_lbl.setText(str("{:.2f}".format(employee_loan)))
        # formating the net sallary and display it :)
        net_sallary = (float(sallary) + float(total_employee_rights)) - float(employee_loan)
        self.employee_net_sallary.setText(str("{:.2f}".format(net_sallary)))



class ApplicationUI(QtWidgets.QMainWindow):
    """ Main application Window """

    def __init__(self: "ApplicationUI") -> None:
        super(ApplicationUI, self).__init__()
        os.chdir(os.path.dirname(__file__))
        uic.loadUi(r"design\UI.ui", self)           # loading .ui design file.
        self.show()                                 # display the GUI.
        self.handleButtons()                        # loading the buttons events.


    def handleButtons(self: "ApplicationUI") -> None:
        """ Handling all buttons in the application """
        self.generate_report.clicked.connect(self.generateReportBTN)
        self.refresh_btn.clicked.connect(self.refresh)


    def generateReportBTN(self: "ApplicationUI") -> None:
        """ Function to get a new employee record for a day """
        # Getting user inputs
        name = self.employee_name.text() # -> (+)
        sallary = self.employee_sallary.text()
        rewards = self.rewards.text()
        addational = self.additional_sallary.text()
        regularity_value = self.regularity.text() # -> (-)
        delay_hours = self.delay_hours.text()
        absence_days = self.absence_days.text()
        borrow_value = self.borrow.text()
        deduction_value = self.deduction.text()
        deduction_reason = self.deduction_reason.text()
        services_value = self.services.text()

        if  len(name) == 0 or len(sallary) == 0:
            win10_display_notification("[-] Error Message",
            "لا تستطيع ترك حقل الاسم او المرتب فارغ.")
            exit()
        else:
            self.report = SallaryReport(name, sallary, rewards, addational, regularity_value, delay_hours, \
                                        absence_days, borrow_value, deduction_value, services_value)

            # data_2_xlsx = f"{name}, {sallary}, {rewards}, {addational}, {regularity_value}, {delay_hours}, {absence_days}, {borrow_value}, {deduction_value}, {services_value}"
            # wb = Workbook()
            # ws = wb.active
            

            # dir_content = os.listdir()
            # for item in dir_content:
            #     if item != f"{date.today()}.xlsx":
            #         pass
            #     ws.append(data_2_xlsx)
            #     wb.save('name.xlsx')


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
        self.deduction_reason.clear()
        self.services.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ApplicationUI()
    app.exec_()
