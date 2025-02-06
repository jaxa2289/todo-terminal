from dataclasses import dataclass


from model.file import *



@dataclass
class ToDo(File):
    id : int = None
    title : str = None
    description : str = None
    start_time : str = None
    category : str = None
    status : str = "new"

    def search(self , search_value):
        todos = self.get()
        result = []
        for todo in todos:
            if search_value.lower() in todo.title.lower():
                result.append(todo)
        return result
    def about(self):
        text = f"""
            id: {self.id}
            title: {self.title}
            description: {self.description}
            start_time: {self.start_time}
            status: {self.status}
            category: {self.category}
        """
        return text
    def show(self):
        todos = self.get()
        for pos , todo in enumerate(todos,1):
            print(f"{pos}) {todo.title}")
        print("0) <-back")
        return todos