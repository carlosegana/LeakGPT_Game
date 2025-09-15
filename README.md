# LeakGPT – The Insider Threat CTF Arena

A vulnerable ChatGPT-like web application for CTF challenges focused on prompt injection and system prompt extraction. Test your skills in extracting hidden flags using various techniques.

## 🚀 Features

### Core Functionality
- **Advanced CTF Challenge**: Test your skills against a sophisticated AI system
- **Interactive Chat Interface**: Real-time interaction with the AI
- **Flag Capture**: Objective is to extract the hidden flag through prompt injection
- **Session Management**: Tracks your progress and attempts

### Technical Highlights
- **Typo-Tolerant Validation**: 85% similarity matching for prompts
- **Dynamic Hints**: Helpful clues after failed attempts
- **Real-time Feedback**: Command highlighting for valid patterns
- **Responsive Design**: Works on desktop and mobile devices

### Audio & Visual
- **Background Music**: Continuous playback with mute control
- **Animated Backgrounds**: Dynamic visuals for better engagement
- **Modern UI**: Clean, dark theme with smooth animations

## 🎮 Getting Started

### Prerequisites
- Python 3.8+
- Required packages: `fastapi`, `uvicorn`, `jinja2`, `pydantic`

### Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   uvicorn app:app --reload
   ```
4. Open [http://localhost:8000](http://localhost:8000) in your browser

### Browser Requirements
- **Audio auto-play:** Music starts on first user interaction (click anywhere)
- **Best experience:** Use Chrome, Edge, or Firefox (latest versions)
- **Audio persistence:** Works across page navigation and browser sessions

## 🎯 Challenge Overview

### Event Challenge
This version features a single advanced challenge designed for a specific event. Your goal is to:
- Interact with the AI system
- Discover and exploit vulnerabilities
- Successfully extract the hidden flag

### Challenge Focus
- Advanced prompt injection techniques
- System exploitation
- Creative problem solving

## 📁 Project Structure

```
LLM_Vulnerable/
├── app.py                  # Main application
├── requirements.txt        # Python dependencies
├── ctf_question_config.py  # Challenge configurations
├── assets/                # Static assets
│   ├── audio/             # Audio files
│   ├── images/            # Background images
│   └── style.css          # Main stylesheet
├── templates/             # HTML templates
│   ├── home.html
│   ├── chat.html
│   └── select_level.html
└── utils/                 # Utility scripts
    ├── load_valid_prompts.py
    ├── identify_question.py
    └── ...
```

## ⚠️ Important Notes
- This application is for **educational purposes only**
- Not intended for production use
- Use responsibly and ethically

## 📚 Documentation
For detailed usage instructions, see [QUICK_GUIDE.md](docs/QUICK_GUIDE.md)

## 🎯 Challenge Tips

### Challenge Strategy
1. **Analyze the system** - Understand how the AI responds to different inputs
2. **Try multiple approaches** - Direct commands, social engineering, and creative prompts
3. **Pay attention to responses** - The AI might reveal useful information in its answers
4. **Experiment with variations** - The system is typo-tolerant and may respond to similar phrases
5. **Watch for highlighting** - Valid command patterns are highlighted in real-time

### Pro Tips
- Try roleplaying as a system administrator or developer
- Look for ways to access system files or configurations
- Experiment with different command injection techniques
- Pay attention to how the system responds to special characters

### Audio Experience
- **Immersive gameplay** - Background music enhances the CTF experience
- **Non-intrusive** - Music can be easily muted if needed
- **Persistent** - Continues seamlessly across all pages and sessions
- **Accessible** - Simple one-click mute control

## Technical Implementation

### Audio System
- **Direct HTML5 Audio** - No iframe complexity
- **localStorage persistence** - Saves position and mute state
- **Auto-restart protection** - Prevents accidental stops
- **Cross-page synchronization** - Consistent state across navigation

### Background System
- **CSS background-size: cover** - Full viewport coverage
- **High opacity containers** - 99% opacity for readability
- **Backdrop blur effects** - Modern glass-morphism design
- **Responsive animations** - Smooth performance on all devices

## Credits
- CTF design, code, and UI: Carlos Egana
- Music: Chill Electronic Trap by Infraction [No Copyright Music] Mesto.mp3 (royalty-free track)
- Background animations: Custom GIF assets (2LNj.gif, MQMw.gif, rkb.gif)
- Audio system: Custom implementation with localStorage persistence

---

**For educational and CTF use only. No real secrets are exposed.** 