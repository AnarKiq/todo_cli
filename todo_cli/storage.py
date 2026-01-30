from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from todo_cli.models import *


class StorageError(Exception):
    """Ошибки чтения/записи хранилища"""


def load_items(path: str) -> list[TodoItem]:
    p = Path(path)
    if not p.exists():
        return []

    try:
        with p.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise StorageError(f"Файл '{path}' содержит некорректный JSON") from e
    except OSError as e:
        raise StorageError(f"Не удалось прочитать файл '{path}': {e}") from e

    if not isinstance(data, list):
        raise StorageError(
            f"Ожидался список задач  JSON, но получено: {type(data).__name__}"
        )

    items: list[TodoItem] = []
    for i, row in enumerate(data):
        if not isinstance(row, dict):
            raise StorageError(f"Элемент #{i} в JSON не является объектом (dict)")
        items.append(from_dict(row))

    return items


def save_items(path: str, items: list[TodoItem]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    payload: list[dict[str, Any]] = [to_dict(item) for item in items]

    try:
        with p.open("w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
    except OSError as e:
        raise StorageError(f"Не удалось записать файл '{path}': {e}") from e
