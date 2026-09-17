🎲 Dice Rolling Simulator

A simple Python Dice Rolling Simulator that uses Python's random number generator to simulate a standard six-sided die.
The program displays an ASCII-art representation of the rolled face and asks the user whether they want to roll again.

📌 Project Overview

This project demonstrates basic Python concepts such as:
Importing and using Python's `random` module
Functions
Random number generation
Conditional statements (`if`)
User input
Recursion for repeating the roll
ASCII-art output

⚙️ How It Works

The `roll()` function is called.
A random integer from 1 to 6 is generated.
The corresponding ASCII-art die face is printed.
The user is asked whether they want to roll again.
If the user enters `y`, the `roll()` function is called again.
If the user enters `n`, the program ends.
The core randomization is performed with:
```python
no = randint(1, 6)
```
This gives each integer from 1 through 6 an equal probability under the standard behavior of Python's pseudo-random number generator.

▶️ How to Run
Requirements
Python 3.14
Run the program
Clone/download the repository and run:
```bash
python Dice.py
```
Depending on your system, you may need:
```bash
python3 Dice.py
```

🖥️ Example Output
```text
       \[---------]
       |o       o|
       |    o    |
       |o       o|
       \[---------]

'Would you like to roll again
Type 'y' or 'n'
```

📊 Fairness Demonstration
A single roll cannot prove that a die is fair. However, when the simulator is run for a large number of independent rolls, the observed frequencies should tend toward approximately 1/6 (16.67%) for each face.
The repository's project report includes a statistical experiment using 10,000 simulated rolls, frequency and percentage charts, and an explanation of random variation and the law of large numbers.

📁 Project Structure
```text
.
├── Dice.py
├── dice\_frequency\_10000.png
├── dice\_percentage\_10000.png
├── Project\_Report.pdf
└── README.md
```

🧠 Concepts Demonstrated
Concept	Use in Project
Function	`roll()` contains the dice-rolling logic
Random numbers	Generates a value from 1–6
Conditional statements	Selects the correct die face
Input	Allows the user to continue or stop
Recursion	Calls `roll()` again when the user chooses `y`
ASCII art	Represents each die face in the terminal

⚠️ Limitations
This is an introductory simulator. The current implementation:
Does not keep a running statistical count during normal interactive use.
Uses recursion to repeat rolls, so an extremely large number of consecutive rolls is not ideal.
Accepts only the expected `y`/`n` inputs.
Uses `from random import \*`; explicitly importing `randint` would be clearer in a larger project.

🔮 Possible Future Improvements
Add a loop instead of recursive calls.
Track and display the number of times each face occurs.
Allow the user to choose the number of rolls.
Calculate percentages automatically.
Add graphical charts directly from the program.
Add input validation.
Add automated tests.
Allow different numbers of sides, such as 4, 8, 10, 12, or 20.

👨‍💻 Project Type
Language: Python  
Project: Dice Rolling Simulator  
Level: Beginner Python Project

📄 Project Report
See `Project\_Report.pdf` for the complete project report, including:
Introduction
Objectives
Methodology
Program working
Code explanation
Fairness and probability
10,000-roll statistical experiment
Frequency and percentage analysis
Visual charts
Results and observations
Limitations
Future improvements
Conclusion
