from __future__ import annotations

from datetime import datetime
from pydantic import ValidationError

from todo_cli.models import TodoItem


class TodoError(Exception):
    """Базовая ошибка todo-сервиса"""


class NotFoundError(TodoError):
    """Задача с указаным id не найдена"""


class TodoService:
    def __init__(self, items: list[TodoItem] | None = None) -> None:
        self._items = list(items) if items else []

    @property
    def items(self) -> list[TodoItem]:
        return list(self._items)

    @property
    def count_total(self) -> int:
        return len(self._items)

    @property
    def count_done(self) -> int:
        return sum(1 for item in self._items if item.done)

    @property
    def count_pending(self) -> int:
        return self.count_total - self.count_done

    def titles(self, items: list[TodoItem]) -> list[str]:
        return [item.title for item in self._items]

    def done_items(self, items: list[TodoItem]) -> list[TodoItem]:
        return [item for item in self._items if item.done]

    def pending_items(self, items: list[TodoItem]) -> list[TodoItem]:
        return [item for item in self._items if not item.done]

    def _next_id(self) -> int:
        if not self._items:
            return 1
        return max(item.id for item in self._items) + 1

    def add(self, title: str) -> TodoItem:

        item = TodoItem(
            id=self._next_id(),
            title=title,
            created_at=datetime.now().isoformat(timespec="seconds"),
            done=False,
        )
        self._items.append(item)
        return item


    def get(self, item_id: int) -> TodoItem:
        for item in self._items:
            if item.id == item_id:
                return item
        raise NotFoundError(f"Задача с id={item_id} не найдена")

    def mark_done(self, item_id: int, done: bool = True) -> TodoItem:

        for idx, item in enumerate(self._items):
            if item.id == item_id:
                updated = TodoItem(
                    id = item.id,
                    created_at = item.created_at,
                    title = item.title,
                    done = done
                )
                self._items[idx] = updated
                return updated
        raise NotFoundError(f"Задача с id={item_id} не найдена")

    def delete(self, item_id: int) -> None:
        for idx, item in enumerate(self._items):
            if item.id == item_id:
                del self._items[idx]
                return
        raise NotFoundError(f"Задача с id={item_id} не найдена")

    def clear_done(self) -> int:
        before = len(self._items)
        self._items = [item for item in self._items if not item.done]
        return before - len(self._items)
