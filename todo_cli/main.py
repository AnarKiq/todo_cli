from datetime import datetime

from todo_cli.models import *
from todo_cli.storage import *


def main() -> None:
    path = "data/todos.json"

    try:
        items = load_items(path)
    except StorageError as e:
        print("Ошибка загрузки:", e)
        items = []

    if not items:
        items = [
            TodoItem(
                id=1,
                title="купить молоко",
                created_at=datetime.now().isoformat(),
                done=True,
            ),
            TodoItem(
                id=2,
                title="погладить кота",
                created_at=datetime.now().isoformat(),
                done=True,
            ),
        ]

    try:
        save_item(path, items)
        print(f"Сохранено задач: {len(items)} -> {path}")
    except StorageError as e:
        print("Ошибка сохранения:", e)


if __name__ == "__main__":
    main()
