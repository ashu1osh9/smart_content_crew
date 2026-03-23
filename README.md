# Smart Content Crew

A tool I built to automate the boring part of content creation — researching a topic and turning it into a readable blog post, without me having to do it manually every time.

---

## Why I made this

Honestly, I got tired of spending hours researching before writing anything. So I set up two AI agents — one that searches the web and collects info, and another that takes that info and writes a proper blog post out of it. Now I just type a topic and it does the rest.

---

## What it does

- Takes any topic as input
- Searches the web for latest info on it
- Writes a full blog post based on the research
- Saves the output as a markdown file

---

## Project files

```
smart_content_crew/
├── .env.example      # put your api keys here (rename to .env)
├── agents.py         # the two agents — researcher and writer
├── tasks.py          # what each agent is supposed to do
├── crew.py           # connects everything together
├── main.py           # run this to start
├── requirements.txt  # dependencies
└── README.md
```

---

## Getting started

Clone it and go into the folder:

```bash
git clone https://github.com/your-username/smart_content_crew.git
cd smart_content_crew
```

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Set up your API keys — rename `.env.example` to `.env` and fill in the values:

```env
OPENAI_API_KEY=your_openai_key_here
SERPER_API_KEY=your_serper_key_here
```

You'll need:
- OpenAI key from https://platform.openai.com
- Serper key from https://serper.dev (free tier works fine)

---

## Running it

```bash
python main.py
```

It'll ask you for a topic, then the agents take over. The final blog post gets saved as `blog_output.md`.

---

## Built with

- CrewAI
- OpenAI
- Serper API
- python-dotenv

---

## Note

The `.env` file is in `.gitignore` so your API keys won't accidentally get pushed. Only `.env.example` goes to GitHub.
