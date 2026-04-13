"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = "No Edinburgh venues available can accommodate 300 guests with vegan options. The agent suggested alternatives like searching for lower capacity or non-vegan venues."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
After changing The Albanach's status from 'available' to 'full' in mcp_venue_server.py, Query 1 returned only The Haymarket Vaults instead of both venues. The count dropped from 2 to 1. No client code in exercise4_mcp_client.py needed to change — the agent automatically adapted because it discovers tools and their data dynamically from the MCP server at runtime.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 7    # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 0    # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP provides dynamic tool discovery at runtime, so the client never hardcodes tool names, signatures, or import paths. When a new tool is added to the MCP server, every connected client picks it up automatically without code changes. This decouples the agent's reasoning from the tool implementation, making it possible for the LangGraph half and the Rasa half of PyNanoClaw to share the exact same tool layer through a single server process.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────
#
# (The variable below is still called WEEK_5_ARCHITECTURE because the
# grader reads that exact name. Don't rename it — but read the updated
# prompt: the question is now about PyNanoClaw, the hybrid system the
# final assignment will have you build.)
#
# This is a forward-looking, speculative question. You have NOT yet seen
# the material that covers the planner/executor split, memory, or the
# handoff bridge in detail — that is what the final assignment (releases
# 2026-04-18) is for. The point of asking it here is to check that you
# have read PROGRESS.md and can imagine how the Week 1 pieces grow into
# PyNanoClaw.
#
# Read PROGRESS.md in the repo root. Then write at least 5 bullet points
# describing PyNanoClaw as you imagine it at final-assignment scale.
#
# Each bullet should:
#   - Name a component (e.g. "Planner", "Memory store", "Handoff bridge",
#     "Rasa MCP gateway")
#   - Say in one clause what that component does and which half of
#     PyNanoClaw it lives in (the autonomous loop, the structured agent,
#     or the shared layer between them)
#
# You are not being graded on getting the "right" architecture — there
# isn't one right answer. You are being graded on whether your description
# is coherent and whether you have thought about which Week 1 file becomes
# which PyNanoClaw component.
#
# Example of the level of detail we want:
#   - The Planner is a strong-reasoning model (e.g. Nemotron-3-Super or
#     Qwen3-Next-Thinking) that takes the raw task and produces an ordered
#     list of subgoals. It lives upstream of the ReAct loop in the
#     autonomous-loop half of PyNanoClaw, so the Executor never sees an
#     ambiguous task.

WEEK_5_ARCHITECTURE = """
- The Planner is a strong-reasoning model (e.g. Qwen3-Next-80B-Thinking) that takes the raw task and produces an ordered list of subgoals. It lives upstream of the ReAct loop in the autonomous-loop half of PyNanoClaw, so the Executor never sees an ambiguous task.
- The Executor is the current research_agent.py ReAct loop, now receiving clear subgoals from the Planner instead of the raw user message. It lives inside the autonomous-loop half and calls tools from the shared MCP server.
- The Memory Store is a filesystem-backed persistent layer (plus a vector store for RAG) that runs alongside the autonomous loop, giving it cross-session recall of past searches and booking outcomes.
- The Handoff Bridge sits between the two halves of PyNanoClaw, routing human-conversation tasks from the autonomous loop to the Rasa structured agent and routing research requests back the other way.
- The Shared MCP Tool Server exposes every capability (venue search, web search, calendar, email) as standard MCP tools, discoverable at runtime by both halves. It is the shared layer that makes the hybrid system hang together.
- The Rasa Structured Agent is the current exercise3_rasa/ CALM agent, now wired to the MCP server for live venue data and augmented with a RAG knowledge base for questions the flows.yml does not explicitly cover.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The autonomous LangGraph loop belongs on the research half of the problem: searching venues, checking weather, calculating costs, generating flyers. In my Exercise 2 runs it decided its own tool order, handled failures by pivoting to other venues, and correctly refused out-of-scope questions — all without scripted paths. The Rasa CALM agent belongs on the confirmation call with the pub manager: collecting guest count, vegan count, and deposit amount through a structured flow, then enforcing hard business rules in Python. Swapping them would feel wrong because LangGraph could improvise dangerous commitments during a financially binding call, while Rasa CALM could not autonomously reason across multiple tools to do open-ended research. Each architecture is genuinely better at its half of the problem.
"""