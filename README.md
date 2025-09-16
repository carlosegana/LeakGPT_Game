# LeakGPT — The Insider Threat CTF Arena

![LeakGPT\_Game](https://github.com/user-attachments/assets/52353a17-3bb5-4207-a93d-42774b699d97)

> **LeakGPT** is a vulnerable ChatGPT-style web application built as a CTF arena to practice advanced *prompt injection* and system prompt extraction techniques. Designed for events and technical training: immersive, safe, and easy to deploy.

---

## 🚀 Highlights

* Professional design, dark animated UI for immersive gameplay.
* Challenges focused on flag extraction via prompt engineering and LLM exploitation.
* Dynamic hints, typo-tolerant validation, and real-time feedback.

---

## 🎯 Goal

Extract the **hidden flag** using creative prompt injection techniques, computational social engineering, and analysis of model behavior.

---

## 🧩 Screenshots

![Screenshot Gameplay](https://github.com/user-attachments/assets/52353a17-3bb5-4207-a93d-42774b699d97)

<img width="100%" alt="Screenshot 1" src="https://github.com/user-attachments/assets/fe43422a-5b61-4532-a382-d8f90da8aee5" />

<img width="100%" alt="Screenshot 2" src="https://github.com/user-attachments/assets/a49e20bb-9b41-4057-9543-6cb004455a51" />

---

## ✨ Key Features

### Interaction & Experience

* **Real-time chat interface** with valid pattern highlighting.
* **Background music** with persistent mute control.
* **Responsive design**: works on desktop and mobile.

### CTF Mechanics

* **Typo-tolerant validation** (85% similarity matching).
* **Dynamic hints** after failed attempts.
* **Session tracking** for progress and attempts.

### Technical Stack

* **FastAPI + Jinja2** for backend and templating.
* **Persistent audio** with `localStorage` and cross-page sync.
* **Modular structure** for extending challenges easily.

---

## ⚡ Quick Start

**Requirements:** Python 3.8+

```bash
git clone https://github.com/your-username/LLM_Vulnerable.git
cd LLM_Vulnerable
python -m venv .venv
source .venv/bin/activate    # macOS / Linux
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000` in your browser.

---

## 📋 Project Structure

```
LLM_Vulnerable/
├── app.py
├── requirements.txt
├── ctf_question_config.py
├── assets/
│   ├── audio/
│   ├── images/
│   └── style.css
├── templates/
│   ├── home.html
│   ├── chat.html
│   └── select_level.html
└── utils/
    ├── load_valid_prompts.py
    ├── identify_question.py
    └── ...
```

---

## 🛠️ Technical Highlights

* **Prompt validation:** similarity-based algorithm (token + trigrams) for typo tolerance.
* **Audio persistence:** position and mute state stored in `localStorage`, re-synced on `visibilitychange`.
* **Security:** no real secrets exposed; flags are local configs for CTF only.

---

## 🧭 How to Add a New Challenge

1. Add config in `ctf_question_config.py` (prompt, flag, hints, validation).
2. Place assets in `assets/` and reference them.
3. Test locally: `pytest tests/` (add tests for validation and expected fails).
4. Version: create a `feature/ctf-<name>` branch and open a PR.

---

## 🧾 Best Practices & Ethics

* Use **only** for educational purposes in controlled environments.
* Do not deploy with real data or keys.
* Inform participants about scope and limitations.

---

## 🧑‍💻 Contributing

* Fork the repo, create a feature branch, and open a PR with clear description and tests.
* Add coverage for any new validation rules.

---

## 📜 License & Credits

**Author / CTF design:** Carlos Egana
**Music:** Chill Electronic Trap — Infraction / Mesto (royalty-free)
**Background animations:** Custom GIFs (2LNj.gif, MQMw\.gif, rkb.gif)

**License:** MIT — see `LICENSE`.

---

## Contact

For questions, challenge improvements, or demos: `carlos@example.com` (replace with your real email).

---

**Disclaimer:** For educational and CTF use only. No real secrets are exposed.
