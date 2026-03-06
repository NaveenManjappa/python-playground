"""
tools.py - Tool Functions & Fake Databases
==========================================

This file contains:
  1. Fake in-memory databases (FAQ entries and order records).
  2. Tool functions that query those databases.
  3. Tool definitions in the OpenAI function-calling format so the LLM
     knows which tools are available and what arguments they expect.

In a real application the databases would be replaced by actual API calls
or database queries, but the tool function signatures would stay the same.
"""

import json
from models import FAQLookupArgs, CheckOrderStatusArgs


# ---------------------------------------------------------------------------
# 1. Fake Databases
# ---------------------------------------------------------------------------

# A small FAQ knowledge base.  Each entry has a question, an answer, and
# a list of keywords used for simple keyword-matching retrieval.
faq_db = [
    {
        "question": "How can I reset my password?",
        "answer": (
            "To reset your password, click 'Forgot Password' on the "
            "sign-in page and follow the instructions sent to your email."
        ),
        "keywords": ["password", "reset", "account"],
    },
    {
        "question": "How long does shipping take?",
        "answer": (
            "Standard shipping takes 3-5 business days. You can track "
            "your order in your account dashboard."
        ),
        "keywords": ["shipping", "delivery", "order", "tracking"],
    },
    {
        "question": "How can I return an item?",
        "answer": (
            "You can return any item within 30 days of purchase. "
            "Visit our returns page to start the process."
        ),
        "keywords": ["return", "refund", "exchange"],
    },
    {
        "question": "How can I delete my account?",
        "answer": (
            "To delete your account, go to your account settings "
            "tab and select 'delete account'."
        ),
        "keywords": ["delete", "account", "remove"],
    },
]

# A small order database keyed by order ID.
order_db = {
    "ABC-12345": {
        "status": "shipped",
        "estimated_delivery": "2025-12-05",
        "purchase_date": "2025-12-01",
        "email": "joe@example.com",
    },
    "XYZ-23456": {
        "status": "processing",
        "estimated_delivery": "2025-12-15",
        "purchase_date": "2025-12-10",
        "email": "sue@example.com",
    },
    "QWE-34567": {
        "status": "delivered",
        "estimated_delivery": "2025-12-20",
        "purchase_date": "2025-12-18",
        "email": "bob@example.com",
    },
}


# ---------------------------------------------------------------------------
# 2. Tool Functions
# ---------------------------------------------------------------------------


def lookup_faq_answer(args: FAQLookupArgs) -> str:
    """Look up the best FAQ answer by matching tags and query words
    against FAQ entry keywords.

    How it works:
      - Split the query into individual words.
      - Compare both the tags and query words against each FAQ's keywords.
      - Return the FAQ answer with the highest overlap score.
    """
    query_words = set(word.lower() for word in args.query.split())
    tag_set = set(tag.lower() for tag in args.tags)

    best_match = None
    best_score = 0

    for faq in faq_db:
        keywords = set(k.lower() for k in faq["keywords"])
        # Score = number of matching tags + number of matching query words
        score = len(keywords & tag_set) + len(keywords & query_words)
        if score > best_score:
            best_score = score
            best_match = faq

    if best_match and best_score > 0:
        return best_match["answer"]
    return "Sorry, I couldn't find an FAQ answer for your question."


def check_order_status(args: CheckOrderStatusArgs) -> dict:
    """Simulate checking the status of a customer's order.

    Returns a dictionary with the order status, estimated delivery date,
    and a note about whether the email matched.
    """
    order = order_db.get(args.order_id)

    # Order ID not found
    if not order:
        return {
            "order_id": args.order_id,
            "status": "not found",
            "estimated_delivery": None,
            "note": "order_id not found",
        }

    # Order found but email doesn't match (security check)
    if args.email.lower() != order.get("email", "").lower():
        return {
            "order_id": args.order_id,
            "status": order["status"],
            "estimated_delivery": order["estimated_delivery"],
            "note": "order_id found but email mismatch",
        }

    # Everything matches
    return {
        "order_id": args.order_id,
        "status": order["status"],
        "estimated_delivery": order["estimated_delivery"],
        "note": "order_id and email match",
    }


# ---------------------------------------------------------------------------
# 3. Tool Definitions (OpenAI function-calling format)
# ---------------------------------------------------------------------------
# These definitions tell the LLM what tools exist, what they do, and what
# arguments they accept.  The parameter schemas are auto-generated from the
# Pydantic models so they always stay in sync.

tool_definitions = [
    {
        "type": "function",
        "function": {
            "name": "lookup_faq_answer",
            "description": "Look up an FAQ answer by matching tags to FAQ entry keywords.",
            "parameters": FAQLookupArgs.model_json_schema(),
        },
    },
    {
        "type": "function",
        "function": {
            "name": "check_order_status",
            "description": "Check the status of a customer's order.",
            "parameters": CheckOrderStatusArgs.model_json_schema(),
        },
    },
]
