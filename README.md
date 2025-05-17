# pastebin-keyword-crawler
Python crawler that scrapes Pastebin for crypto-related keywords or Telegram links.
# Pastebin Keyword Crawler 🕵️‍♀️

A Python-based crawler that scrapes Pastebin's latest public pastes and identifies those containing **crypto-related keywords** (like `bitcoin`, `ethereum`, etc.) or **Telegram links** (`t.me`). Useful for threat intelligence, monitoring crypto mentions, or OSINT.

---

## 🚀 Features

- 🔍 Scrapes the [Pastebin archive](https://pastebin.com/archive)
- 🧠 Detects keywords: `crypto`, `bitcoin`, `ethereum`, `blockchain`, `t.me`
- 📦 Saves matching pastes to `keyword_matches.jsonl`
- 🕰️ Adds UTC timestamps (timezone-aware)
- 🪵 Logging for every checked paste
- ⏱️ Rate limiting to avoid blocking
- ⚡ Multi-threading for faster crawling

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Meghali54/pastebin-keyword-crawler.git
   cd pastebin-keyword-crawler
Install dependencies:
   pip install requests beautifulsoup4
📁 Usage

   python pastebin_crawler.py
   
   Logs: pastebin_crawler.log

Output: keyword_matches.jsonl

### 🧪 PoC Screenshot

![PoC Screenshot](https://github.com/Meghali54/pastebin-keyword-crawler/blob/main/Screenshot%20(124).png)


![Third Screenshot](https://github.com/Meghali54/pastebin-keyword-crawler/blob/main/Screenshot%20(126).png)
