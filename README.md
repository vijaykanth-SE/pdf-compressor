# PDF Compressor

A simple, free web app to compress PDF files. Drop up to 10 PDFs, pick a quality level, download the compressed result.

## Status
🚧 In development — MVP planning phase complete.

## Tech stack
- **Frontend:** React (Vite) + Tailwind CSS + shadcn/ui
- **Backend:** Python + FastAPI + Ghostscript
- **Hosting:** Railway (backend) + Vercel (frontend); AWS migration planned

## Project documentation

All planning and design docs live in `/docs`:

- [`PRD.md`](docs/PRD.md) — Product requirements (problem, users, scope)
- [`user-stories.md`](docs/user-stories.md) — User stories with acceptance criteria
- [`user-flow.md`](docs/user-flow.md) — How a user moves through the app
- [`wireframes.md`](docs/wireframes.md) — Low-fidelity sketches of each state
- [`api-contract.md`](docs/api-contract.md) — Backend API spec (frontend ↔ backend agreement)
- [`tickets.md`](docs/tickets.md) — Work broken into tickets, with estimates

## Local development

### Prerequisites
- Node.js 20+
- Python 3.11+
- Ghostscript installed and available on PATH

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Backend runs on `http://localhost:8000`.

### Frontend
```bash
cd frontend
npm install
npm run dev
```
Frontend runs on `http://localhost:5173`.

## Project structure
```
pdf-compressor/
├── docs/         # Planning & design docs
├── backend/      # Python FastAPI server
├── frontend/     # React + Vite app
└── README.md
```
