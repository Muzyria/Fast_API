import fastapi
import database
import pydantic_models
import config

api = fastapi.FastAPI()


@api.get('/static/path')
def hello():
    return "hello"


@api.get('/user/{nick}')  # переменные в пути заключаются в фигурные скобки
def get_nick(nick):  # в функцию передаем эту переменную и работаем с ней дальше
    return {"user": nick}  # при запросе страницы вернет строку, которую мы вписали после последнего слеша


@api.get('/userid/{id:int}')  # мы можем задавать тип данных прямо в пути через двоеточие
def get_id(id):  # тут в пути обязательно должно быть число, иначе возникнет ошибка
    return {"user": id}


@api.get('/user_id/{id}')
def get_id2(id: int):  # либо же его можно задавать как тайп-хинт прямо в функции
    return {"user": id}  # возвращается число, а не строка, как было бы без объявления типа данных


@api.get('/user_id_str/{id:str}')
def get_id2(id):
    return {"user": id}  # тут id - это уже строка, так как мы объявили тип данных


@api.get('/test/{id:int}/{text:str}/{custom_path:path}')
def get_test(id, text, custom_path):
    return {"id": id,
            "": text,
            "custom_path": custom_path}


fake_database = {'users': [
    {
        "id": 1,  # тут тип данных - число
        "name": "Anna",  # тут строка
        "nick": "Anny42",  # и тут
        "balance": 15.01  # а тут float
    },

    {
        "id": 2,  # у второго пользователя
        "name": "Dima",  # такие же
        "nick": "dimon2319",  # типы
        "balance": 8.01  # данных
    }
    , {
        "id": 3,  # у третьего
        "name": "Vladimir",  # юзера
        "nick": "Vova777",  # мы специально сделаем
        "balance": "23"  # нестандартный тип данных в его балансе
    }
], }
