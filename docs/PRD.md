# PDF Compressor — Product Requirements Document

**Last updated:** May 18, 2026
**Author:** [your name]
**Status:** Draft v1

## Problem
Existing PDF compression tools are often expensive (paid SaaS like Smallpdf, Adobe) or come with privacy concerns when users upload sensitive documents to third-party servers. Users frequently hit email and upload size limits when sharing PDFs, forcing them to find a compression solution. A free, simple, reliable PDF compressor fills this gap.

## Target users
Anyone who needs to reduce PDF file sizes — particularly people hitting email attachment limits, students submitting assignments, and professionals sharing reports or contracts. No login required, no technical knowledge expected.

## Goals (success metrics)
- Users can successfully compress a PDF in under 30 seconds end-to-end
- Average file size reduction of 40%+ on image-heavy PDFs
- Tool stays free to operate (low infrastructure cost)
- Build a working portfolio-grade full-stack project demonstrating React + Python + cloud deployment

## Non-goals (what we are NOT doing in MVP)
- No user accounts, signup, or login
- No file types other than PDF (no images, no docx, no generic zip)
- No file history or saved compressions
- No target file size mode (e.g., "make it under 2MB") — quality slider only
- No payment, premium tier, or subscriptions
- No batch above 10 files
- No files larger than 50MB per file
- No advanced PDF editing (merge, split, rotate, etc.)

## Solution overview
A single-page web app where users drag-and-drop up to 10 PDF files, choose a compression quality (Low / Medium / High), and click compress. Files upload to a Python backend running Ghostscript, which performs the actual compression. Once complete, the user sees before/after sizes and downloads either a single PDF or a ZIP of all compressed files. Uploaded files are auto-deleted from the server within 1 hour.

## MVP scope (v1)
- Drag-and-drop or click-to-select file upload (max 10 PDFs, max 50MB each)
- PDF file type and size validation with clear error messages
- Compression quality selector: Low / Medium / High
- Server-side compression using Ghostscript
- Progress indicator during compression
- Results view showing original size → new size → % reduction per file
- Download as single PDF (1 file) or ZIP (multiple files)
- Error handling for network failures, server errors, and failed compressions
- Auto-cleanup of files on server after 1 hour

## Future scope (v2 and beyond)
- Target file size mode ("make this under X MB")
- Support for other file types (images, docx)
- User accounts with compression history
- Higher file size and batch limits
- AWS Lambda + S3 migration for better scalability
- Custom domain
- Real-time WebSocket progress updates instead of polling
- Mobile-optimized UX improvements

## Constraints
- **Time:** ~2 weeks part-time to MVP, then AWS migration
- **Budget:** Free hosting tier initially (Railway + Vercel); migrate to AWS within free tier limits
- **Team:** Solo developer (first real project)
- **Skill:** Learning React, FastAPI, and cloud deployment simultaneously — scope kept narrow on purpose

## Tech stack
- **Frontend:** React (Vite) + Tailwind CSS + shadcn/ui
- **Backend:** Python + FastAPI + Ghostscript
- **Storage:** Local disk (MVP), S3 later
- **Hosting:** Railway (backend) + Vercel (frontend) for MVP; AWS migration planned
- **Project tracking:** GitHub Projects

## Open questions
- What's the actual compression ratio we'll achieve on text-heavy vs image-heavy PDFs?
- Will Ghostscript handle all PDF variants users throw at it, or will some fail?
- Is the Railway free tier sufficient, or will compression workloads hit limits?
- For AWS migration: Lambda (with 15-min timeout) vs EC2 (always-on cost)?
- How will we handle a user closing the tab mid-compression — orphaned files on server?
