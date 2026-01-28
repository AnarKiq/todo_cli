from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class TodoItem:
    id: int
    title: str
    created_at: str  # ISO строка, например "2026-01-26T12:34:56"
    done: bool = False


def to_dict(item: TodoItem) -> dict[str, Any]:
    return asdict(item)


def from_dict(data: dict[str, Any]) -> TodoItem:
    # Базовая валидация + применение типов, чтобы JSON не ломал программу
    return TodoItem(
        id=int(data["id"]),
        title=str(data["title"]),
        created_at=str(data["created_at"]),
        done=bool(data.get("done", False)),
    )


def titles(items: list[TodoItem]) -> list[str]:
    return [item.title for item in items]


def done_items(items: list[TodoItem]) -> list[TodoItem]:
    return [item for item in items if item.done]


def pending_items(items: list[TodoItem]) -> list[TodoItem]:
    return [item for item in items if not item.done]
