# 🧠 Human-Like Color-Triggered Bot in Python

This project is a Python-based GUI automation bot designed to simulate **human-like interaction** with screen elements based on **color detection**. The bot monitors specific screen pixels and performs different mouse actions accordingly.

---

> ⚠️ **Disclaimer**\
> This project was developed **strictly for educational purposes**.\
> It was **never tested or deployed on any live online gambling platform**, and was only used in **simulated environments** to explore automation and detection evasion concepts.

> 🗓️ The project was originally built earlier and is now being published on GitHub for documentation and learning reference.

---

## 🎯 Purpose

This project was created to:

- Explore how screen pixel color detection can drive decision-making in bots
- Implement mouse movements and clicks that mimic human behavior
- Understand timing randomization and GUI automation with Python
- Practice building an event-driven loop using keyboard inputs

---

## 🛠 Technologies Used

- Python 3.x
- [PyAutoGUI](https://pypi.org/project/pyautogui/) – for mouse and screen interaction
- `win32api` & `win32con` – for low-level mouse control
- `keyboard` – for key-based bot termination
- `numpy`, `time`, `random` – for timing and randomness

---

## ⚙️ How It Works

- The bot **monitors specific screen coordinates** for color changes using `pyautogui.pixel()` and `pyautogui.pixelMatchesColor()`.
- Depending on detected colors, it **performs different mouse actions** (clicks, drags).
- All movements and delays are randomized to **mimic human behavior**.
- Pressing the `Q` key at any time will **terminate the program safely**.

---

## 📁 File Structure

```
/color-bot/
│
├── main.py         # Main bot logic
└── README.md       # This file
```

---

## 📸 Example Behavior

- If a specific pixel turns orange `(242, 154, 18)` → triggers a decision based on a secondary pixel color:
  - Yellow `(194, 166, 22)` → calls `sari()` or color switch logic
  - Blue `(31, 77, 212)` → calls `mavi()` or color switch logic
  - Green `(19, 124, 55)` → may trigger reset or repeat action
- Functions like `sariya()` or `maviye()` simulate **drag actions** between screen coordinates.

---

## 📌 Sample Code Snippet

```python
if pyautogui.pixelMatchesColor(910, 451, (242, 154, 18), tolerance=10):
    if pyautogui.pixel(383, 783) == (194, 166, 22):
        sari()
    elif pyautogui.pixel(383, 783) == (31, 77, 212):
        mavi()
```

---

## 🧪 Notes

- The pixel positions `(910, 451)`, `(383, 783)`, etc., are hardcoded and should be adjusted based on your screen resolution and environment.
- The project is **not production-grade** and was built for **exploratory purposes**.
- You must run this script on a Windows machine with the correct packages installed.

---

## ❌ Warning

Any attempt to use this code on third-party platforms (e.g., gambling, trading, gaming) **may violate terms of service** and is **strongly discouraged**. This code is provided **as-is for research and educational use only**.

---

## ✍️ Author

**Furkan Canbolat**\
Computer Engineering Student\
Bandırma Onyedi Eylül University\
[GitHub Profile](https://github.com/ElbruzMafe)
[Linkedin Profile]https://www.linkedin.com/in/elbruz-mâfe-canbolat-77665b335/

