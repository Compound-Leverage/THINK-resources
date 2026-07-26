# Automation Ops Audit -- Workflow

An advisory review of your own fleet of scheduled agents/automations -- how much they
notify you, where they pause waiting for your approval, and how dense their combined
schedule has gotten. Useful once you're running more than a couple of scheduled routines
and the notification volume itself has become worth managing.

**Trigger:** on demand, or monthly if you want it recurring. Run it when notification
volume feels high, your automation count has grown, or you just want a governance
check-in.

**Output:** an advisory report to your notification destination. This skill never
changes anything itself -- you approve every recommendation before it's implemented.

## What this audit covers
1. **Notification load** -- every ping each automation sends, to whom, under what
   condition
2. **Approval gates** -- every point where an automation pauses waiting on you
3. **Schedule density** -- how many routines fire per day and whether any conflict
4. **Consolidation opportunities** -- what can be silenced, batched into a digest, or
   otherwise reduced
5. **Autonomy gaps** -- automations that pause for approval on something genuinely
   mechanical, where a gate probably isn't earning its keep

## Step 1: Read every automation's own hook-map or schedule doc

For every automation you run, read whatever documents its trigger and notification
behavior (a `hooks/hook-map.md` if you're using this repo's persona-folder pattern, or
your own equivalent). Extract:

| Automation | Schedule/trigger | Notification target | Notification condition | Approval gate? |
|---|---|---|---|---|

If an automation has no documented schedule, flag it: `[automation] -- no schedule doc,
trigger unknown`.

## Step 2: Check each automation's own instructions for notification rules

For each automation, check its own instructions (a CLAUDE.md, SKILL.md, or system
prompt) for:
- Explicit notification instructions
- Approval-gate language ("wait for approval," "post before proceeding")
- Any "route to [owner]" instructions
- Silent-run conditions, if any

## Step 3: Map the combined schedule

Build a day-by-day view of every automation's firing times:

```
SUNDAY:    [list all automations that run, with times]
MONDAY:    [list all automations that run, with times]
...
```

Flag any day approaching or exceeding your platform's routine-count cap, if it has one.
Flag any time slot where two or more automations fire simultaneously, especially if they
touch the same resource (same database, same account, same webhook).

## Step 4: Classify each notification

| Class | Definition | Recommended action |
|---|---|---|
| Keep -- immediate | Error, failed run, a genuinely high-stakes signal, an external send about to go out | Keep as-is |
| Batch into a digest | Routine completion, counts, a routine queue update, an intake summary | Route to a daily/weekly digest automation, if you have one, and drop the direct ping |
| Silent | An internal write, a routine scoring update, anything with no decision attached | Log only, no ping |
| Gate -- keep | An external send, an irreversible action, a genuinely high-stakes decision | Keep the approval gate |
| Gate -- remove | A routine internal update, a rule-based fix, a completed scan with nothing to decide | The automation should act on its own |

## Step 5: Identify consolidation opportunities

Produce three lists from the classification above:

**Notifications to silence:**
- [automation]: [what it currently pings about] -> silent log instead

**Notifications to batch into a digest** (if you have one):
- [automation]: [what it currently pings about] -> routed to [your digest automation]

**Approval gates to remove:**
- [automation]: [gate description] -> reason the gate isn't earning its keep

**Approval gates to keep:**
- [automation]: [gate description] -> reason the gate is required

## Step 6: Flag schedule conflicts

For each day with high density: which automations fire together, whether they share a
resource, and a recommended time offset to stagger them.

## Step 7: Build the advisory report

```
AUTOMATION OPS AUDIT -- [date]

NOTIFICATION LOAD
Total pings (current): [n]
After recommended changes: [n]

SCHEDULE
Peak day: [day] -- [n] automations
Conflicts: [list, or "none"]

CHANGES RECOMMENDED
Silence:
  - [automation]: [what changes]

Batch into a digest:
  - [automation]: [what changes]

Gates to remove:
  - [automation]: [what changes]

Gates to keep:
  - [automation]: [why]

IMPLEMENTATION ORDER
1. [highest-impact, lowest-risk change]
2. ...

No changes have been made. You approve before anything is modified.
```

Post the full report to your notification destination. If it's too long for one message,
write it to a log file and post the summary plus the file path instead.
