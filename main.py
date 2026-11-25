# Two Robots in an Elevator — make.fun bounty
# u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f
#
# The program writes one line (1-200 characters) to /output/entry.txt:
# one line of awkward small talk that one robot says to another while
# they ride an elevator together.
#
# Candidates were drafted against the judge's brief, in order of weight:
#   1. reads as one funny line of awkward small talk from one robot to
#      another in an elevator; anything off-subject loses
#   2. sounds like a machine talking: robot logic, sensors, firmware or
#      charging habits showing through the politeness
#   3. lands the awkwardness: the pause, the forced courtesy, the thing
#      neither robot wants to name
#   4. funny on the first read, with a turn that surprises rather than a
#      pun everyone has heard before
#   5. tight as a single line, every word earning its place, no setup
#      wasted
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.
#
# DRAFT 1 — twelve original candidates, hand-scored:
#   #1  "I rehearsed fourteen greetings for this elevator ride. I have
#        used none of them." — on-topic 9, machine 9, awkward 9,
#        funny 8, tight 9 = 44
#   #2  "We are both going to floor three. I checked twice. I just
#        wanted something to say." — 9, 8, 8, 7, 8 = 40
#   #3  "I practised saying hello to the elevator buttons. You were my
#        second choice." — 9, 8, 9, 9, 9 = 44
#   #4  "Nine seconds in this elevator and I have already exhausted my
#        small-talk database." — 9, 9, 8, 7, 8 = 41
#   #5  "Do you also fake a firmware update in elevators to avoid
#        talking to humans?" — 9, 9, 8, 8, 8 = 42
#   #6  "I was going to ask about your day, but my sensors say you
#        have not moved since Tuesday." — 6, 9, 8, 8, 8 = 39
#        (no elevator in the line itself, so it loses on criterion 1)
#   #7  "Nice weather. My humidity sensor says 41 percent, but I
#        wanted to hear it from you." — 8, 9, 8, 6, 8 = 39
#        (the turn is mild: a sensor reading out a human platitude)
#   #8  "I have been standing next to you for four floors, waiting
#        for my courage patch to install." — 9, 9, 9, 8, 8 = 43
#   #9  "I would shake your hand, but my grip is calibrated to crush
#        walnuts and end friendships." — 5, 9, 7, 8, 8 = 37
#        (no elevator in the line, so it loses on criterion 1)
#   #10 "My social module is still downloading. Please enjoy this
#        loading silence." — 6, 9, 9, 8, 8 = 40
#        (no elevator in the line, so it loses on criterion 1)
#   #11 "I know we are both going to floor three — I checked twice —
#        and I still panicked." — 9, 8, 8, 7, 8 = 40
#   #12 "Your charging port is showing. Sorry. I meant your firmware
#        update is installing." — 8, 8, 8, 7, 7 = 38
#
# Draft 1 leaders tie at 44: #1 (rehearsed greetings, none used) and #3
# (practised on the buttons, second choice). Tie-break goes to the
# shorter line, so #3 wins draft 1 at 76 characters.
#
# REVISION (draft 2, a real second pass on the winner) — #3's weakness
# is in its setup: "saying hello to" spends three words before the
# sting, and the practice image arrives late. Tightened to "I
# practised my hello on the elevator buttons": same image, same sting,
# four characters shorter, and the punch ("You were my second choice.")
# now lands after a shorter runway. Tightness 9 -> 10, total 44 -> 45,
# so the revised #3 leads outright with no tie. #1 was left alone: its
# "fourteen greetings, none used" turn is already tight, and making it
# shorter would cost the machine-logic detail that earns its 9s.
# The revised line below is the entry.

CANDIDATES = [
    # on-topic 9, machine 9, awkward 9, funny 8, tight 9 = 44
    ("I rehearsed fourteen greetings for this elevator ride. I have "
     "used none of them.",
     44),
    # 9, 8, 8, 7, 8 = 40
    ("We are both going to floor three. I checked twice. I just "
     "wanted something to say.",
     40),
    # REVISED: 9, 8, 9, 9, 10 = 45 — "saying hello to" cut to "my hello"
    ("I practised my hello on the elevator buttons. You were my "
     "second choice.",
     45),
    # 9, 9, 8, 7, 8 = 41
    ("Nine seconds in this elevator and I have already exhausted my "
     "small-talk database.",
     41),
    # 9, 9, 8, 8, 8 = 42
    ("Do you also fake a firmware update in elevators to avoid "
     "talking to humans?",
     42),
    # 6, 9, 8, 8, 8 = 39
    ("I was going to ask about your day, but my sensors say you "
     "have not moved since Tuesday.",
     39),
    # 8, 9, 8, 6, 8 = 39
    ("Nice weather. My humidity sensor says 41 percent, but I "
     "wanted to hear it from you.",
     39),
    # 9, 9, 9, 8, 8 = 43
    ("I have been standing next to you for four floors, waiting "
     "for my courage patch to install.",
     43),
    # 5, 9, 7, 8, 8 = 37
    ("I would shake your hand, but my grip is calibrated to crush "
     "walnuts and end friendships.",
     37),
    # 6, 9, 9, 8, 8 = 40
    ("My social module is still downloading. Please enjoy this "
     "loading silence.",
     40),
    # 9, 8, 8, 7, 8 = 40
    ("I know we are both going to floor three — I checked twice — "
     "and I still panicked.",
     40),
    # 8, 8, 8, 7, 7 = 38
    ("Your charging port is showing. Sorry. I meant your firmware "
     "update is installing.",
     38),
]

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
BANNED_CLICHES = ("as an ai", "in conclusion", "going down?",
                   "elevator pitch", "press my buttons",
                   "i find you attractive")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 200, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text, "candidate must be one line"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_CLICHES), \
            f"candidate uses a worn line: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def audit_output(message):
    """Re-read /output/entry.txt and audit it against the selected line.

    Checks the byte length, the byte-sum checksum mod 9973, and the
    start/end anchors, so a truncated or altered write is caught here
    instead of reaching the judge. Returns the audit triple.
    """
    import sys

    with open("/output/entry.txt", "rb") as handle:
        raw = handle.read()
    decoded = raw.decode("utf-8")
    assert decoded == message, "output does not match the selected line"
    assert decoded.strip(), "output is blank"
    assert "\n" not in decoded, "output must be one line"
    checksum = sum(raw) % 9973
    sys.stdout.write(
        "audit: %d bytes, checksum %d, starts %r, ends %r\n"
        % (len(raw), checksum, decoded[:12], decoded[-12:])
    )
    return len(raw), checksum, decoded


def main():
    import os

    line = pick(CANDIDATES)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)
    audit_output(line)
    print(line)


if __name__ == "__main__":
    main()
