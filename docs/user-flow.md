# User Flow — PDF Compressor

This document maps how a user moves through the app, from opening it to completing a compression.

## Flow Diagram

```
   ┌─────────────┐
   │   START     │
   │ (open app)  │
   └──────┬──────┘
          │
          ▼
   ┌─────────────┐
   │ Empty state │
   │  (dropzone) │
   └──────┬──────┘
          │ user drops/selects files
          ▼
   ┌─────────────┐         ┌─────────────┐
   │  Validate   │── fail ▶│ Show error  │
   │   files     │         │  (inline)   │
   └──────┬──────┘         └──────┬──────┘
          │ valid                  │
          ▼                        │
   ┌─────────────┐                 │
   │Files added  │◀────────────────┘
   │  state      │
   └──────┬──────┘
          │ user clicks Compress
          ▼
   ┌─────────────┐         ┌─────────────┐
   │ Compressing │── fail ▶│ Error state │
   │  (progress) │         │             │
   └──────┬──────┘         └──────┬──────┘
          │ success                │
          ▼                        ▼
   ┌─────────────┐         ┌─────────────┐
   │   Results   │         │  Try again  │
   │  (download) │         └─────────────┘
   └──────┬──────┘
          │ user downloads
          ▼
   ┌─────────────┐
   │   Reset?    │── yes ─▶ back to Empty state
   └──────┬──────┘
          │ no
          ▼
   ┌─────────────┐
   │     END     │
   └─────────────┘
```

## States

| State | What user sees | Triggered by |
|---|---|---|
| Empty | Dropzone with "Drop PDFs here" message | App load, or after reset |
| Validating | Brief check after files dropped | File drop or selection |
| Files added | List of selected files, quality selector, Compress button | Valid files dropped |
| Compressing | Progress bar, "X of Y" indicator | Compress button click |
| Results | Before/after sizes, Download button | Compression complete |
| Error | Error message + Try again button | Any failure |

## Key transitions

- **Empty → Files added:** User drops or selects valid PDFs
- **Files added → Empty:** User removes all files
- **Files added → Compressing:** User clicks Compress
- **Compressing → Results:** Backend returns compressed files
- **Compressing → Error:** Backend fails or network issue
- **Results → Empty:** User clicks "Compress more"
- **Error → Files added:** User clicks "Try again"

## Edge cases to handle

- User drops non-PDF files → reject with error, keep existing valid files
- User drops 11+ files → only accept first 10, show warning
- User drops file > 50MB → reject that file, keep others
- User closes tab during compression → orphaned files on server (cleanup job handles)
- Backend takes > 30 seconds → keep showing progress, don't time out frontend prematurely
