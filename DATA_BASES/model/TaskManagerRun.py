from DATA_BASES.controller.TaskManagerController import TaskManagerController

start = TaskManagerController()
# start.insertUser('jarek@onet.pl', 'jarek123', 'Prezes', 'Malutki', 'M')
# start.selectUsers()
# start.insertTaskToUser("programowanie", "w Pythonie","w toku","2020-12-05", 3)
start.updateTaskDateStop("2020-02-20", 2)
# start.selectSummary()
