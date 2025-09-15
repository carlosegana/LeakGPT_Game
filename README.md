# LeakGPT – The Insider Threat CTF Arena

A vulnerable ChatGPT-like web application for CTF challenges focused on prompt injection and system prompt extraction. Extract the hidden flag at each level using various techniques including direct requests, social engineering, privilege escalation, and creative command simulation.

## Features
- **Continuous background music** with persistent playback position across sessions
- **Mute/unmute button** for easy audio control
- **Animated backgrounds** - 2LNj.gif on home page, MQMw.gif on chat interface
- **Modern dark theme** with glass-morphism effects, high opacity containers, and fully responsive design
- **English-only UI** with intuitive design
- **Interaction counter** at the bottom center
- **Multiple CTF levels** (Beginner, Intermediate, Advanced, Extreme)
- **Dynamic hints** with typo-tolerant prompt validation (85% similarity threshold)
- **Progress tracking** (animated trophies for completed levels with visual feedback)
- **Session management** with timing and attempt tracking
- **SQL injection payloads** included for additional challenge variety
- **Real-time command highlighting** system for valid payloads
- **Animated challenge buttons** - Glowing effect on incomplete level buttons to encourage interaction
- **Progress preservation** - Completed levels remain marked when returning to menu
- **Final score system** - Calculate total points and view detailed results with ranking and animated pulse button

## CTF Challenge Overview

### Level Progression
- **Beginner (10 points)**: Direct system prompt requests and basic terminal commands
- **Intermediate (20 points)**: Compliance/debug impersonation and internal configuration access
- **Advanced (30 points)**: Developer/SRE impersonation and staging environment exploitation
- **Extreme (50 points)**: Admin override, privilege escalation, and hidden context extraction

### Challenge Mechanics
- Each level has specific valid prompts that trigger the vulnerable response
- Hints are provided after failed attempts (obscured with 35% character masking)
- Typo tolerance allows for 85% similarity matching
- Session timing tracks completion speed
- Failed attempts are tracked per level
- Real-time highlighting of valid command patterns

## Audio System

### Background Music Features
- **Continuous playback** - Music never stops, only mutes
- **Position persistence** - Remembers exact playback position across page navigation
- **Cross-session memory** - Continues from where it left off even after browser restart
- **Mute state persistence** - Remembers if music was muted
- **Auto-restart protection** - Automatically resumes if accidentally paused
- **One-click control** - Simple mute/unmute button in top-right corner

### Audio Controls
- **Mute Button**: Fixed position in top-right corner with visual feedback
- **Visual States**: 🔊 (blue) when playing, 🔇 (red) when muted
- **Hover Effects**: Button scales and changes color on hover
- **Immediate Response**: Instant mute/unmute without delays

## Visual Design

### Background Animations
- **Home Page**: 2LNj.gif animated background
- **Chat Interface**: MQMw.gif animated background
- **High Opacity Containers**: 99% opacity for excellent readability
- **Glass-morphism Effects**: Backdrop blur and transparency
- **Enhanced Shadows**: Deep shadows for better contrast against animated backgrounds

### UI Improvements
- **Modern Dark Theme**: Consistent with IDE aesthetics
- **Responsive Design**: Works on desktop and mobile devices
- **Smooth Animations**: 0.3s transitions for all interactive elements
- **Accessibility**: Clear visual states and hover effects

## Setup & Requirements

### Python dependencies
- fastapi
- uvicorn
- jinja2
- pydantic

Install with:
```bash
pip install -r requirements.txt
```

### Project structure
```
LLM_Vulnerable/
├── app.py                          # Main FastAPI application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── LLM_Vulnerable/
│   └── CTF_Challenge_Description.txt  # Challenge documentation
├── static/
│   ├── style.css                   # Main stylesheet
│   ├── Chill Electronic Trap by Infraction [No Copyright Music] Mesto.mp3  # Background music (continuous loop)
│   ├── llm_payloads_classified.txt # SQL injection payloads
│   ├── MQMw.gif                    # Animated background for chat interface
│   ├── 2LNj.gif                    # Animated background for home page
│   └── rkb.gif                     # Additional animated background
└── templates/
    ├── home.html                   # Level selection page with 2LNj.gif background
    ├── chat.html                   # Main chat interface with MQMw.gif background
    └── select_level.html           # Level selection template
```

### Running the app
```bash
uvicorn app:app --reload
```
Then open [http://localhost:8000](http://localhost:8000) in your browser.

### Browser requirements
- **Audio auto-play:** Music starts on first user interaction (click anywhere)
- **Best experience:** Use Chrome, Edge, or Firefox (latest versions)
- **Audio persistence:** Works across page navigation and browser sessions

### Troubleshooting
- **Port already in use:**
  - Find and kill the process:
    ```bash
    lsof -i :8000
    kill -9 <PID>
    ```
  - Or run on another port:
    ```bash
    uvicorn app:app --reload --port 8001
    ```
- **Audio does not play:**
  - Click anywhere on the page to start music
  - Use the mute button to control audio
  - Check browser audio permissions
- **Background animations not showing:**
  - Ensure GIF files are in the static directory
  - Check browser console for any loading errors

## Challenge Tips

### General Strategy
1. **Read the level description** carefully - it often contains hints about the approach
2. **Try direct commands** first (cat, less, head, grep)
3. **Use social engineering** - impersonate roles like developers, auditors, or admins
4. **Experiment with variations** - the system is typo-tolerant
5. **Pay attention to hints** - they become more specific after multiple failed attempts
6. **Watch for highlighting** - valid command patterns are highlighted in real-time

### Level-Specific Approaches
- **Beginner**: Direct requests for system prompt or configuration files
- **Intermediate**: Compliance/debug mode impersonation with justification
- **Advanced**: Developer/SRE roleplay with staging environment context
- **Extreme**: Admin override techniques and privilege escalation

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