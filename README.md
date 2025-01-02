# D&D 5e Class and Race Selector

## Overview
This project is a Python-based interactive questionnaire designed to help players of **Dungeons & Dragons 5th Edition (D&D 5e)** choose the most suitable class and race for their character. Based on the user's preferences and responses to a series of questions, the program calculates scores for different classes and suggests the best match, along with an optimized race for that class.

## Features
- **Interactive Questionnaire**: Users answer simple Yes/No questions to define their character preferences.
- **Class Recommendation**: Determines the best class based on weighted scores.
- **Race Suggestion**: Suggests an optimized race for the chosen class, considering racial bonuses and synergies.
- **Error Handling**: Validates user inputs to ensure a smooth experience.

## How It Works
1. The user is presented with a series of questions about their gameplay preferences (e.g., melee combat, magic usage, stealth).
2. Each response adjusts the scores for various classes according to predefined weights.
3. Once all questions are answered, the program:
   - Identifies the class with the highest score.
   - Suggests the race that provides the best synergy with the chosen class.
4. The final results are displayed, including the recommended class and race.

## Installation
1. Clone this repository or download the source code:
   ```bash
   git clone https://github.com/yourusername/dnd-5e-class-selector.git
   ```
2. Ensure you have Python 3 installed on your system.
3. Navigate to the project directory:
   ```bash
   cd dnd-5e-class-selector
   ```
4. Run the program:
   ```bash
   python selector.py
   ```

## Usage
1. Run the script using Python:
   ```bash
   python selector.py
   ```
2. Follow the prompts and answer the questions with `1` (Yes) or `2` (No).
3. View the recommended class and race at the end of the questionnaire.

## Example
```
Bem-vindo ao questionário de classe e raça para D&D 5e!
Responda as perguntas abaixo com o número correspondente à sua preferência.

1. Você prefere lutar corpo a corpo?
1) Sim  2) Não
Sua resposta: 1

2. Você gosta de usar magia ofensiva?
1) Sim  2) Não
Sua resposta: 2

--- Resultado ---
Classe recomendada: Fighter
Raça recomendada para Fighter: Human
```

## Customization
- **Add New Questions**: Modify the `questions` list in the `ask_questions` function to include additional preferences.
- **Adjust Class Weights**: Update the `classes` dictionary to tweak the scoring system.
- **Expand Races**: Add new races to the `races` dictionary for more options.

## Dependencies
This script has no external dependencies and runs on any standard Python 3 installation.

## Contributions
Feel free to contribute to this project by submitting pull requests or suggesting new features! Whether you want to improve the logic, expand the database, or enhance the user interface, all contributions are welcome.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Credits
Created by [Your Name/Username].

Inspired by the official materials of **Dungeons & Dragons 5th Edition** by Wizards of the Coast.

