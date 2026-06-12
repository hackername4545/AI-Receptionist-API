# AI Receptionist API

A REST API that acts as a smart business receptionist — answers visitor questions, books appointment slots, and saves them to a file. Powered by **Groq** (llama-3.3-70b) and **FastAPI**.

---

## Folder structure

```
testtry/
├── main.py          ← the API server
├── test_main.py     ← the test suite
├── .env             ← your secret API key (you create this)
└── bookings.json    ← created automatically when first booking is made
```

---

## Step 1 — Install dependencies

Open a terminal in your project folder and run:

```bash
pip install fastapi uvicorn groq pytest httpx python-dotenv
```

---

## Step 2 — Get your Groq API key

1. Go to **[console.groq.com](https://console.groq.com)**
2. Sign up or log in
3. Click **API Keys** in the left sidebar
4. Click **Create API Key**
5. Copy the key — it starts with `gsk_`

---

## Step 3 — Create the .env file

In your `testtry/` folder, create a new file called `.env` (no other name, just `.env`).

Open it and paste:

```
GROQ_API_KEY=gsk_your_actual_key_here
```

> Replace `gsk_your_actual_key_here` with the key you copied from Groq.
> No quotes. No spaces around the `=`.

---

## Step 4 — Start the server

In your terminal, make sure you are inside the `testtry/` folder, then run:

```bash
python -m uvicorn main:app --reload
```

You should see:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
```

---

## Step 5 — Open in browser

Open **Google Chrome** (or any browser) and go to:

```
http://127.0.0.1:8000/docs
```

This opens the **Swagger UI** — a built-in page where you can test all your endpoints by clicking buttons, no code needed.

---

## What you can do in Swagger

| Endpoint | What it does |
|---|---|
| `POST /api/v1/receptionist/chat` | Talk to the AI receptionist |
| `POST /api/v1/receptionist/book` | Book an appointment slot |
| `GET /api/v1/receptionist/bookings` | View all booked slots |
| `DELETE /api/v1/receptionist/bookings/{id}` | Cancel a booking |
| `GET /health` | Check if server is running |

---

## Test the chat

Click `POST /api/v1/receptionist/chat` → **Try it out** → paste this → **Execute**:

```json
{
  "message": "Hi, I want to book an appointment",
  "business_name": "Pixel Studio",
  "business_context": "a creative design agency in Chennai"
}
```

## Book a slot

Click `POST /api/v1/receptionist/book` → **Try it out** → paste this → **Execute**:

```json
{
  "name": "Sathiya",
  "email": "sathiya@gmail.com",
  "slot": "2024-06-15 10:00 AM",
  "reason": "Product demo"
}
```

---

## Run the tests

In your terminal (inside `testtry/`):

```bash
python -m pytest test_main.py -v
```

You should see 10 tests all passing.

---

## Stop the server

Press `Ctrl + C` in the terminal.

---

## Common errors

| Error | Fix |
|---|---|
| `Invalid API Key` | Check your `.env` file — key must start with `gsk_` |
| `ModuleNotFoundError` | Run `pip install fastapi uvicorn groq python-dotenv` |
| `Address already in use` | Another server is running — close it or restart terminal |
| `0 items collected` | Make sure test file is named `test_main.py` |
