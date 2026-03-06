"""
main.py - Customer Support Pipeline
====================================

This is the entry point that ties everything together. It runs the full
pipeline end-to-end:

  Step 1  Validate the raw user JSON           → UserInput
  Step 2  Enrich with an LLM (Gemini)          → CustomerQuery
  Step 3  Ask GPT-4o which tools to call        → tool_calls
  Step 4  Execute the requested tools           → tool_outputs
  Step 5  Generate a structured support ticket  → SupportTicket
          using Claude (Anthropic)

Usage:
    python main.py

Make sure you have a .env file with the following keys:
    OPENAI_API_KEY=...
    ANTHROPIC_API_KEY=...
    GOOGLE_API_KEY=...       (for Gemini via pydantic-ai)
"""

import asyncio
import json

# Load API keys from .env before importing anything that needs them
from dotenv import load_dotenv

load_dotenv()

from agents import (
    validate_user_input,
    create_customer_query,
    decide_next_action_with_tools,
    get_tool_outputs,
    generate_structured_support_ticket,
)


# ---------------------------------------------------------------------------
# Pipeline function
# ---------------------------------------------------------------------------
async def run_pipeline(user_json: str) -> None:
    """Execute the full customer-support pipeline for a single user query."""

    print("=" * 60)
    print("STEP 1: Validate user input")
    print("=" * 60)
    valid_input = validate_user_input(user_json)
    if valid_input is None:
        print("Pipeline aborted — invalid input.")
        return
    valid_user_json = valid_input.model_dump_json()
    print(f"  Validated JSON: {valid_user_json}\n")

    # ------------------------------------------------------------------
    print("=" * 60)
    print("STEP 2: Create CustomerQuery via Gemini (Pydantic AI)")
    print("=" * 60)
    customer_query = await create_customer_query(valid_user_json)
    print(f"  Type:     {type(customer_query).__name__}")
    print(f"  Priority: {customer_query.priority}")
    print(f"  Category: {customer_query.category}")
    print(f"  Tags:     {customer_query.tags}\n")

    # ------------------------------------------------------------------
    print("=" * 60)
    print("STEP 3: Decide next action via GPT-4o (with tool calling)")
    print("=" * 60)
    message, tool_calls, messages = decide_next_action_with_tools(customer_query)
    if tool_calls:
        print(f"  LLM requested {len(tool_calls)} tool call(s).")
    else:
        print("  LLM did not request any tool calls.")
    print()

    # ------------------------------------------------------------------
    print("=" * 60)
    print("STEP 4: Execute requested tools")
    print("=" * 60)
    tool_outputs = get_tool_outputs(tool_calls)
    print(f"  Tool outputs: {json.dumps(tool_outputs, indent=2)}\n")

    # ------------------------------------------------------------------
    print("=" * 60)
    print("STEP 5: Generate SupportTicket via Claude (Anthropic)")
    print("=" * 60)
    support_ticket = generate_structured_support_ticket(
        customer_query, message, tool_outputs
    )
    print(support_ticket.model_dump_json(indent=2))


# ---------------------------------------------------------------------------
# Example user inputs
# ---------------------------------------------------------------------------
# Example 1: A delivery/order-status question
user_json_1 = """
{
    "name": "Joe User",
    "email": "joe@example.com",
    "query": "When can I expect delivery of the headphones I ordered?",
    "order_id": "ABC-12345",
    "purchase_date": "2025-12-01"
}
"""

# Example 2: A complaint without a specific order ID
user_json_2 = """
{
    "name": "Joe User",
    "email": "joe@example.com",
    "query": "I'm really not happy with this product I bought",
    "order_id": "QWE-34567",
    "purchase_date": null
}
"""


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------
async def main():
    """Run the pipeline for both example inputs."""

    print("\n>>> PIPELINE RUN 1\n")
    await run_pipeline(user_json_1)

    print("\n\n>>> PIPELINE RUN 2\n")
    await run_pipeline(user_json_2)


if __name__ == "__main__":
    # asyncio.run() works perfectly in a normal Python script — no
    # nest_asyncio hacks needed outside of Jupyter notebooks.
    asyncio.run(main())
