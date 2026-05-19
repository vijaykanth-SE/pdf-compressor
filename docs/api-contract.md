# API Contract — PDF Compressor

The agreement between frontend and backend. Frontend codes against this; backend implements this. Keeps both in sync.

**Base URL (dev):** `http://localhost:8000`
**Base URL (prod):** TBD (Railway deploy URL)

---

## POST `/api/compress`

Upload PDFs and start compression.

### Request

- **Method:** POST
- **Content-Type:** `multipart/form-data`
- **Body:**
  - `files`: 1-10 PDF files
  - `quality`: string, one of `"low"`, `"medium"`, `"high"`

### Response — 200 OK

Returns the compressed file(s) directly.

- **Single file:** `application/pdf` binary stream
- **Multiple files:** `application/zip` binary stream

**Custom response headers** (so frontend can show before/after stats):
```
X-Original-Size: 9762304
X-Compressed-Size: 3245056
X-Files-Processed: 3
X-Files-Failed: 0
```

### Errors

| Status | When | Response body |
|---|---|---|
| 400 | No files, wrong file type, or invalid quality | `{ "error": "message" }` |
| 413 | File or total payload too large | `{ "error": "File X exceeds 50MB" }` |
| 422 | Validation error on request shape | `{ "error": "Invalid quality value" }` |
| 500 | Ghostscript failed or unknown error | `{ "error": "Compression failed" }` |

### Limits

- Max 10 files per request
- Max 50MB per file
- Max 200MB total payload
- Request timeout: 5 minutes

---

## GET `/api/health`

Simple health check. Used for uptime monitoring and deployment verification.

### Response — 200 OK

```json
{
  "status": "ok",
  "ghostscript": "available",
  "version": "1.0.0"
}
```

---

## Quality level mapping (Ghostscript presets)

| Quality | Ghostscript `-dPDFSETTINGS` | Use case |
|---|---|---|
| low | `/screen` | 72 DPI — smallest file, web viewing |
| medium | `/ebook` | 150 DPI — good balance |
| high | `/printer` | 300 DPI — high quality, larger file |

---

## CORS

Backend must allow:
- **Origin:** `http://localhost:5173` (Vite dev) and prod frontend URL
- **Methods:** `GET, POST, OPTIONS`
- **Headers:** `Content-Type`
- **Expose headers:** `X-Original-Size, X-Compressed-Size, X-Files-Processed, X-Files-Failed`

---

## Open decisions

- **Sync vs async:** For MVP, this is synchronous — frontend waits for the response. If compression of 10 large files exceeds ~30 seconds reliably, switch to job-based async pattern (POST returns `job_id`, frontend polls `GET /api/status/{job_id}`).
- **Auth:** None for MVP. Add API key or rate limiting before public launch to prevent abuse.
