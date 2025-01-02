import sys

# Banco de dados básico das classes e raças de D&D 5e
classes = {
    "Barbarian": {"strength": 2, "combat": 3, "magic": 0, "stealth": 0},
    "Bard": {"charisma": 3, "magic": 2, "support": 3, "stealth": 1},
    "Cleric": {"wisdom": 3, "magic": 2, "support": 2, "combat": 2},
    "Druid": {"wisdom": 3, "magic": 3, "support": 2, "nature": 3},
    "Fighter": {"strength": 3, "combat": 3, "versatility": 2},
    "Monk": {"dexterity": 3, "wisdom": 2, "combat": 3, "stealth": 1},
    "Paladin": {"strength": 2, "charisma": 2, "combat": 2, "magic": 1},
    "Ranger": {"dexterity": 3, "wisdom": 2, "stealth": 2, "nature": 3},
    "Rogue": {"dexterity": 3, "stealth": 3, "combat": 1},
    "Sorcerer": {"charisma": 3, "magic": 3, "combat": 1},
    "Warlock": {"charisma": 3, "magic": 3, "combat": 2},
    "Wizard": {"intelligence": 3, "magic": 3, "support": 1},
}

races = {
    "Human": {"all": 1},
    "Elf": {"dexterity": 2, "magic": 1},
    "Dwarf": {"constitution": 2, "combat": 1},
    "Halfling": {"dexterity": 2, "stealth": 1},
    "Dragonborn": {"strength": 2, "charisma": 1},
    "Gnome": {"intelligence": 2, "magic": 1},
    "Half-Elf": {"charisma": 2, "versatility": 2},
    "Half-Orc": {"strength": 2, "combat": 1},
    "Tiefling": {"charisma": 2, "magic": 1},
}

def ask_questions():
    print("Bem-vindo ao questionário de classe e raça para D&D 5e!")
    print("Responda as perguntas abaixo com o número correspondente à sua preferência.")

    scores = {key: 0 for key in classes.keys()}

    # Perguntas para determinar a classe
    questions = [
        ("Você prefere lutar corpo a corpo?", {"Barbarian": 3, "Fighter": 3, "Paladin": 2, "Monk": 2}),
        ("Você gosta de usar magia ofensiva?", {"Wizard": 3, "Sorcerer": 3, "Warlock": 2}),
        ("Você prefere ajudar seus aliados?", {"Cleric": 3, "Bard": 3, "Druid": 2}),
        ("Você gosta de atuar furtivamente?", {"Rogue": 3, "Ranger": 2, "Monk": 2}),
        ("Você prefere uma conexão com a natureza?", {"Druid": 3, "Ranger": 3}),
        ("Você gosta de versatilidade em combate?", {"Fighter": 2, "Bard": 2, "Rogue": 1}),
    ]

    for i, (question, impacts) in enumerate(questions, 1):
        print(f"{i}. {question}")
        print("1) Sim  2) Não")

        while True:
            try:
                answer = input("Sua resposta: ").strip()
                if answer not in ["1", "2"]:
                    print("Opção inválida. Por favor, escolha 1 (Sim) ou 2 (Não).")
                    continue
                answer = int(answer)
                break
            except ValueError:
                print("Por favor, responda com 1 (Sim) ou 2 (Não).")

        if answer == 1:
            for cls, score in impacts.items():
                scores[cls] += score

    # Determinar a melhor classe com base na pontuação
    best_class = max(scores, key=scores.get)

    # Sugerir a melhor raça para a classe escolhida
    class_priority = list(classes[best_class].keys())
    best_race = max(races.keys(), key=lambda r: sum(races[r].get(stat, 0) for stat in class_priority))

    print("\n--- Resultado ---")
    print(f"Classe recomendada: {best_class}")
    print(f"Raça recomendada para {best_class}: {best_race}")

if __name__ == "__main__":
    try:
        ask_questions()
    except KeyboardInterrupt:
        print("\nQuestionário interrompido. Até a próxima!")
        sys.exit(0)
