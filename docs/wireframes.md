# Wireframes — PDF Compressor

Low-fidelity sketches of the app's 5 states. These are intentionally rough — boxes and labels only, no styling. The goal is to lock layout and content before visual design.

## State 1: Empty (initial load)

```
┌─────────────────────────────────────────────────┐
│  📦 PDF Compressor                              │
├─────────────────────────────────────────────────┤
│                                                 │
│  ┌───────────────────────────────────────────┐  │
│  │                                           │  │
│  │              ⬆                           │  │
│  │     Drop PDF files here                   │  │
│  │     or click to browse                    │  │
│  │                                           │  │
│  │     Max 10 files · 50MB each              │  │
│  │                                           │  │
│  └───────────────────────────────────────────┘  │
│                                                 │
│  Compression quality                            │
│  ┌──────┐  ┌────────┐  ┌──────┐                 │
│  │ Low  │  │ Medium │  │ High │                 │
│  └──────┘  └────────┘  └──────┘                 │
│             (selected)                          │
│                                                 │
│  ┌─────────────────────────────────────────┐    │
│  │      Compress Files (disabled)          │    │
│  └─────────────────────────────────────────┘    │
│                                                 │
└─────────────────────────────────────────────────┘
```

## State 2: Files added

```
┌─────────────────────────────────────────────────┐
│  📦 PDF Compressor                              │
├─────────────────────────────────────────────────┤
│                                                 │
│  ┌───────────────────────────────────────────┐  │
│  │      ⬆ Add more files                    │  │
│  └───────────────────────────────────────────┘  │
│                                                 │
│  3 files (9.3 MB total)                         │
│  ┌─────────────────────────────────────────┐    │
│  │ 📄 report.pdf       2.4 MB        ✕     │    │
│  │ 📄 invoice.pdf      1.1 MB        ✕     │    │
│  │ 📄 contract.pdf     5.8 MB        ✕     │    │
│  └─────────────────────────────────────────┘    │
│                                                 │
│  Compression quality                            │
│  ┌──────┐  ┌────────┐  ┌──────┐                 │
│  │ Low  │  │ Medium │  │ High │                 │
│  └──────┘  └────────┘  └──────┘                 │
│                                                 │
│  ┌─────────────────────────────────────────┐    │
│  │         Compress 3 Files                │    │
│  └─────────────────────────────────────────┘    │
│                                                 │
└─────────────────────────────────────────────────┘
```

## State 3: Compressing

```
┌─────────────────────────────────────────────────┐
│  📦 PDF Compressor                              │
├─────────────────────────────────────────────────┤
│                                                 │
│                                                 │
│           Compressing your files...             │
│                                                 │
│         ┌─────────────────────────┐             │
│         │  ████████████░░░░░░░░   │   2 of 3    │
│         └─────────────────────────┘             │
│                                                 │
│         Currently: invoice.pdf                  │
│                                                 │
│                                                 │
└─────────────────────────────────────────────────┘
```

## State 4: Done (results + download)

```
┌─────────────────────────────────────────────────┐
│  📦 PDF Compressor                              │
├─────────────────────────────────────────────────┤
│                                                 │
│   ✓ Compression complete                        │
│                                                 │
│   Saved 6.2 MB total (67% reduction)            │
│                                                 │
│   ┌─────────────────────────────────────────┐   │
│   │ report.pdf      2.4 MB → 0.8 MB  (-67%) │   │
│   │ invoice.pdf     1.1 MB → 0.4 MB  (-64%) │   │
│   │ contract.pdf    5.8 MB → 1.9 MB  (-67%) │   │
│   └─────────────────────────────────────────┘   │
│                                                 │
│   ┌─────────────────────────────────────────┐   │
│   │       ⬇  Download ZIP (3.1 MB)          │   │
│   └─────────────────────────────────────────┘   │
│                                                 │
│   Compress more files                           │
│                                                 │
└─────────────────────────────────────────────────┘
```

## State 5: Error

```
┌─────────────────────────────────────────────────┐
│  📦 PDF Compressor                              │
├─────────────────────────────────────────────────┤
│                                                 │
│   ⚠ Something went wrong                        │
│                                                 │
│   We couldn't compress your files. Please       │
│   check your connection and try again.          │
│                                                 │
│   ┌─────────────────────────────────────────┐   │
│   │              Try again                  │   │
│   └─────────────────────────────────────────┘   │
│                                                 │
└─────────────────────────────────────────────────┘
```

## Notes for visual design phase

When moving to high-fidelity in Figma:
- Use shadcn/ui components (Button, Card, Progress, Alert)
- Stick to 2-3 colors max + grayscale
- Use a single sans-serif font (Inter is a safe default)
- Mobile breakpoint: stack everything vertically, full-width buttons
