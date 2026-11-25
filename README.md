# Job Hunter: Free AI Remote Job Search Bot (Python, Gemini, Gmail Drafts)

**Job Hunter** is a free, open-source **remote job search bot with a desktop GUI** for Linux. It searches 19 job sites and 150+ company career pages at once (plus Google, for LinkedIn and Indeed posts), filters by your keywords, job age, work type (remote, hybrid, on-site) and where the job is open (worldwide, your country, countries you pick, or with visa sponsorship), finds the **recruiter or company email**, and uses **Google Gemini (free tier)** to write a **tailored ATS-friendly CV (PDF), cover letter and application email** for each job, in any field: software, finance, sales, SEO, support, design, writing, HR and more. It then saves the email as a **Gmail draft**. It never sends anything on its own: you read each draft and press Send yourself.

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform: Linux](https://img.shields.io/badge/platform-Linux-FCC624.svg)](#requirements)
[![No pip packages](https://img.shields.io/badge/dependencies-none-brightgreen.svg)](#requirements)
[![Free Gemini API](https://img.shields.io/badge/AI-Gemini%20free%20tier-8E75B2.svg)](https://aistudio.google.com/app/apikey)

> **Watch the 1-minute demo:** https://www.youtube.com/watch?v=4s38kwQLMh4

Good for developers and freelancers looking for **remote jobs from Pakistan, India, Bangladesh, Africa or anywhere in the world**, and for anyone who wants to **automate job applications** without paying for an AI service.

> 🎥 Made by **Ahsan Mehmood** · GitHub: [Ahsan483](https://github.com/Ahsan483)

## Features

- **Searches 19 job sites and 150+ company career pages at once:** Remotive, RemoteOK, Arbeitnow, Himalayas, Jobicy, We Work Remotely, Working Nomads, Remote First Jobs, Real Work From Anywhere, 4 Day Week, Workew, Jobspresso, NoDesk, LaraJobs, VueJobs, Remote Python, Landing.jobs (Europe), Platsbanken (Sweden's public job service), the Hacker News "Who is hiring?" thread, and the career pages of 150+ companies on Greenhouse, Ashby, Lever and SmartRecruiters (Stripe, OpenAI, Anthropic, Cloudflare, Spotify, Canva, Wise, GitLab and more). These career pages are where sites like Wellfound and HiringCafe get most of their listings; Job Hunter reads them at the source.
- **Google search too:** Gemini searches Google for posts on LinkedIn, Indeed, Glassdoor and company sites. Only links Google really returned are kept. One Gemini request every 4 hours at most.
- **Any kind of remote job:** pick a job type (Finance / Accounting, Sales, SEO / Marketing, Customer support, Design, Writing, Data, HR, Virtual assistant, Project management, Software) or type your own keywords.
- **Smart, forgiving filter:** "fullstack", "full stack" and "Full-Stack" are the same; small typos are fine; a job that matches part of your keywords is shown as a **partial match** under the strong ones. Posts that don't say where they hire are kept and marked. When results are few, the window says what to loosen ("15 more are older than 10 days").
- **Finds the application email** in the post, or on the company's own careers page.
- **Tailored CV + cover letter (PDF)** for each job, built only from facts in your profile. The bot drops any line that adds a skill or number you don't have.
- **Gmail drafts** with the CV attached, ready for you to review and send. Gmail is optional: without it you get the CV, cover letter and email text as files.
- **Paste any job post** (LinkedIn, a company site) and get a tailored CV + cover letter for it.
- **Upload your CV** once (PDF, Word, text, or even a photo/scan) and Gemini turns it into your profile. Works without work experience too, for students and career changers.
- **Track your applications:** mark a job as applied, reopen the CV made for it, or copy its cover letter into an application form.
- **Tells you when an update is out**, with a getting-started checklist and a hint on every button.
- **Auto-run every 30 minutes** with cron.
- **Uses only free Gemini models** and switches to another model when one runs out of free quota.

## Quick start (Linux)

```
git clone https://github.com/Ahsan483/job-hunter.git
cd job-hunter
./run.sh
```

The first run sets everything up (a virtual environment in `.venv`, pywebview, and the window's page built with npm), then opens the window. Later runs just open it. Before the first run install the [requirements](#requirements) below: Python, Node.js, a GUI toolkit for the window, and Chrome or Chromium.

The window asks for your **Gemini API key** and, optionally, a **Gmail app password**. Press **How do I get…?** under each box for step-by-step help, then **Test & save**. Then press **Upload my CV**, then **Find jobs**.

Your keys, profile and CVs stay in the `job-hunter` folder (or in `JOBHUNTER_HOME`, see [Files](#files)).

## Requirements

- Linux with a desktop (X11 or Wayland)
- [Python 3.10+](https://www.python.org/downloads/) with `venv` (Debian/Ubuntu: `sudo apt install python3 python3-venv`)
- A GUI toolkit for the window. The easiest is GTK + WebKit:
  - Debian / Ubuntu: `sudo apt install python3-gi gir1.2-webkit2-4.1`
  - Fedora: `sudo dnf install python3-gobject webkit2gtk4.1`
  - Arch: `sudo pacman -S python-gobject webkit2gtk-4.1`
  - Or Qt, from pip: put `pywebview[qt]` in `requirements.txt` instead of `pywebview`
- Google Chrome or Chromium, used to make the PDF CVs (`sudo apt install chromium`). Set `JOBHUNTER_BROWSER` to a browser's path if yours is somewhere unusual. The Snap version of Chromium cannot write the PDFs: use the `.deb` of Chrome or Chromium instead.
- [Node.js 20+](https://nodejs.org) to build the window once
- `cron`, only for Auto-run (`sudo apt install cron`)
- `xdg-utils` (`xdg-open`) so the **Open** menu can open your CVs, files and folders
- A free Gemini API key
- A Gmail account, only if you want automatic drafts

The bot itself uses only Python's standard library. `./run.sh` installs pywebview. To do the same by hand:
```
python3 -m venv --system-site-packages .venv
.venv/bin/python -m pip install -r requirements.txt
cd ui
npm ci
npm run build
cd ..
```
(`--system-site-packages` lets the virtual environment see the distribution's GTK bindings.)

## Install

### 1. Download
```
git clone https://github.com/Ahsan483/job-hunter.git
cd job-hunter
```
Or click **Code → Download ZIP** on GitHub and unzip it.

### 2. Get a free Gemini API key
1. Go to https://aistudio.google.com/app/apikey and sign in with a Google account.
2. Click **Create API key** and copy it.

### 3. Set up Gmail drafts (optional)
Skip this if you only want CVs and cover letters.
1. Turn on 2-Step Verification: https://myaccount.google.com/security
2. Create an app password at https://myaccount.google.com/apppasswords (name it "Job Hunter") and copy the 16 letters.
3. Check that IMAP is on: Gmail → Settings → See all settings → Forwarding and POP/IMAP. It is on by default for most accounts.

### 4. Create `config.json`
The window asks for your keys the first time it opens and writes `config.json` for you. To do it by hand, copy `config.example.json` to `config.json` and fill in:

| Key | What to put |
|---|---|
| `gemini_api_key` | Your Gemini key from step 2 |
| `gmail_address` | The Gmail address that should hold the drafts |
| `gmail_app_password` | The 16-letter app password from step 3 |

`config.json` holds your passwords. It is in `.gitignore`, so it's never uploaded. Don't share it.

### 5. Create `profile.json` (your CV data)
Every CV, cover letter and email is built **only** from facts in `profile.json`. Pick one way to make it:

- **Easiest:** open the window (next step) and press **Upload my CV**. Gemini reads your CV (.pdf, .docx, .txt or .md) and writes `profile.json`. Then press **My profile** and check it.
- **By hand:** copy `profile.example.json` to `profile.json` and replace the sample person (Jane Doe) with your details. Keep the same keys: `name`, `default_title`, `contact`, `location`, `years`, `default_summary`, `experience` (each with a unique `id` and a list of `bullets`), `projects`, `skills`, `education`.
- **Command line:** `python -I bot.py --import-cv my-cv.pdf`

### 6. Start it
Run:
```
./run.sh
```
Press **Find jobs** for a first test. It takes 1-3 minutes and uses no Gemini and no Gmail.

## Using the window

The window has three columns you can resize by dragging the lines between them: **your CV, AI model and filter** on the left, the **job list** with the **Activity** log under it in the middle, and the **job you picked** on the right. Hover over any button to see what it does. While no job is picked, the right column shows a **Getting started** checklist. Every result comes as a notification in the bottom-right corner, with a soft sound (turn sounds off with the speaker icon). The sun/moon icon switches between dark and light.

**Top bar**
- **Find jobs** (F5): searches every job site and lists the matches. Uses no Gemini and no Gmail.
- **Auto-draft best matches**: Gemini checks the fit of the top matches, writes a tailored CV and email for each, and saves Gmail drafts. Without Gmail it saves the CV, cover letter and email text as files instead.
- **Stop**: shows up while a run is going, including one started by Auto-run.
- **Update to vX.Y**: shows up when a newer version is out. It opens the project page; update with `git pull` and start Job Hunter again. Your keys, profile and CVs are kept.
- **Auto-run**: sets up and turns on or off the 30-minute schedule (see below).
- **Open**: your Gmail drafts, your CVs and cover letters, `tracker.csv`, `runs.log`, your profile and the data folder.
- **Help**: getting started, this guide, report a problem, check for updates, about.
- **Settings** (gear icon): fit score, draft limits, Gemini call limit and the years-of-experience filter, and your Gmail & Gemini keys.

**Left column**
- **Upload my CV** / **Replace CV**: rebuilds `profile.json` from your CV (.pdf, .docx, .txt, .md, or a .png/.jpg photo). The old one is kept as `profile.backup-*.json`. **Check or correct my profile** opens it in your default text editor.
- **Tailor to a job**: paste any job post to get a tailored CV + cover letter.
- **AI model**: pick a Gemini model, or leave it on Auto. Each model shows whether it works right now; the refresh icon asks Google again.
- **What to look for**: the filter (see Filters below). **Save & search** saves it (Auto-run uses it too) and searches.

**Job list**
- The tabs pick the list: ready to draft (has an email), apply on company site, all matches, done / applied / skipped, or everything (rejected jobs show why).
- **Search** (Ctrl+F) filters by any text. Click a column title to sort. The arrow keys move through the list.
- Click a job to read the full post, salary, type and tags, then:
  - **Draft email + CV**: for jobs that published an email address.
  - **CV + cover letter**: for jobs you apply to on the company site. The files go to `cvs/`.
  - **Job page** (Enter), **Email** (copy the address), **My CV for it** (open the CV and cover letter made for this job), **Cover letter** (copy its text for an application form).
  - **Applied**: you sent it. It moves to Done and is noted in `tracker.csv`.
  - **Skip**: the bot won't draft it.

**Activity** shows each site searched and how many jobs it gave, every match, and anything that needs your attention, in plain words. Saved files are links: click one to open it.

## Filters

Set these under **What to look for** (then press **Save & search**) or in `config.json`:

| Setting | Meaning | Example |
|---|---|---|
| Job type | Fills in keywords that suit a field and picks the matching We Work Remotely categories. Pick **Custom** to type your own (then every category is read) | `Finance / Accounting` |
| Keywords (`keywords`) | A job is kept if **any** of these is in it. In the title it is a **strong** match; part of it in the title, or the keyword only in the description, is a **partial** match | `React, Node.js` or `Accountant, Bookkeeper` |
| Keywords in title only (`keywords_in_title`) | The keyword must be in the job title, not just the description. Turn it on for words like *Sales* or *Finance* that appear in almost every job ad | on |
| Exclude in title (`exclude_keywords`) | Skip jobs with these words in the title | `Intern, PHP` |
| Max age (`max_job_age_days`) | Ignore older posts | `30` |
| Search Google too (`search_google`) | Gemini searches Google for LinkedIn, Indeed, Glassdoor and company-site posts (one request every 4 hours at most) | on |
| Work type (`work_modes`) | Kinds of work to keep: **Remote**, **Hybrid**, **On-site** (tick several). Each job is marked with its work type in the list | `Remote` |
| Open to (`open_to`) | **Worldwide + my country** (`me`): remote jobs that hire worldwide or name your country, office jobs in your country. **Countries I pick** (`countries`): the same for the countries in *Countries*. **Any country** (`anywhere`): no limit | Worldwide + my country |
| My country/region (`my_region_words`) | Where you live. Posts naming these count as open to you | `Pakistan, South Asia` |
| Countries (`target_countries`) | For *Countries I pick*: countries or regions you would work for or move to | `UAE, Saudi Arabia, Germany` |
| Visa / relocation abroad (`visa_sponsorship`) | Also keep hybrid and on-site jobs in other countries when the post offers visa sponsorship or relocation help | off |
| Skip jobs asking for (years) (`max_years_required`, in Settings) | Skip jobs asking for this many years or more (`0` = off) | `8` |
| `job_fields` (config.json) | We Work Remotely categories to read: `software`, `devops`, `design`, `sales & marketing`, `customer support`, `finance & management`, `product`, `other`, or `all`. Set by **Job type** | `["sales & marketing"]` |

The defaults look for .NET / C# jobs. Pick a **Job type** or type your own keywords for any other field. Your CV can be from any field too: **Upload my CV** keeps certifications, languages and software as skills, and the tailoring never adds a tool, certification or number your CV doesn't have.

**Settings** also has: `min_fit_score` (0-100 score Gemini gives a job before a draft is made, default 60), `max_drafts_per_run` (3), `max_drafts_per_day` (20) and `max_gemini_calls_per_run` (8, keeps you inside the free limits).

## Auto-run every 30 minutes

Press **Set up auto-run** in the window once. It adds one line to your crontab (marked `# Remote Job Hunter`) that runs the bot every 30 minutes while the computer is on, even with the window closed. After that, the same button turns it on and off: off comments the line out, and your other crontab lines are never touched. Each run searches, tailors up to `max_drafts_per_run` CVs, and saves the drafts. Nothing is ever sent. If the button says cron is not installed, install it (`sudo apt install cron`) and make sure the service runs (`systemctl enable --now cron`).

## Command line

```
python -I bot.py --dry-run          # search and filter only (no Gemini, no Gmail)
python -I bot.py                    # one full run, the same as Auto-run
python -I bot.py --import-cv cv.pdf # rebuild profile.json from your CV
python -I -m unittest discover -s tests   # run the tests (no network needed)
```

## Troubleshooting

| Problem | Fix |
|---|---|
| `./run.sh` says Python, venv or Node.js is missing | Install what it names (see [Requirements](#requirements)). |
| "Job Hunter needs a GUI toolkit" | Install GTK + WebKit or Qt, see [Requirements](#requirements). If you made `.venv` yourself, create it with `--system-site-packages` (`./run.sh` does). |
| The window is blank or white (often with NVIDIA, or on Wayland) | Start it with `WEBKIT_DISABLE_DMABUF_RENDERER=1 ./run.sh` (or `WEBKIT_DISABLE_COMPOSITING_MODE=1 ./run.sh`). |
| "Gmail or Gemini is not connected yet" | Press **Settings → Gmail & Gemini keys…** (or fill in `config.json`, install step 4). |
| "profile.json not found" | Press **Upload my CV**, or copy `profile.example.json` to `profile.json`. |
| "Another run is in progress" | A run was killed halfway. Wait 25 minutes or delete `bot.lock`. |
| "Could not make the PDF" / "Chrome or Chromium not found" | Install Chrome or Chromium (not the Snap version), or set `JOBHUNTER_BROWSER` to its path. The message also shows what the browser itself reported. |
| "Gmail is not connected" | Gmail is only needed for drafts. Use **CV + cover letter**, or connect Gmail in **Settings → Gmail & Gemini keys…** |
| "profile.json has a typo" | Press **My profile** and fix the line it names (usually a missing comma or quote), or **Upload my CV** again. |
| Gmail login fails | Use the 16-letter **app password**, not your normal password, and check that IMAP is on. |
| "every free model is out of quota" | Gemini's free limit is used up. The log says when it's back, usually within a day. |
| "model was not found" in `runs.log` | Set `gemini_model` to a current name from https://ai.google.dev/gemini-api/docs/models. |
| No jobs found | Read the line above the job list: it says how many more jobs a longer max age or any country would give. Add more keywords, raise the max age, or set **Open to** to *Any country*. For non-software jobs, pick a **Job type** so the right job categories are searched. Pick **Show: Everything** to see why each job was left out. |

## Files

| File | Purpose | Uploaded to GitHub? |
|---|---|---|
| `bot.py` | Job search, Gemini tailoring, Gmail drafts | yes |
| `webapp.py`, `backend.py`, `ui/` | The window: a React page (`ui/`) shown by pywebview; `backend.py` is everything its buttons do | yes |
| `cv.py` | Builds the CV / cover letter PDF | yes |
| `run.sh` | Sets up and starts the window | yes |
| `tests/` | Unit tests, run by GitHub Actions on every push | yes |
| `config.example.json`, `profile.example.json` | Templates to copy | yes |
| `config.json` | Your keys, password and settings | **no** |
| `profile.json` | Your CV data | **no** |
| `cvs/`, `tailor/`, `jobs.json`, `tracker.csv`, `runs.log` | Your generated files and history | **no** |

The files that are not uploaded live in the `job-hunter` folder next to the scripts. To keep them somewhere else (for example `~/.local/share/job-hunter`, a USB stick, or a test copy), set the environment variable `JOBHUNTER_HOME` to that folder; the window, Auto-run and the bot all follow it (for Auto-run, set it in the crontab line or in your login profile).

## Privacy

Your keys, CV, profile, jobs and CVs never leave your computer, except to the services you connect: the Gemini key goes only to Google and the Gmail app password only to Gmail.

Once a day Job Hunter sends an anonymous "in use" signal to `stats.codeprojectsofficial.com`: a random install number and the app version, nothing else. It only counts how many people use the app. Turn it off in **Settings > Count me as an active user** (or set `"usage_stats": false` in `config.json`). The counter's code is in [`stats/`](stats/).

## Job sources and credits

Job listings come from [Remotive](https://remotive.com), [Remote OK](https://remoteok.com), [Arbeitnow](https://www.arbeitnow.com), [Himalayas](https://himalayas.app), [Jobicy](https://jobicy.com), [We Work Remotely](https://weworkremotely.com), [Working Nomads](https://www.workingnomads.com), [Remote First Jobs](https://remotefirstjobs.com), [Real Work From Anywhere](https://www.realworkfromanywhere.com), [4 Day Week](https://4dayweek.io), [Workew](https://workew.com), [Jobspresso](https://jobspresso.co), [NoDesk](https://nodesk.co), [LaraJobs](https://larajobs.com), [VueJobs](https://vuejobs.com), [Remote Python](https://www.remotepython.com), [Landing.jobs](https://landing.jobs), [Platsbanken](https://arbetsformedlingen.se/platsbanken) through the [JobTech API](https://jobtechdev.se), [Hacker News](https://news.ycombinator.com), the public job APIs of company career pages on Greenhouse, Ashby, Lever and SmartRecruiters, and Google search through Gemini. Every job links back to its original post. Please apply through those links and support these sites.

Job Hunter does not scrape LinkedIn, Indeed, Glassdoor, Wellfound or Google directly: their terms and robots.txt forbid it and they block bots. It finds their posts through Gemini's Google Search instead. To stay polite, the bot only reads sites that allow it, pauses between requests to the same site, backs off when a site says it's busy, checks robots.txt before reading company career pages, and fetches Remotive at most every 6 hours, as its API terms ask.

## FAQ

**Is Job Hunter really free?**
Yes. The code is MIT-licensed. It uses the free tier of the Google Gemini API, and you use your own key. Gmail drafts are free too.

**Do I need Python?**
Yes, Python 3.10+. `./run.sh` sets up its own virtual environment, so nothing is installed system-wide except the [requirements](#requirements).

**Can it find remote jobs for Pakistan, India or other regions?**
Yes. Set **Open to** to *Worldwide + my country* and type your country or region in **My country/region** (for example `Pakistan, South Asia`). Remote jobs that name your region, or that are open worldwide, are kept.

**Can it find on-site or hybrid jobs, or jobs in other countries?**
Yes. Tick **On-site** and/or **Hybrid** under **Work type**. With *Worldwide + my country* you get office jobs in your own country; pick *Countries I pick* and type e.g. `UAE, Germany` for jobs there (remote jobs limited to those countries too). Tick **Visa / relocation abroad** to also keep office jobs anywhere whose post offers visa sponsorship or relocation. Most free job feeds list remote jobs; office jobs come from Arbeitnow, 4 Day Week, company career pages, Hacker News and the Google search.

**Does it apply to jobs automatically or send emails by itself?**
No. It only creates Gmail **drafts**. You read each one and press Send.

**Will it make up facts on my CV?**
Gemini is told to use only facts from your `profile.json`, and the bot drops reworded lines that add tools or numbers your profile does not contain. Always read the result before you send it.

**Which job sites does it search?**
Remotive, RemoteOK, Arbeitnow, Himalayas, Jobicy, We Work Remotely, Working Nomads, Remote First Jobs, Real Work From Anywhere, 4 Day Week, Workew, Jobspresso, NoDesk, LaraJobs, VueJobs, Remote Python, Landing.jobs (Europe), Platsbanken (Sweden's public job service), the Hacker News "Who is hiring?" thread, and the career pages of 150+ companies on Greenhouse, Ashby, Lever and SmartRecruiters (Stripe, OpenAI, Anthropic, Cloudflare, Spotify, Canva, Wise, GitLab and more). These career pages are where sites like Wellfound and HiringCafe get most of their listings; Job Hunter reads them at the source. With **Search Google too** on, Gemini also finds posts on LinkedIn, Indeed, Glassdoor and company sites.

**Does it work on Windows or Mac?**
This version targets Linux (the window, Auto-run through cron, and the PDF export through Chrome or Chromium). The Windows version, with its installer, is in this repository's git history from before the Linux conversion. Pull requests for macOS are welcome.

**How do I get a free Gemini API key?**
Create one at https://aistudio.google.com/app/apikey. The window asks for it the first time it opens, with step-by-step help.

## Disclaimer

- This tool is for **personal job searching** only. Respect each job site's terms of service and robots.txt, and don't use it to re-publish listings or to collect emails.
- Gemini can make mistakes. **Read every CV, cover letter and email before you send it.** You're responsible for what you send.
- Job posts are written by strangers, and some may be scams. Never pay to apply, and be careful with anyone asking for money or personal documents.
- There's no guarantee of jobs, interviews or replies.
- The software is provided "as is", without warranty. See [LICENSE](LICENSE).

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Good first contributions: new job sources, macOS support, better email extraction, tests, translations.

## Support

If Job Hunter helped you land interviews, star the repo ⭐ and tell a friend.

## License

[MIT](LICENSE) © Ahsan Mehmood

## Related searches

remote job search bot, remote jobs for Pakistan, AI job application automation, tailored CV generator, ATS resume generator, cover letter generator, Gemini API project, free job hunting tool, Python job scraper, Gmail draft automation, Hacker News Who is hiring, RemoteOK, Remotive, We Work Remotely, Himalayas.
