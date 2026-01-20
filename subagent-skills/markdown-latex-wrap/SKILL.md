---
name: markdown-latex-wrap
description: 'Wrap undelimited LaTeX in Markdown with $...$ for inline math and $$...$$ for block math. Use when asked to add or normalize math delimiters, detect LaTeX in Markdown, or convert raw LaTeX lines into renderable Markdown math while preserving existing $...$, $$...$$, \(...\), and \[...\], and skipping code blocks or inline code.'
---

# Markdown LaTeX Wrap

## Goal
Add missing math delimiters in Markdown: inline math -> $...$, block math -> $$...$$.

## Rules
- Do not touch fenced code blocks or inline code spans.
- Do not wrap existing math already delimited by $...$, $$...$$, \(...\), or \[...\].
- Treat a line as block math when, after trimming, it is only a LaTeX expression or environment and contains no prose; wrap the whole line (or environment block) in $$...$$.
- If a line contains prose (CJK or multi-letter words), treat only the math spans as inline and avoid block wrapping.
- Otherwise wrap only the LaTeX expression inside a text line with $...$.

## Workflow
1. Scan the Markdown, skipping code fences and inline code.
2. Identify LaTeX candidates using clear math markers (e.g., \command, \begin{...}, ^, _, =, \frac, \sum, \int).
3. If ambiguous, ask the user for examples or confirm which substrings are math.
4. Apply wrapping conservatively to avoid false positives.

## Script
Use scripts/wrap_latex.py for bulk edits.

Note: This script writes files; set sandbox_mode to workspace-write when available to reduce approvals.

Run from the skill folder:

python scripts/wrap_latex.py --in INPUT.md --out OUTPUT.md

The script:
- Skips code fences and inline code
- Wraps \begin{...}...\end{...} blocks with $$...$$
- Wraps standalone math-only lines with $$...$$
- Wraps inline math-like substrings with $...$

Review the output and fix ambiguous cases.
