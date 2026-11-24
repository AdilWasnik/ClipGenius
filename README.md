# ClipGenius

> **AI Viral Clip Engine** · Turn long videos into captioned 9:16 vertical clips in minutes. Fast, private, 100% local processing. No subscriptions.

---

### What ClipGenius does

- **Paste a link, get clips:** Paste YouTube, Twitch or Kick replays. ClipGenius downloads the video, analyzes audio energy, chat activity, and transcripts using local AI, finds high-impact moments, and renders captioned 9:16 vertical clips.
- **Dynamic Captions:** Burn in subtitle presets with active-word highlights (Karaoke, Impact, Hormozi, MrBeast, TikTok, Pill, Clean, Cinematic, etc.).
- **Smart Framing:** Multi-box framing with automatic facecam detection and presets for top, bottom, or corner webcams.
- **100% Local AI & Private:** Runs entirely on your hardware. Transcriptions run locally via Whisper; no videos or clips are sent to third-party servers.
- **Direct Export & Pro Editing:** Download standalone MP4s, SRT subtitles, or export multi-track timelines for Premiere Pro and DaVinci Resolve.
- **Phone Remote (LAN):** Control live clipping and preview clips from any phone on the same Wi-Fi network.

---

### Quick Start

#### macOS / Linux
```bash
./run.sh
```
Or start manually:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open **http://127.0.0.1:8770** in your browser.

#### Windows
Run PowerShell or double-click `run.ps1`:
```powershell
.\run.ps1
```

---

### Key Features

1. **Clip Engine:**
   - One-click batch generation (`⚡ Make clips`)
   - Manual moment selector and timeline editor
   - Subtitle generator with Hinglish, Hindi, English, and 40+ languages
   - Custom branding, outro cards, watermark overlay, background blur, and audio beds

2. **Live Clipping:**
   - Record and clip live streams in real time from YouTube Live or Twitch
   - Real-time chat spike detection and instant 30-second backdated clipping

3. **Creator Watcher:**
   - Automatically monitors favorite streamers and clips high-energy moments when they go live

4. **Multi-Track Export:**
   - Export XML timeline sequences for DaVinci Resolve and Adobe Premiere Pro with separate gameplay, facecam, and audio stems

---

### Configuration & Environment Variables

| Variable | Default | Description |
|---|---|---|
| `CLIPGENIUS_PORT` | `8770` | Port for the local web server |
| `CLIPGENIUS_DATA_DIR` | `./data` | Custom folder for downloaded sources, clips, and models |
| `CLIPGENIUS_LAN` | `0` | Set `1` to enable phone remote access over local Wi-Fi |
| `CLIPGENIUS_ENCODER` | `auto` | Force hardware encoder: `nvenc`, `videotoolbox`, `qsv`, `amf`, `x264` |
| `CLIPGENIUS_CPU` | `0` | Set `1` to force CPU inference for Whisper transcription |

*(Legacy `NEONCLIPPING_*` environment variables are also supported for backward compatibility)*

---

### License
AGPL-3.0. See [LICENSE](LICENSE).
