from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Any


class TodoItem(BaseModel):
    id: int
    created_at: str  # ISO строка, например "2026-01-26T12:34:56"
    title: str = Field("...", min_length=3, max_length=100)
    done: bool = False


def to_dict(item: TodoItem) -> dict[str, Any]:
    return {"id" : item.id,
            "created_at": item.created_at,
            "title" : item.title,
            "done" : item.done
            }


def from_dict(data: dict[str, Any]) -> TodoItem:
    # Базовая валидация + применение типов, чтобы JSON не ломал программу
    return TodoItem(
        id = data["id"],
        created_at = data["created_at"],
        title = data["title"],
        done = data.get("done", False),
    )
