from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic
import os

os.chdir(os.path.dirname(__file__))
with open("data center\hours.txt", "r") as obj:
    _HOURS_ = int(obj.read())


class SallaryReport(QtWidgets.QWidget):
    """a class that create a new window for reporting the net sallary for the employee """

    def __init__(self: "SallaryReport",
            name: str, sallary: float,
            rewards: float = 0,
            addational: float = 0,
            regularity_value: float = 0,
            movements_value: float = 0,
            delay_hours: int = 0,
            absence_days: int = 0,
            borrow_value: float = 0,
            deduction_value: float = 0,
            other_ded: float = 0,
            services_value: float = 0
        ) -> None:
        super(QtWidgets.QWidget, self).__init__()
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
        self.add_sallary_lbl.setText(str(addational))
        self.employee_regularity_lbl.setText(str(regularity_value))
        self.movements_lbl.setText(str(movements_value))
        total_employee_rights = float(sallary) + float(rewards) + float(addational) + float(regularity_value) + float(movements_value)
        self.total_eployee_rights.setText(str(total_employee_rights))
        self.employee_delay_lbl.setText(str(delay_hours))
        self.employee_absence_lbl.setText(str(absence_days))
        self.employee_borrow_lbl.setText(str(borrow_value))
        self.employee_deduction_lbl.setText(str(deduction_value))
        self.other_de_lbl.setText(str(other_ded))
        self.employee_services_lbl.setText(str(services_value))

        # some of important calculations for report
        global _Hours_
        pay_per_day = (float(sallary) / 30)
        pay_per_hour = pay_per_day / _HOURS_
        get_delay = pay_per_hour * int(delay_hours)
        get_absence = pay_per_day * int(absence_days)
        get_borrow = float(borrow_value)
        get_deduction = float(deduction_value)
        get_service = float(services_value)
        employee_loan = get_delay + get_absence + get_borrow + get_deduction + get_service + float(other_ded)
        self.total_employee_loan_lbl.setText(str("{:.2f}".format(employee_loan)))
        # formating the net sallary and display it :)
        net_sallary = (float(total_employee_rights)) - float(employee_loan)
        self.employee_net_sallary.setText(str("{:.2f}".format(net_sallary)))
