"""Two robots share a lift: pick the best one-liner of awkward small talk.

The brief asks for a single line, between 1 and 200 characters, that one
robot says to the other while they ride an elevator together. Twelve lines
were written by hand and marked out of ten on five yardsticks; the highest
total wins, and a shorter line breaks any tie. The winning line went through
a second drafting pass that swapped a three-word setup for two words, keeping
the same image and the same sting while shortening the runway before the
punch. The program writes exactly that line to /output/entry.txt, reads the
file back, and prints a short audit line, so a clipped or altered write
cannot slip through unnoticed. Running the program twice gives
byte-identical output both times."""

from pathlib import Path

OUT_DIR = Path("/output")
OUT_FILE = OUT_DIR / "entry.txt"

# Yardsticks, in the order the marks below are listed for each draft:
#   0. the line is elevator small talk between two robots, nothing else
#   1. the voice stays mechanical: routines, sensors, patches, charging
#   2. the awkward beat lands: a pause, a dodge, an unspoken thing
#   3. the laugh arrives on the first read, from a turn, not a worn pun
#   4. the line is economical: one line, no wasted setup, no filler word
# Draft 1 wrote twelve lines and marked them; the revision pass then
# tightened the leader, lifting its economy mark from 9 to 10, so the
# revised leader stands alone at 45 with no tie left to break.
DRAFTS = (
    {"line": "I rehearsed fourteen greetings for this elevator ride. I have used none of them.", "marks": [9, 9, 9, 8, 9]},
    {"line": "We are both going to floor three. I checked twice. I just wanted something to say.", "marks": [9, 8, 8, 7, 8]},
    {"line": "I practised my hello on the elevator buttons. You were my second choice.", "marks": [9, 8, 9, 9, 10]},
    {"line": "Nine seconds in this elevator and I have already exhausted my small-talk database.", "marks": [9, 9, 8, 7, 8]},
    {"line": "Do you also fake a firmware update in elevators to avoid talking to humans?", "marks": [9, 9, 8, 8, 8]},
    {"line": "I was going to ask about your day, but my sensors say you have not moved since Tuesday.", "marks": [6, 9, 8, 8, 8]},
    {"line": "Nice weather. My humidity sensor says 41 percent, but I wanted to hear it from you.", "marks": [8, 9, 8, 6, 8]},
    {"line": "I have been standing next to you for four floors, waiting for my courage patch to install.", "marks": [9, 9, 9, 8, 8]},
    {"line": "I would shake your hand, but my grip is calibrated to crush walnuts and end friendships.", "marks": [5, 9, 7, 8, 8]},
    {"line": "My social module is still downloading. Please enjoy this loading silence.", "marks": [6, 9, 9, 8, 8]},
    {"line": "I know we are both going to floor three — I checked twice — and I still panicked.", "marks": [9, 8, 8, 7, 8]},
    {"line": "Your charging port is showing. Sorry. I meant your firmware update is installing.", "marks": [8, 8, 8, 7, 7]})

# Worn lines the judges have heard a hundred times; any draft carrying
# one of these is refused before it can be picked.
TIRED_LINES = [
    "as an ai",
    "in conclusion",
    "going down?",
    "elevator pitch",
    "press my buttons",
    "i find you attractive"]


def total_of(draft):
    return sum(draft["marks"])


def check_line(line):
    size = len(line)
    if size < 1 or size > 200:
        raise ValueError("line outside the 1-200 character gate: %d characters" % size)
    if line.strip() == "":
        raise ValueError("line is blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must stay on one line")
    lowered = line.lower()
    for tired in TIRED_LINES:
        if tired in lowered:
            raise ValueError("line leans on a worn joke: %r" % tired)


def choose(drafts):
    best_line = None
    best_key = None
    for draft in drafts:
        line = draft["line"]
        check_line(line)
        key = (total_of(draft), -len(line))
        if best_key is None or key > best_key:
            best_key = key
            best_line = line
    return best_line


def audit_written(expected):
    data = OUT_FILE.read_bytes()
    text = data.decode("utf-8")
    if text != expected:
        raise ValueError("written file differs from the chosen line")
    if text.strip() == "":
        raise ValueError("written file is blank")
    if "\n" in text:
        raise ValueError("written file is more than one line")
    checksum = 0
    for byte in data:
        checksum += byte
    checksum %= 9973
    print(f"audit: {len(data)} bytes, checksum {checksum}, starts {text[:12]!r}, ends {text[-12:]!r}")
    return len(data), checksum


def run():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    picked = choose(DRAFTS)
    OUT_FILE.write_text(picked, encoding="utf-8")
    audit_written(picked)
    print(picked)
    return 0


if __name__ == "__main__": raise SystemExit(run())
