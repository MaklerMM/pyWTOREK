from programowanieObiektowe.employee_mgm.controller.CompanyContr import CompanyController
from programowanieObiektowe.employee_mgm.model.Employee import Employee
from programowanieObiektowe.employee_mgm.model.Trainee import Trainee

cc = CompanyController()
cc.getEmployees()
cc.setPrise(1000,"e1")
cc.deleteEmployeeWithConfirm("mk7")