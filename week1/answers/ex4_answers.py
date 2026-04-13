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
QUERY_2_FINAL_ANSWER  = "No venues were found that can accommodate 300 people with vegan options. Would you like to adjust the capacity requirement or check for other dietary preferences?"

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
After changing one venue entry in mcp_venue_server.py and rerunning the client, the tool result changed from 2 matching venues to 1. The important point is that only the server-side venue data needed updating. No changes were required in week1/exercise4_mcp_client.py or in the agent logic, because the LangGraph client simply consumed the updated MCP tool output.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 202   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 48   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
In the hardcoded version, the tool logic lives directly inside the local Python tool layer, so the agent is tightly coupled to that implementation. In the MCP version, the client contains only a small bridge for discovery and calling, while the real tool implementation lives on the server side. That means tools can be updated once and then reused by multiple consumers, including both a LangGraph agent and a Rasa action, without duplicating the business logic.
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
- The Planner lives in the autonomous-loop half and turns a raw task into clearer subgoals before execution starts.
- The Executor grows out of research_agent.py and lives in the autonomous-loop half, where it runs the ReAct loop and carries out the research work.
- The Shared MCP Tool Server grows out of mcp_venue_server.py and lives in the shared layer, exposing tools such as venue lookups, web search, calendar access, and email.
- The Structured Agent grows out of exercise3_rasa/ and lives in the structured-agent half, where it handles auditable business conversations with explicit flows and rules.
- The Handoff Bridge lives in the shared layer and routes work between the autonomous loop and the structured agent depending on whether the task needs research or a controlled human conversation.
- The Memory layer lives alongside the main system and stores useful past context so PyNanoClaw can avoid repeating work and make better decisions.
- The Observability layer lives across the whole system and records traces, failures, and costs so the hybrid agent can be inspected and debugged.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The LangGraph agent is better suited to the research phase because it can handle open-ended, multi-step reasoning such as finding candidate venues, comparing them, and then fetching the details of the best match without relying on a rigid predefined flow. For the final call, Rasa CALM is the better fit because it enforces explicit business rules, such as the 16:45 cutoff, in a predictable and auditable way. Swapping them would feel wrong because you would lose the flexibility needed for exploratory research and the reliability needed for a high-stakes booking conversation.
"""