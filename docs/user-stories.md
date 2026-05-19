# User Stories — PDF Compressor

## US-01: Upload PDF files
**As a user**, I want to upload up to 10 PDF files by dragging or selecting them, **so I can prepare them for compression.**

**Acceptance Criteria:**
- User can drag and drop files onto a dropzone
- User can also click the dropzone to open a file picker
- Only `.pdf` files are accepted; others show an error
- Maximum 10 files at once
- Maximum 50MB per file
- Each uploaded file shows: name, size, remove button
- User can remove individual files before compressing

---

## US-02: Choose compression quality
**As a user**, I want to choose a compression level **so I can balance file size against quality.**

**Acceptance Criteria:**
- Three options visible: Low, Medium, High compression
- Each option has a short description (e.g., "High = smallest file, lower image quality")
- Default selection: Medium
- Selection persists until user changes it

---

## US-03: Start compression
**As a user**, I want to start compression with one click **so I don't have to configure anything else.**

**Acceptance Criteria:**
- Compress button is disabled until at least one file is uploaded
- Clicking it sends files to backend
- Button shows loading state while processing
- User cannot add/remove files during compression

---

## US-04: See compression progress
**As a user**, I want to see progress while files are being compressed **so I know the app is working.**

**Acceptance Criteria:**
- Progress indicator visible during processing
- Shows current state: "Uploading...", "Compressing...", "Preparing download..."
- Shows which file is being processed if multiple (e.g., "2 of 5")

---

## US-05: View compression results
**As a user**, I want to see how much each file shrunk **so I can confirm the tool worked.**

**Acceptance Criteria:**
- For each file, show: original size → new size, % reduction
- Highlight total bytes saved
- If a file failed, show error message for that specific file

---

## US-06: Download compressed files
**As a user**, I want to download my compressed files **so I can use them.**

**Acceptance Criteria:**
- Single file: download directly as a PDF
- Multiple files: download as a single ZIP
- Download starts on button click
- After download, user can compress more files (reset state)

---

## US-07: Handle errors gracefully
**As a user**, I want clear error messages when something fails **so I know what to do.**

**Acceptance Criteria:**
- Network error: "Connection lost. Please try again."
- File too big: "File X exceeds 50MB limit."
- Wrong file type: "Only PDF files are supported."
- Server error: "Something went wrong. Please try again."
- Errors don't crash the page
