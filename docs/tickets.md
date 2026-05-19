# Tickets / Backlog — PDF Compressor

All work broken into tickets. Copy these into GitHub Projects (or Linear/Trello). One ticket = one focused unit of work.

**Total estimate:** ~46 hours. Add 1.5x buffer → plan for ~70 hours over 2-3 weeks part-time.

---

## Epic 1: Project Setup (3.5h)

- [ ] **SETUP-01** Initialize Git repo + `.gitignore` — 30min
- [ ] **SETUP-02** Set up backend folder with FastAPI hello world — 1h
- [ ] **SETUP-03** Set up frontend folder with Vite + React + Tailwind — 1h
- [ ] **SETUP-04** Set up shadcn/ui in frontend — 30min
- [ ] **SETUP-05** Install Ghostscript locally, verify CLI works — 30min

## Epic 2: Backend Core — covers US-01, US-03, US-06 (11.5h)

- [ ] **BE-01** Endpoint: accept one PDF upload, return it unchanged — 2h
- [ ] **BE-02** Wire Ghostscript via subprocess to compress one PDF — 3h
- [ ] **BE-03** Support 3 quality levels (Low/Med/High Ghostscript presets) — 1h
- [ ] **BE-04** Accept multiple files, compress each, return as ZIP — 3h
- [ ] **BE-05** Validate file type (PDF only) and size (50MB max) — 1h
- [ ] **BE-06** Add CORS middleware so frontend can call backend — 30min
- [ ] **BE-07** Cleanup temp files after response sent — 1h

## Epic 3: Frontend Core — covers US-01, US-02, US-03 (9h)

- [ ] **FE-01** Build FileDropzone component (drag-drop + click) — 3h
- [ ] **FE-02** Build FileList component (show files, remove button) — 2h
- [ ] **FE-03** Build QualitySelector component (3 options) — 1h
- [ ] **FE-04** Build CompressButton with disabled/loading states — 1h
- [ ] **FE-05** API client function to upload files to backend — 2h

## Epic 4: Frontend Feedback — covers US-04, US-05, US-07 (7h)

- [ ] **FE-06** Build ProgressDisplay component — 2h
- [ ] **FE-07** Build ResultsView component (before/after sizes) — 2h
- [ ] **FE-08** Handle and display all error states — 2h
- [ ] **FE-09** Reset state after download (back to upload screen) — 1h

## Epic 5: Integration & Polish (9h)

- [ ] **INT-01** Connect frontend to backend end-to-end — 2h
- [ ] **INT-02** Test with real PDFs of various sizes — 1h
- [ ] **INT-03** Trigger download on completion — 1h
- [ ] **INT-04** Mobile responsive check — 2h
- [ ] **POLISH-01** Loading spinners, empty states, micro-animations — 3h

## Epic 6: Deployment (6h)

- [ ] **DEPLOY-01** Push to GitHub — 30min
- [ ] **DEPLOY-02** Deploy frontend to Vercel — 1h
- [ ] **DEPLOY-03** Deploy backend to Railway with Dockerfile — 3h
- [ ] **DEPLOY-04** Configure production CORS — 30min
- [ ] **DEPLOY-05** Test live end-to-end — 1h

## Epic 7: Future — AWS Migration (post-MVP)

- [ ] **AWS-01** Set up AWS account + billing alerts
- [ ] **AWS-02** Move frontend to S3 + CloudFront
- [ ] **AWS-03** Convert backend to Lambda + API Gateway
- [ ] **AWS-04** Set up S3 for file storage with lifecycle cleanup
- [ ] **AWS-05** CloudWatch monitoring

---

## Order of work (dependency-driven)

```
SETUP (all)
  ↓
BE-01 → BE-02 → BE-03 → BE-04 → BE-05 → BE-06 → BE-07
  ↓
FE-01 → FE-02 → FE-03 → FE-04 → FE-05
  ↓
FE-06 → FE-07 → FE-08 → FE-09
  ↓
INT-01 → INT-02 → INT-03 → INT-04 → POLISH-01
  ↓
DEPLOY-01 → DEPLOY-02 → DEPLOY-03 → DEPLOY-04 → DEPLOY-05
  ↓
SHIPPED 🚀
```

Pull tickets into "Todo" only when their dependencies are done. Focus on one ticket at a time.
