from dataclasses import dataclass

from model.file import *



@dataclass
class Category(File):
    id : int = None
    name : str = None

    def show(self):
        categories = self.get()
        for index , category in enumerate(categories,1):
            print(f"{index}) {category.name}")
        print("0) <-back")
        return categories


    def search(self , search_value)->list['Category']:
        categories: list['Category'] = self.get()
        result = []
        for category in categories:
            if search_value.lower() in category.name.lower():
                result.append(category)
        return result

    def about(self):
        text = f"""
            id : {self.id}
            name : {self.name}
        """
        return text