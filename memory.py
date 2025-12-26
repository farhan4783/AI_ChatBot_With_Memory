from database import get_db

def save_message(user_id, role, content):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chat_history (user_id, role, content) VALUES (?, ?, ?)",
        (user_id, role, content)
    )

    conn.commit()
    conn.close()

def get_recent_memory(user_id, limit=6):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT role, content FROM chat_history WHERE user_id=? ORDER BY id DESC LIMIT ?",
        (user_id, limit)
    )

    rows = cursor.fetchall()
    conn.close()

    return list(reversed(rows))  # chronological order
