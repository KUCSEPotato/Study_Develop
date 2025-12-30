# Mango seller search using BFS
from collections import deque

graph = {
    "you":   [("alice", "friend"), ("bob", "friend")],
    "alice": [("mango", "mango seller")],
    "bob":   [("potato", "potato seller")],
    # "mango": [], "potato": []  # 없어도 get으로 처리됨
}

def append_to_search_queue(queue: deque, current_name: str, visited: set):
    """current_name의 이웃을 방문하지 않은 것만 큐에 추가"""
    for name, tag in graph.get(current_name, []):
        if name not in visited:
            queue.append((name, tag))

def is_mango_seller(tag: str) -> bool:
    return tag == "mango seller"

def search_mango_seller(start: str = "you"):
    search_queue = deque()
    visited = set()

    # 시작점의 이웃들을 초기 큐에
    append_to_search_queue(search_queue, start, visited)

    while search_queue:
        name, tag = search_queue.popleft()
        if name in visited:
            continue

        if is_mango_seller(tag):
            print(f"Found mango seller: {name}")
            return name

        visited.add(name)
        append_to_search_queue(search_queue, name, visited)
        print(f"Queue updated: {list(search_queue)}")

    return None

def main():
    print("Starting search for mango seller...")
    if search_mango_seller():
        print("Mango seller found!")
    else:
        print("No mango seller found.")
    print("Search completed.")

if __name__ == "__main__":
    main()
