from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            searched.append(person)
            if person_is_seller(person):
                print(f"{person} sprzedaje mango!")
                return 0
            else:
                search_queue += graph[person]

    print("Nikt nie sprzedaje mango")


graph = {}
graph["ty"] = ["alicja", "bartek", "cecylia"]
graph["bartek"] = ["janusz", "patrycja"]
graph["alicja"] = ["patrycja"]
graph["cecylia"] = ["tamara", "jarek"]
graph["janusz"] = []
graph["patrycja"] = []
graph["tamara"] = []
graph["jarek"] = []
search("ty")