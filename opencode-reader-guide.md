# OpenCode Reader — Setup Guide

A quick reference for getting NaturalReader to read your OpenCode AI responses in the browser.

---

## What You Need

- **opencode** installed on Windows (native, not WSL)
- **NaturalReader** Chrome extension (logged into your paid account)
- **Node.js** installed (for `npx serve`)
- The `opencode-reader.html` file (keep it somewhere easy to find)

---

## Every Time You Want to Use It

### Step 1 — Start OpenCode normally

Open your terminal (PowerShell or Windows Terminal) and run opencode as you usually do:

```powershell
opencode
```

### Step 2 — Serve the HTML file

Open a **second** PowerShell window, navigate to the folder where `opencode-reader.html` is saved, and run:

```powershell
npx serve .
```

You'll see output like:
```
Serving!
- Local: http://localhost:3000
```

### Step 3 — Open in Chrome

Go to:
```
http://localhost:3000/opencode-reader.html
```

### Step 4 — Connect to OpenCode

- The server URL field will default to `http://127.0.0.1:4096`
- Click **Connect**
- Your sessions will appear in the left sidebar

> **If it doesn't connect:** run `curl http://127.0.0.1:4096/global/health` in PowerShell.
> If you get `{"healthy":true}` — you're good. If not, opencode may not be running yet.

### Step 5 — Start NaturalReader

- Click the **NaturalReader N icon** in your Chrome toolbar
- Click **Play** — it will read the AI responses on the page using your premium voices

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| "Could not connect: Failed to fetch" | Open the HTML via `npx serve`, not by double-clicking the file. Chrome blocks `file://` requests to localhost. |
| Port 4096 not responding | Make sure `opencode` is running in another terminal window first |
| Sessions not showing | Make sure you're running opencode from your project folder, not a different directory |
| Port 3000 already in use | Run `npx serve . -l 3001` and open `http://localhost:3001` instead |
| NaturalReader not reading | Click inside the page first, then hit Play in the NaturalReader toolbar |

---

## How It Works (Quick Summary)

OpenCode runs a local HTTP API server on port `4096` when active. The `opencode-reader.html` file connects to that API, fetches your sessions and messages, and displays them as a clean chat interface in Chrome. NaturalReader's Chrome extension can then read any text on the page — including AI responses as they appear.

Opening the HTML file via `npx serve` (instead of directly) is required because Chrome's security policy blocks web requests to localhost from `file://` URLs.

---

## One-Line Quick Start (after first setup)

Once you've done this before, your daily workflow is just three commands across two terminals:

**Terminal 1:**
```powershell
opencode
```

**Terminal 2 (from the folder with the HTML file):**
```powershell
npx serve .
```

Then open `http://localhost:3000/opencode-reader.html` in Chrome and connect.

