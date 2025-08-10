# 🔐 Simple Password Generator

This Python script transforms a basic word into a stronger, more secure password by replacing common characters with symbols and appending a suffix. It's a beginner-friendly tool that demonstrates basic string manipulation and user input handling.

## 💡 How It Works

The function `password_maker(word)`:
- Replaces letters with symbols:
  - `a → @`
  - `e → 3`
  - `i → !`
  - `o → 0`
  - `s → $`
- Capitalizes the first letter
- Adds a fixed suffix: `195!`

### Example
**Input:** `password` 

**Output:** `P@$$w0rd195!`

![Output](https://github.com/user-attachments/assets/c4014845-bfa8-4dc5-80a1-d3d435e113c9)


## 🛠 Requirements
- Python 3.x (no external libraries needed)

## 🚀 How to Run

```bash
python password_generator.py
