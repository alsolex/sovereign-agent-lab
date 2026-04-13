"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  calling to confirm a booking                                                                                                                                                                          
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                                                                                                                                            
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan                                                                                                                                                                                   
Sorry, it seems the value you provided `about 50` is not a valid number. Please provide a valid number in your response.
And how many of those guests will need vegan meals?
Your input ->  50                                                                                                                                                                                                    
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £200 deposit                                                                                                                                                                                          
Sorry, it seems the value you provided `£200 deposit` is not a valid number. Please provide a valid number in your response.
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  200                                                                                                                                                                                                   
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  160 guests
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £500 deposit                                                                                                                                                                                          
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300."   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  160 guests
And how many of those guests will need vegan meals?
Your input ->  can you arrange parking for the speakers?                                                                                                                                                             
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
CALM recognised that the parking request was outside the scope of the booking-confirmation flow. It clearly stated that it could only help with confirming tonight's venue booking, directed the caller to contact the organiser for anything else, and then asked whether they wanted to continue with the booking process.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
In Exercise 2, LangGraph tried to respond to the user's request even though it did not have the right tools or reliable information, which led to an ungrounded answer. By contrast, Rasa CALM stayed within its defined scope, acknowledged the limitation clearly, and redirected the user appropriately. For this use case, CALM was more controlled and dependable, even if it was less flexible.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I enabled the four commented lines that add the time-based escalation guard and then tested the flow late in the evening, when the cutoff condition should trigger. The agent escalated the booking as expected and gave the correct reason: it is past 16:45 — insufficient time to process the confirmation before the 5 PM deadline.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
Rasa Pro CALM simplifies the system by letting the LLM handle the messy part of natural language understanding and slot extraction. This reduces the need for regex, intent examples, and hand-written dialogue rules. Python is still needed for business rules such as deposit limits and cutoff times, because those checks must remain deterministic and consistent. The gain is faster development and more natural conversations; the cost is less transparency and direct control over how values are extracted.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
Rasa CALM still requires more setup than LangGraph, but that setup buys structure and control. The agent stays within defined flows and cannot freely improvise responses or call tools that were not explicitly configured. For a booking-confirmation use case, this is mostly a strength rather than a weakness, because consistency, scope control, and safe escalation matter more than flexibility.
"""
