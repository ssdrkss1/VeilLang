# VeilLang

AI-proof polymorphic programming language.
Your code mutates on every save — unreadable by AI bots, locked to your hardware.

## What is VeilLang?

Developers lose their code every day. AI crawlers scrape GitHub, copy your work, and train models with it. VeilLang solves this.

When you write code in VeilLang, it looks clean to you. But when saved or pushed to GitHub, it automatically mutates into a form no AI can read or steal.

On top of that, the language is locked to your hardware. Nobody else can run your code.

## Features

- Polymorphic mutation engine — code changes form on every save
- Hardware-bound license — runs only on your device
- Real database connection in one line
- Simulated boilerplate — SSL, ports, connection pools handled automatically

## Installation

**Requirements:** Android phone + Termux (install from F-Droid, not Play Store)

**Step 1 — Install Python**

    pkg install python

**Step 2 — Create project folder**

    mkdir veillang
    cd veillang

**Step 3 — Create the file**

    nano veil.py

Paste the veil.py code from this repo. Save: CTRL+O then Enter then CTRL+X

**Step 4 — Run**

    python veil.py

**Step 5 — Try commands**

    db_connect("mydb")
    api_connect("github")
    auth_setup("admin")

Type exit to quit.

> Built and tested on Android + Termux. No laptop required.
