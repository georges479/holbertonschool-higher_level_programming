#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    # Récupérer tous les noms définis dans le module hidden_4
    names = dir(hidden_4)
    # Filtrer et trier les noms
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
