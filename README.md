# Song Text Manipulation

## Overview
The **Song Text Manipulation** project is a Python-based program that processes song lyrics to perform tasks like finding the longest word and reversing the word order in each line. It demonstrates basic text processing techniques and file handling in Python.

## Features
- **Find Longest Word:** Reads a text file containing song lyrics and identifies the longest word.
- **Reverse Song Lines:** Reverses the word order in each line of the lyrics and writes the output to a new file.

## Installation
To run this project, ensure you have **Python 3.x** installed on your system.

### Steps:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/song-text-manipulation.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd song-text-manipulation
   ```
3. **Ensure the input file is available:**
   Place `song.txt` in the project directory.

## Usage
1. **Run the script:**
   ```bash
   python SongExercise.py
   ```
2. The script performs the following actions:
   - Prints the longest word in the song (`song.txt`).
   - Reverses the word order in each line of the song and writes the result to `song2.txt`.

## Input File Format
The input file (`song.txt`) should be a plain text file with song lyrics. Example:
```
If I stay with you if I'm choosing wrong
I don't care at all
If I'm losing now but I'm winning late
That's all I want
I don't care at all
Lost my time my life is going on
```

## Output Example
**Longest Word:**
```
choosing
```

**Reversed Lines (saved in `song2.txt`):**
```
wrong choosing I'm if you with stay I If
all at care don't I
late winning I'm but now losing I'm If
want I all That's
all at care don't I
on going is life my time my Lost
```

## License
This project is licensed under the **MIT License**.

## Contributions
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-new-feature`).
3. Commit and push your changes.
4. Open a pull request.

## Contact
For any questions or support, please open an issue on GitHub.

