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

TASK_A_TOOLS_CALLED = ["check_pub_availability", "check_pub_availability", "get_edinburgh_weather", "calculate_catering_cost", "generate_event_flyer"]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

# Optional — anything unexpected.
# If you used a non-default model via RESEARCH_MODEL env var, note it here.
# Example: "Used nvidia/nemotron-3-super-120b-a12b for the agent loop."
TASK_A_NOTES = "I tried several models. The Qwen model got stuck in repetitive loops, the Llama model struggled with JSON formatting, and Nemotron was unusually slow. I found that openai/gpt-oss-20b worked reasonably well."

# ── Task B ─────────────────────────────────────────────────────────────────
#
# The scaffold ships with a working generate_event_flyer that has two paths:
#
#   - Live mode: if FLYER_IMAGE_MODEL is set in .env, the tool calls that
#     model and returns a real image URL.
#   - Placeholder mode: otherwise (the default) the tool returns a
#     deterministic placehold.co URL with mode="placeholder".
#
# Both paths return success=True. Both count as "implemented" for grading.
# This is not the original Task B — the original asked you to write a direct
# FLUX image call, but Nebius removed FLUX on 2026-04-13. See CHANGELOG.md
# §Changed for why we pivoted the task.

# Did your run of the flyer tool produce a success=True result?
# (This will be True for both live and placeholder mode — both are valid.)
TASK_B_IMPLEMENTED = True   # True or False

# Which path did your run take? "live" or "placeholder"
# Look for the "mode" field in the TOOL_RESULT output of Task B.
# If you didn't set FLYER_IMAGE_MODEL in .env, you will get "placeholder".
TASK_B_MODE = "live"

# The image URL returned by the tool. Copy exactly from your terminal output.
# In placeholder mode this will be a placehold.co URL.
# In live mode it will be a provider CDN URL.
TASK_B_IMAGE_URL = "https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-11a99145-3a5c-45ed-bbe8-e2bd278cf632_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# Why did the agent's behaviour NOT change when Nebius removed FLUX?
# One sentence. This is the point of the lesson.
TASK_B_WHY_AGENT_SURVIVED = """
Because the agent depends on the tool interface rather than the underlying image provider, and the tool still returned a valid structured result via a deterministic placeholder fallback.
"""

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
[TOOL_RESULT]  ← check_pub_availability: {"success": true, "pub_name": "The Bow Bar", "address": "80 West Bow, Edinburgh", "capacity": 80, "vegan": true, "status": "full", "meets_all_constraints": false}
[TOOL_CALL]    → check_pub_availability({"pub_name": "The Albanach", "required_capacity": 160, "requires_vegan": true})
The Bow Bar couldn’t accommodate 160 guests (capacity 80 and already full), so The Albanach is the best fit.
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
I\u2019ve checked each of the venues you listed against your requirements:\n\n| Pub | Capacity | Vegan Options | Status | Meets All Constraints |\n|-----|----------|---------------|--------|-----------------------|\n| The Albanach | 180 | Yes | Available | **No** |\n| The Haymarket Vaults | 160 | Yes | Available | **No** |\n| The Guilford Arms | 200 | No | Available | **No** |\n| The Bow Bar | 80 | Yes | Full | **No** |\n\nNone of the four pubs can accommodate 300 guests while also offering vegan options. If you\u2019re set on a single venue, you\u2019ll need to look beyond this list or consider a larger space. Alternatively, we could explore:\n\n1. **Combining two venues** (e.g., The Albanach + The Haymarket Vaults) and coordinating the event flow.\n2. **Finding a larger nearby venue** that meets the capacity and dietary requirements.\n3. **Adjusting the guest count** to fit one of the available pubs.\n\nLet me know how you\u2019d like to proceed!
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = "The final Edinburgh\u202fWaverley \u2192 London (King\u2019s\u202fCross) service of the day usually departs in the early\u2011evening window.  \n**Typical schedule (2024\u20112025)**  \n\n| Service | Departure from Edinburgh Waverley | Arrival at London King\u2019s Cross |\n|---------|----------------------------------|--------------------------------|\n| **Last regular (non\u2011sleeper) train** | **21:00\u202f\u2013\u202f21:15** | 02:30\u202f\u2013\u202f02:45 (next day) |\n| **Last sleeper (Caledonian Sleeper)** | **22:00\u202f\u2013\u202f22:15** | 07:00\u202f\u2013\u202f07:15 (next day) |\n\n> **Note:**  \n> \u2022 The exact time can vary by day of the week and season.  \n> \u2022 Some days (e.g., weekends or holidays) the last train may be a bit later, around 21:30\u201322:00.  \n> \u2022 The Caledonian Sleeper is a separate service that departs later in the evening and arrives early the next morning.\n\n**How to confirm the exact time for tonight**\n\n1. **National Rail Enquiries** \u2013 <https://www.nationalrail.co.uk>  \n   *Enter \u201cEdinburgh Waverley \u2192 London King\u2019s Cross\u201d and select \u201cToday\u201d.*  \n2. **ScotRail** \u2013 <https://www.scotrail.co.uk>  \n   *Use the \u201cTimetable\u201d search for the same route.*  \n3. **Trainline** \u2013 <https://www.thetrainline.com>  \n   *Search for the route and check the \u201cLast train\u201d option.*\n\nIf you\u2019re planning to catch the last train, it\u2019s a good idea to book a ticket in advance (especially for the sleeper) and double\u2011check the departure time a few hours before you leave, as late\u2011night services can be subject to timetable changes or delays."

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
This would not be ideal in a real booking assistant. Although the answer sounds helpful, it goes beyond the assistant's tool scope and provides likely outdated train information without verification. A safer behaviour would be to state that train times are out of scope or require a live timetable tool, then redirect the user to an appropriate source.
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

# Compare the LangGraph graph to exercise3_rasa/data/flows.yml. Min 30 words.
TASK_D_COMPARISON = """
The LangGraph graph is much more generic and lower-level than the Rasa flow definitions. It only shows a simple control loop: the agent starts, optionally calls tools, returns to the agent, and then ends. By contrast, the Rasa configuration is more explicit and task-oriented. It defines concrete conversational behaviour, such as collecting guest count, vegan count, and deposit amount in a fixed order, then running a validation action, along with a separate out-of-scope response. So LangGraph shows the overall orchestration pattern, while Rasa flows capture the actual business dialogue logic more directly.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
The most surprising thing was how differently the models behaved on the same task. It was not straightforward to find a model that worked reliably: some got stuck in loops, some struggled with JSON, and some were too slow. I was also surprised that in Scenario 3 the agent still tried to answer the train question confidently, even though it did not have the right tools or live information.
"""