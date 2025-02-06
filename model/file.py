
from pathlib import Path
from os.path import join


BASE_DIR = Path(__file__).parent.parent
DB_PATH = join(BASE_DIR, "database")


class File:
    def write(self, datas: list):
        file_name = self.__class__.__name__.lower() + 's.txt'
        make_string = []
        for data in datas:
            tmp = "|".join(map(str, data.__dict__.values())) + '\n'
            make_string.append(tmp)
        with open(join(DB_PATH, file_name), 'w') as f:
            f.writelines(make_string)

    def save(self):
        datas: list = self.get()
        self.id = int(datas[-1].id) + 1 if datas else 1
        datas.append(self)
        self.write(datas)

    def get(self) -> list:
        file_name = self.__class__.__name__.lower() + "s.txt"
        if not Path(join(DB_PATH, file_name)).exists():
            with open(join(DB_PATH, file_name), 'x') as f:
                pass
        with open(join(DB_PATH, file_name)) as f:
            datas = f.readlines()
        result = []
        for data in datas:
            obj = self.__class__(*data.strip().split("|"))
            result.append(obj)
        return result

    def update(self, field, new_value) -> object:
        datas: list = self.get()

        x = object
        for obj in datas:
            if obj.id == str(self.id):
                setattr(obj, field, new_value)
                x = obj
        self.write(datas)

        return x

    def delete(self):
        datas: list = self.get()
        x = object
        for data in datas:
            if data.id == str(self.id):
                datas.remove(data)
                x = data
        self.write(datas)
        return x

