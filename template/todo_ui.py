
from template.category_ui import *
from model.todo1 import *

class UITodo:
    session_todo: Optional['ToDo'] = None

    def main(self):
        from template.acount_ui import UIaccount
        menu = """
            *) Search 🔍
            1) Add
            2) List
            0) <-back
            >>>"""
        key = input(menu)
        assert key in ("*", "1", "2", "0"), "Menuyada yo'q bo'lim tanlandi"

        match key:
            case "1":
                self.add()
            case "2":
                self.list()
            case "*":
                short_name = input("🔍>>>")
                find_todos = ToDo().search(short_name)
                for i, todo in enumerate(find_todos, 1):
                    print(f"{i}) {todo.title}")
                print("0) <-back")
                pos = input(">>>")
                if pos == "0":
                    self.main()
                    return
                self.session_todo = find_todos[int(pos) - 1]
                self.settings()
            case"0":
                UIaccount().panel()


    def settings(self):
        menu = """
                    1) delete
                    2) update
                    3) about
                    0) <-back
                    >>>"""
        match input(menu):
            case "0":
                self.main()
            case "3":
                print(self.session_todo.about())
                self.settings()
            case "1":
                self.session_todo.delete()
                self.main()
            case "2":
                fields = """
                    1) title
                    2) description
                    3) start time
                    4) status
                    5) category
                    0) <-back
                >>>"""
                key = input(fields)
                if key == "0":
                    self.settings()
                    return

                match key:
                    case "1":
                        new_value = input("New title:")
                        self.session_todo = self.session_todo.update("title", new_value)

                    case "2":
                        new_value = input("New description:")
                        self.session_todo = self.session_todo.update("description", new_value)

                    case "3":
                        new_value = input("New start time:")
                        self.session_todo = self.session_todo.update("start_time", new_value)

                    case "4":
                        status = """
                            1) New
                            2) Processing
                            3) Completed
                        >>>"""
                        key = input(status)
                        _map = {
                            "1" : "new",
                            "2" : "processing",
                            "3" : "completed"
                        }
                        status = _map[key]
                        self.session_todo = self.session_todo.update("status", status)
                    case "5":
                        categories = Category().show()
                        pos = input(">>>")
                        if pos == "0":
                            self.settings()
                            return

                        choice_cat = categories[int(pos)-1]

                        self.session_todo = self.session_todo.update("category" ,choice_cat.id )
                self.settings()

    def list(self):
        todos = ToDo().show()
        pos = input(">>>")
        if pos == "0":
            self.main()
        self.session_todo = todos[int(pos)-1]
        self.settings()

    def add(self):
        categories = Category().show()

        pos = input(">>>")
        if pos == "0":
            self.main()
        todo = {
            "category" : categories[int(pos) - 1].id,
            "title" : input("Title:"),
            "description" : input("Description:"),
            "start_time" : input("Start_time:")
        }
        ToDo(**todo).save()
        self.main()