# Useful data

userInput = "ezequiel.gonzalez@enroutesystems.com"
passInput = "-123quielo"
hours = '8'

# Login objects

url = 'https://www.bigtime.net'

loginMain = ".menu-right-side-menu-container:nth-of-type(2) [href='https\:\/\/iq\.bigtime\.net\/']"

username = "input#SUserName"

password = "input#SPassword"

loginSecond = ".btn.btn-block.signin"

# Hour setup objects

selectLists = "[bt-validate] .ng-scope:nth-of-type(1) .projectsid [ng-style]"

taskDropper = ".col.editor-col.tasksid > .bt-select.bt_select_box > .btn_select"

taskop = "PTO"

taskListObject = f"[data-display-name={str(taskop)}]"

projectDropper = ".col.editor-col.projectsid > .bt-select.bt_select_box > .btn_select"

projectop = "Enroute:Rockstars VI"

# projectListObject = f"[data-display-name={str(projectop)}]"

projectListObject = f"[data-display-name=\"Enroute:Rockstars VI\"]"

# days

sun = "td:nth-of-type(3)  .form-control.ng-not-empty.ng-pristine.ng-untouched.ng-valid"
mon = "td:nth-of-type(4)  .form-control.ng-not-empty.ng-pristine.ng-untouched.ng-valid"
tue = "td:nth-of-type(5)  .form-control.ng-not-empty.ng-pristine.ng-untouched.ng-valid"
wed = "td:nth-of-type(6)  .form-control.ng-not-empty.ng-pristine.ng-untouched.ng-valid"
thu = "td:nth-of-type(7)  .form-control.ng-not-empty.ng-pristine.ng-untouched.ng-valid"
fri = "td:nth-of-type(8)  .form-control.ng-not-empty.ng-pristine.ng-untouched.ng-valid"
sat = "td:nth-of-type(9)  .form-control.ng-not-empty.ng-pristine.ng-untouched.ng-valid"

week = [mon, tue, wed, thu, fri]

save = "[bt-process='saveRow\(activeRow\)']"