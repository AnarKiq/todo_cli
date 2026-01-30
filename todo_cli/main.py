from datetime import datetime

from todo_cli.storage import *
from todo_cli.services import NotFoundError, TodoService


def main() -> None:
    path = "data/todos.json"

    try:
        items = load_items(path)
    except StorageError as e:
        print("Ошибка загрузки:", e)
        items = []

    service = TodoService(items)

    print(
        f"Всего: {service.count_total}, выполнено: {service.count_done}, осталось: {service.count_pending}"
    )

    if service.count_total == 0:
        service.add("Сделать дз")
        service.add("Сходить в магазин")

    try:
        service.mark_done(1, True)
    except NotFoundError as e:
        print("Ошибка:", e)

    try:
        save_items(path, service.items)
        print(f"Сохранено задач: {len(service.items)} -> {path}")
    except StorageError as e:
        print("Ошибка сохранения:", e)


if __name__ == "__main__":
    main()
