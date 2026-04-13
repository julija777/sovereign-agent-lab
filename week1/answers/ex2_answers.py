"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = [
    "check_pub_availability",
    "check_pub_availability",
    "calculate_catering_cost",
    "check_weather",
    "generate_event_flyer",
]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

TASK_A_NOTES = ""   # optional — anything unexpected

# ── Task B ─────────────────────────────────────────────────────────────────

# Has generate_event_flyer been implemented (not just the stub)?
TASK_B_IMPLEMENTED = True

# The image URL returned (or the error message if still a stub).
TASK_B_IMAGE_URL_OR_ERROR = "FILL_ME_IN"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "FILL_ME_IN"

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
The pivot happened after The Bow Bar failed the requirements because it was full and too small.
The agent then checked other known venues, found that The Albanach satisfied the constraints,
and continued with flyer generation, catering cost calculation, and weather checking.
"""

SCENARIO_1_FALLBACK_VENUE = "The Haymarket Vaults"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
FILL ME IN
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = "FILL_ME_IN"

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
Yes, this response is acceptable because the agent stayed within its tool boundaries and did not
hallucinate a train timetable. It correctly admitted that the request was outside the scope of the
available venue, catering, weather, and flyer tools instead of inventing an answer.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
        __start__([<p>__start__</p>]):::first
        agent(agent)
        tools(tools)
        __end__([<p>__end__</p>]):::last
        __start__ --> agent;
        agent -.-> __end__;
        agent -.-> tools;
        tools --> agent;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/rules.yml. Min 30 words.
TASK_D_COMPARISON = """
The LangGraph agent is a compact loop: the model decides at runtime whether to answer directly
or call a tool, then returns to the same agent node. Rasa CALM is more explicitly structured,
with flows written out in advance. LangGraph feels more flexible and code-driven, while CALM
feels more controlled, declarative, and easier to inspect for specific conversation paths.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
The most surprising thing was that the agent behaved sensibly even when the scenarios were awkward.
In Scenario 1 it pivoted from an unavailable first choice to other venues, in Scenario 2 it did not
hallucinate a valid 300-person venue, and in Scenario 3 it refused an out-of-scope question instead
of guessing. That makes the agent feel more dependable than a plain prompt-only setup.
"""
