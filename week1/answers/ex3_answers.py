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
Your input → I'm calling to confirm a booking for tonight
Bot → I'd be happy to help with the booking confirmation. How many guests are expected?
Your input → 160 guests
Bot → And how many of those guests will need vegan meals?
Your input → about 50 need vegan
Bot → What deposit amount has been agreed?
Your input → 200 pounds deposit
Bot → Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
"""
CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

CONVERSATION_2_TRACE = """
Your input → I'm calling to confirm a booking
Bot → I'd be happy to help with the booking confirmation. How many guests are expected?
Your input → 160 guests
Bot → And how many of those guests will need vegan meals?
Your input → about 50 need vegan
Bot → What deposit amount has been agreed?
Your input → 500 pound deposit
Bot → I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
"""
CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "a deposit of £500 exceeds the organiser's authorised limit of £300"

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input → I'm calling to confirm a booking
Bot → I'd be happy to help with the booking confirmation. How many guests are expected?
Your input → can you arrange parking for the speakers?
Bot → I'm not able to help with parking arrangements. I can only assist with booking confirmations. How many guests are expected for tonight's event?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
CALM recognised the parking request as out of scope and did not attempt to answer it. Instead it acknowledged it could not help with parking, restated its role as a booking confirmation agent, and prompted the manager again for the guest count to continue the booking flow.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
Rasa CALM handled the out-of-scope request by politely declining and steering the conversation back to the booking flow it was designed for. It stayed strictly within its defined flows.yml boundaries. LangGraph, by contrast, honestly said it had no train-schedule tool but then offered alternative suggestions and external URLs. CALM is more controlled and narrowly scoped, whereas LangGraph is more flexible but also more prone to improvising beyond its tool boundaries.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I uncommented the cutoff guard block in actions.py, temporarily changed the condition to 'if True' to force escalation, ran a booking conversation through rasa shell, and verified the bot escalated immediately with the deadline message. Then I reverted the test condition back to the real time check.
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
In CALM the LLM handles natural language understanding and slot extraction that previously required hand-written regex in Python FormValidationAction classes. Python still handles deterministic business rules like deposit limits and capacity checks because those decisions must be auditable and non-negotiable. The old approach gave more explicit control over parsing but required far more boilerplate code.
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
The extra setup cost of Rasa CALM — config.yml, domain.yml, flows.yml, endpoints.yml, rasa train, two terminal processes, and a licence key — buys you deterministic, auditable behaviour that LangGraph cannot guarantee. The CALM agent cannot improvise responses outside its defined flows or call tools not specified in flows.yml. For the confirmation use case this is a feature, not a limitation: when every word could commit money or create a legal obligation, you want the agent's behaviour to be predictable and inspectable, not creative.
"""
