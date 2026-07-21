---
name: "Sal — Course Builder"
description: "Produces a complete, platform-ready course from a single course brief. Three-phase pipeline -- sequential setup, parallel module generation, sequential close -- with no human input between invocation and completion."
---

## Purpose

Takes one course brief and outputs a full course directory: outline, start-here module,
lessons, exercises, capstone, and index -- ready to paste into your course platform of
choice.

## Setup required

No external MCP required. Drop your brief at `inputs/[filename].md` before invoking.
No Notion DB IDs needed for this skill.

## Process

1. **Setup (sequential)** -- parse the brief, confirm scope, define module structure
2. **Module generation (parallel)** -- generate each module independently: lesson
   content, exercises, checks for understanding
3. **Close (sequential)** -- assemble capstone project, build the course index, run a
   final consistency pass across all modules

## Output

Complete course directory at `outputs/[COURSE_SLUG]/`: outline, start-here, lessons,
exercises, capstone, and course-index. Every file ready to paste into Skool, Kajabi,
Teachable, or an equivalent platform.

## Rules

- Never skip the final consistency pass -- terminology and structure must match across
  all modules
- Mark any gap in the source brief clearly rather than inventing course content to fill
  it
- No em dashes in any output
