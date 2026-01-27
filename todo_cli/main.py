from datetime import datetime

from todo_cli.models import (
    TodoItem,
    to_dict,
    from_dict,
    titles,
    done_items,
    pending_items,
)


def main() -> None:
    items = [
        TodoItem(id=1, title="купить молоко", created_at=datetime.now().isoformat()),
        TodoItem(
            id=2,
            title="погладить кота",
            created_at=datetime.now().isoformat(),
            done=True,
        ),
    ]
    print("titles:", titles(items))
    print("done:", [i.id for i in done_items(items)])
    print("pending:", [i.id for i in pending_items(items)])

    d = to_dict(items[0])
    print("to_dict:", d)
    restored = from_dict(d)
    print("restored:", restored)


if __name__ == "__main__":
    main()
