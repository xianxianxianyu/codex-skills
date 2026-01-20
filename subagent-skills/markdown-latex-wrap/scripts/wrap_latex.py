#!/usr/bin/env python3
"""Wrap undelimited LaTeX in Markdown."""

import argparse
import re
from pathlib import Path

CODE_FENCE_RE = re.compile(r"^\s*(```|~~~)")
BEGIN_ENV_RE = re.compile(r"\\begin\{[^}]+\}")
END_ENV_RE = re.compile(r"\\end\{[^}]+\}")
INLINE_CODE_SPLIT_RE = re.compile(r"(`[^`]*`)")
BLOCK_MATH_START_RE = re.compile(r"^\s*(\$\$|\\\[)\s*$")
BLOCK_MATH_END_RE = re.compile(r"^\s*(\$\$|\\\])\s*$")
ARG_COMMAND_FIX_RE = re.compile(r"\$(\\+[A-Za-z]+)\$\{([^}]+)\}")
CJK_RE = re.compile(r"[\u4e00-\u9fff]")
PROSE_WORD_RE = re.compile(r"[A-Za-z]{2,}")
INLINE_MATH_RE = re.compile(
    r"(?<![A-Za-z0-9_])("
    r"\\+[A-Za-z]+(?:\s*\{[^}]*\})*"
    r"|[A-Za-z0-9]+(?:\s*(?:\\+_|_)\s*[A-Za-z0-9]+)+"
    r"|[A-Za-z0-9]+(?:\s*[=+*/<>-]\s*[A-Za-z0-9]+)+"
    r")(?![A-Za-z0-9_])"
)


def line_has_existing_math_delims(line):
    return "$" in line or "\\[" in line or "\\]" in line or "\\(" in line or "\\)" in line


def is_math_only_line(line):
    stripped = line.strip()
    if not stripped:
        return False
    if line_has_existing_math_delims(stripped):
        return False
    if CJK_RE.search(stripped) or PROSE_WORD_RE.search(stripped):
        return False
    if re.search(r"\\+[A-Za-z]+", stripped):
        return True
    if re.search(r"[A-Za-z0-9]\s*[\^_]\s*[A-Za-z0-9]", stripped):
        return True
    if re.search(r"[A-Za-z0-9]\s*[=+*/<>-]\s*[A-Za-z0-9]", stripped):
        return True
    return False


def fix_command_arguments(line):
    return ARG_COMMAND_FIX_RE.sub(r"$\1{\2}$", line)


def wrap_inline(segment):
    return INLINE_MATH_RE.sub(lambda m: f"${m.group(0)}$", segment)


def process_inline_line(line):
    parts = INLINE_CODE_SPLIT_RE.split(line)
    for i, part in enumerate(parts):
        if part.startswith("`") and part.endswith("`"):
            continue
        collapsed = re.sub(r"\$+", "$", part)
        if "$" in collapsed:
            text_parts = collapsed.split("$")
            for j in range(0, len(text_parts), 2):
                text_parts[j] = wrap_inline(text_parts[j])
            collapsed = "$".join(text_parts)
        else:
            collapsed = wrap_inline(collapsed)
        parts[i] = collapsed
    merged = "".join(parts)
    return fix_command_arguments(merged)


def prev_nonempty(lines):
    for line in reversed(lines):
        if line.strip():
            return line
    return ""


def process_lines(lines):
    out_lines = []
    in_code = False
    in_env = False
    in_block = False
    env_lines = []
    block_lines = []
    env_has_delim_before = False

    for line in lines:
        if CODE_FENCE_RE.match(line):
            if in_env:
                out_lines.extend(env_lines)
                env_lines = []
                in_env = False
            if in_block:
                out_lines.extend(block_lines)
                block_lines = []
                in_block = False
            in_code = not in_code
            out_lines.append(line)
            continue

        if in_code:
            out_lines.append(line)
            continue

        if in_block:
            block_lines.append(line)
            if BLOCK_MATH_END_RE.match(line):
                content_lines = block_lines[1:-1]
                nonempty = [l for l in content_lines if l.strip()]
                if len(nonempty) == 1 and not is_math_only_line(nonempty[0]) and not BEGIN_ENV_RE.search(nonempty[0]):
                    for content in content_lines:
                        if not content.strip():
                            out_lines.append(content)
                        else:
                            out_lines.append(process_inline_line(content))
                else:
                    out_lines.extend(block_lines)
                block_lines = []
                in_block = False
            continue

        if BLOCK_MATH_START_RE.match(line):
            in_block = True
            block_lines = [line]
            continue

        if in_env:
            env_lines.append(line)
            if END_ENV_RE.search(line):
                first = env_lines[0]
                last = env_lines[-1]
                if (
                    not env_has_delim_before
                    and not line_has_existing_math_delims(first)
                    and not line_has_existing_math_delims(last)
                ):
                    out_lines.append("$$\n")
                    out_lines.extend(env_lines)
                    out_lines.append("$$\n")
                else:
                    out_lines.extend(env_lines)
                env_lines = []
                in_env = False
            continue

        if BEGIN_ENV_RE.search(line):
            env_has_delim_before = False
            prev_line = prev_nonempty(out_lines)
            if prev_line.strip() in ("$$", "\\["):
                env_has_delim_before = True
            env_lines = [line]
            in_env = True
            if END_ENV_RE.search(line):
                first = env_lines[0]
                if not env_has_delim_before and not line_has_existing_math_delims(first):
                    out_lines.append("$$\n")
                    out_lines.extend(env_lines)
                    out_lines.append("$$\n")
                else:
                    out_lines.extend(env_lines)
                env_lines = []
                in_env = False
            continue

        if is_math_only_line(line):
            out_lines.append("$$\n")
            out_lines.append(line)
            out_lines.append("$$\n")
            continue

        out_lines.append(process_inline_line(line))

    if in_env:
        out_lines.extend(env_lines)
    if in_block:
        out_lines.extend(block_lines)

    return out_lines


def main():
    parser = argparse.ArgumentParser(description="Wrap undelimited LaTeX in Markdown.")
    parser.add_argument("--in", dest="input_path", required=True, help="Input Markdown file")
    parser.add_argument("--out", dest="output_path", required=True, help="Output Markdown file")
    args = parser.parse_args()

    input_path = Path(args.input_path)
    output_path = Path(args.output_path)

    text = input_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    processed = process_lines(lines)
    output_path.write_text("".join(processed), encoding="utf-8")


if __name__ == "__main__":
    main()