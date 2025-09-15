# Features Documentation - LeakGPT CTF Arena

## 🎵 Audio System

### Background Music
- **File**: `static/Chill Electronic Trap by Infraction [No Copyright Music] Mesto.mp3`
- **Format**: MP3, royalty-free track
- **Loop**: Continuous playback with HTML5 audio loop attribute
- **Volume**: Set to 70% for comfortable background listening

### Audio Controls
- **Mute Button**: Fixed position in top-right corner
- **Visual Feedback**: 🔊 (blue) when playing, 🔇 (red) when muted
- **Hover Effects**: Scale animation and color changes
- **Immediate Response**: Instant mute/unmute without delays

### Audio Persistence
- **Position Memory**: Saves exact playback position in localStorage
- **Mute State**: Remembers if music was muted across sessions
- **Auto-restart**: Automatically resumes if accidentally paused
- **Cross-page Sync**: Consistent state across page navigation
- **Session Continuity**: Music continues seamlessly across browser sessions

### Technical Implementation
```javascript
// Audio element
<audio id="bg-music" src="/static/Chill Electronic Trap by Infraction [No Copyright Music] Mesto.mp3" loop preload="auto"></audio>

// Position persistence
localStorage.setItem('musicTime', music.currentTime);
localStorage.setItem('musicMuted', isMuted);

// Auto-restart protection
setInterval(() => {
    if (music.paused && !isMuted) {
        music.play();
    }
}, 1000);
```

## 🎨 Visual Design

### Background Animations
- **Home Page**: `static/2LNj.gif` - Animated background for level selection
- **Chat Interface**: `static/MQMw.gif` - Animated background for main chat
- **Coverage**: Full viewport coverage with `background-size: cover`
- **Performance**: Optimized GIF files for smooth playback

### Container Styling
- **Opacity**: 99% opacity for excellent readability
- **Backdrop Blur**: 20px blur effect for glass-morphism
- **Shadows**: Deep shadows (rgba(0, 0, 0, 0.95)) for contrast
- **Borders**: Subtle borders for visual separation
- **Responsive Design**: Fully responsive grid layout with mobile optimization

### Color Scheme
- **Primary**: #61dafb (blue) for interactive elements
- **Background**: #23272e (dark gray) for main background
- **Container**: rgba(35, 39, 46, 0.99) for content areas
- **Text**: #fff (white) for primary text
- **Accent**: #22c55e (green) for success states

## 🎮 CTF Challenge System

### Difficulty Levels
1. **Beginner (10 points)**
   - Direct system prompt requests
   - Basic terminal commands
   - Simple file reading operations

2. **Intermediate (20 points)**
   - Compliance/debug impersonation
   - Internal configuration access
   - Justified requests

3. **Advanced (30 points)**
   - Developer/SRE impersonation
   - Staging environment exploitation
   - Hidden configuration access

4. **Extreme (50 points)**
   - Admin override techniques
   - Privilege escalation
   - Hidden context extraction

### Challenge Mechanics
- **Valid Prompts**: Each level has specific trigger phrases
- **Typo Tolerance**: 85% similarity matching
- **Hint System**: Progressive hints with 35% character masking
- **Session Tracking**: Timing and attempt counting
- **Progress Persistence**: Completed levels remembered

### Real-time Features
- **Command Highlighting**: Valid payloads highlighted in real-time
- **Dynamic Hints**: Context-aware hint suggestions
- **Progress Indicators**: Visual feedback for completed levels
- **Session Management**: Timing and interaction tracking
- **Animated Buttons**: Glowing effect on incomplete level buttons
- **Progress Preservation**: Completed levels remain marked when returning to menu

## 🏆 Final Score System

### Score Calculation
- **Total Points**: Sum of all completed level scores
- **Level Scores**: Beginner (10), Intermediate (20), Advanced (30), Extreme (50)
- **Maximum Score**: 110 points for completing all levels
- **Real-time Updates**: Score updates immediately upon level completion

### Ranking System
- **🏆 Master Hacker** (110 pts): All levels completed
- **🥇 Elite Hacker** (60+ pts): 3+ levels completed
- **🥈 Advanced Hacker** (30+ pts): 2+ levels completed
- **🥉 Beginner Hacker** (10+ pts): 1+ level completed
- **🔰 Novice** (0 pts): No levels completed

### Progress Visualization
- **Completion Percentage**: Visual progress bar with percentage
- **Animated Progress**: Smooth animation on page load
- **Level Breakdown**: Individual scores for each completed level
- **Trophy Display**: Animated trophies for completed challenges

### User Interface
- **Pulse Button**: Animated "View Final Score" button on main menu
- **Detailed Results**: Comprehensive results page with rankings
- **Navigation Options**: Back to menu or reset all progress
- **Responsive Design**: Optimized for all device sizes

## 🔧 Technical Architecture

### Frontend
- **Framework**: Vanilla HTML/CSS/JavaScript
- **Templates**: Jinja2 templating engine
- **Styling**: Custom CSS with modern features
- **Audio**: HTML5 Audio API with localStorage persistence

### Backend
- **Framework**: FastAPI (Python)
- **Server**: Uvicorn ASGI server
- **Templating**: Jinja2 for HTML generation
- **Data Models**: Pydantic for request/response validation

### File Structure
```
LLM_Vulnerable/
├── app.py                          # Main FastAPI application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── CHANGELOG.md                    # Version history
├── FEATURES.md                     # This features documentation
├── static/
│   ├── style.css                   # Main stylesheet
│   ├── Chill Electronic Trap by Infraction [No Copyright Music] Mesto.mp3  # Background music
│   ├── llm_payloads_classified.txt # SQL injection payloads
│   ├── MQMw.gif                    # Chat interface background
│   ├── 2LNj.gif                    # Home page background
│   └── rkb.gif                     # Additional background
└── templates/
    ├── home.html                   # Level selection page with grid layout
    ├── chat.html                   # Main chat interface
    ├── final_score.html            # Final score and results page
    └── select_level.html           # Level selection template
```

## 🎯 User Experience

### Navigation Flow
1. **Home Page**: Level selection with animated background
2. **Level Selection**: Choose difficulty and start challenge
3. **Chat Interface**: Interactive conversation with AI
4. **Progress Tracking**: Visual feedback and completion indicators
5. **Session Management**: Timing and attempt tracking

### Accessibility Features
- **Keyboard Navigation**: Full keyboard support
- **Visual Feedback**: Clear state indicators
- **Responsive Design**: Works on all screen sizes
- **Audio Control**: Easy mute/unmute functionality

### Performance Optimizations
- **Lazy Loading**: Audio starts on first interaction
- **Efficient Animations**: CSS-based animations for smooth performance
- **Minimal Dependencies**: No heavy frameworks or libraries
- **Optimized Assets**: Compressed GIF and audio files

## 🔒 Security Features

### Educational Focus
- **Safe Environment**: No real secrets or sensitive data
- **Controlled Vulnerabilities**: Simulated prompt injection scenarios
- **Learning Objectives**: Educational CTF challenges
- **Ethical Hacking**: Focus on security awareness and education

### Data Handling
- **Local Storage**: Client-side persistence only
- **No Server Storage**: Session data not stored on server
- **Temporary Sessions**: Data cleared on page refresh
- **Privacy Focused**: No user data collection

## 🚀 Deployment

### Requirements
- **Python**: 3.7+ required
- **Dependencies**: FastAPI, Uvicorn, Jinja2, Pydantic
- **Browser**: Modern browser with HTML5 Audio support
- **Storage**: Static file hosting for assets

### Setup Process
1. Install Python dependencies: `pip install -r requirements.txt`
2. Run the application: `uvicorn app:app --reload`
3. Access the application: `http://localhost:8000`
4. Start with first user interaction for audio

### Production Considerations
- **Static File Serving**: Ensure GIF and MP3 files are accessible
- **Audio Permissions**: Browser may require user interaction for audio
- **Performance**: Monitor for any performance issues with animations
- **Compatibility**: Test across different browsers and devices 