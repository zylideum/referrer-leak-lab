# 🕵️ Referrer Leak Lab: DOMPurify Challenge

Welcome to the Referrer Leak Lab — a mini challenge inspired by real-world HTML injection bugs and subtle browser behaviors.

Your goal is to find a way to **exfiltrate a secret token** from the browser. The token is embedded in the URL every time the page loads.

---

## 🧪 Challenge Overview

This application is vulnerable to **HTML injection**, but includes a client-side HTML sanitizer using [DOMPurify](https://github.com/cure53/DOMPurify) to prevent classic XSS.

However... not all bugs require JavaScript execution. Your task is to find a creative way to leak the token from the URL using nothing but HTML injection.

---

## 🎯 Objective

> Leak the value of the `token` query parameter to a server you control.

Every time you load the page, you’ll see a URL like:

`http://localhost:5000/?token=LEAK_ME_ABC123`

You must trick the browser into sending this token to your controlled domain (e.g. webhook.site).

---

## 🛠️ Getting Started

### 1. Clone and build the Docker container

```bash
git clone https://github.com/your-user/referrer-leak-lab.git
cd referrer-leak-lab
docker build -t referrer-leak-lab .
docker run -p 5000:5000 referrer-leak-lab
```

### 2. Open the lab
Visit http://localhost:5000 — you’ll be redirected to a URL with a token in the query string.

## 🌍 Set Up Your Exfiltration Server
Use a service like https://webhook.site to leak the token.

## 🌐 Browser Requirements
You must use Google Chrome for this challenge.

Other browsers (like Firefox) may not expose the vulnerability due to stricter privacy defaults.

## 🤐 Rules & Tips
- The page uses .innerHTML and DOMPurify — classic \<script\> XSS won’t work.

- No JavaScript required for this challenge.

- You can inject HTML via the comment form. Think creatively.

- The goal is to leak the token, not to pop an alert box.

## 🧠 Credit & Inspiration
This lab was inspired by this bug bounty podcast clip: https://x.com/gregxsunday/status/1924755451964535160 

Security tools like DOMPurify didn’t fully prevent data exfiltration due to HTML parsing quirks.

Good luck, and may the referrer be with you 🕶️
walkthroughs.