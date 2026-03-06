"""
models.py - Pydantic Models for the Customer Support Pipeline
=============================================================

This file defines all the data models (schemas) used throughout the pipeline.
Pydantic models enforce data validation and type safety, ensuring that
the data flowing through the system is always in the expected format.

The model hierarchy:
  UserInput          - Raw user input with basic validation
  CustomerQuery      - Enriched version of UserInput (adds priority, category, etc.)
  SupportTicket      - Final output combining all gathered information

Supporting models:
  FAQLookupArgs      - Input schema for the FAQ lookup tool
  CheckOrderStatusArgs - Input schema for the order status tool
  OrderDetails       - Structured order information returned by the order tool
"""

import re
from typing import Literal, List, Optional
from datetime import datetime, date
from pydantic import BaseModel, Field, EmailStr, field_validator


# ---------------------------------------------------------------------------
# 1. UserInput - Validates the raw JSON data coming from a customer
# ---------------------------------------------------------------------------
class UserInput(BaseModel):
    """Represents the initial input from a customer.

    Fields:
        name:          Customer's full name (required).
        email:         Customer's email, validated by Pydantic's EmailStr.
        query:         The free-text question or issue from the customer.
        order_id:      Optional order ID in the format ABC-12345.
        purchase_date: Optional date of purchase.
    """

    name: str = Field(..., description="User's name")
    email: EmailStr = Field(..., description="User's email address")
    query: str = Field(..., description="User's query")
    order_id: Optional[str] = Field(
        None,
        description="Order ID if available (format: ABC-12345)",
    )
    purchase_date: Optional[date] = None

    # Custom validator: ensures order_id matches the pattern ABC-12345
    @field_validator("order_id")
    def validate_order_id(cls, order_id):
        if order_id is None:
            return order_id
        pattern = r"^[A-Z]{3}-\d{5}$"
        if not re.match(pattern, order_id):
            raise ValueError(
                "order_id must be in format ABC-12345 "
                "(3 uppercase letters, dash, 5 digits)"
            )
        return order_id


# ---------------------------------------------------------------------------
# 2. CustomerQuery - An enriched version of UserInput produced by an LLM
# ---------------------------------------------------------------------------
class CustomerQuery(UserInput):
    """Extends UserInput with fields that an LLM infers from the query text.

    Additional fields:
        priority:     "low", "medium", or "high".
        category:     One of 'refund_request', 'information_request', 'other'.
        is_complaint: Whether the query is a complaint.
        tags:         Keyword tags relevant to the query.
    """

    priority: str = Field(..., description="Priority level: low, medium, high")
    category: Literal["refund_request", "information_request", "other"] = Field(
        ..., description="Query category"
    )
    is_complaint: bool = Field(..., description="Whether this is a complaint")
    tags: List[str] = Field(..., description="Relevant keyword tags")


# ---------------------------------------------------------------------------
# 3. Tool-Input Models - Define the expected inputs for each tool
# ---------------------------------------------------------------------------
class FAQLookupArgs(BaseModel):
    """Input schema for the FAQ lookup tool.

    Fields:
        query: The customer's original question.
        tags:  Keywords extracted from the customer query.
    """

    query: str = Field(..., description="User's query")
    tags: List[str] = Field(
        ..., description="Relevant keyword tags from the customer query"
    )


class CheckOrderStatusArgs(BaseModel):
    """Input schema for the order-status lookup tool.

    Fields:
        order_id: Must match the ABC-12345 format.
        email:    Customer's email for verification.
    """

    order_id: str = Field(..., description="Customer's order ID (format: ABC-12345)")
    email: EmailStr = Field(..., description="Customer's email address")

    @field_validator("order_id")
    def validate_order_id(cls, order_id):
        pattern = r"^[A-Z]{3}-\d{5}$"
        if not re.match(pattern, order_id):
            raise ValueError(
                "order_id must be in format ABC-12345 "
                "(3 uppercase letters, dash, 5 digits)"
            )
        return order_id


# ---------------------------------------------------------------------------
# 4. OrderDetails & SupportTicket - Final structured outputs
# ---------------------------------------------------------------------------
class OrderDetails(BaseModel):
    """Structured representation of an order lookup result."""

    status: str
    estimated_delivery: str
    note: str


class SupportTicket(CustomerQuery):
    """The final support ticket combining all pipeline information.

    Additional fields beyond CustomerQuery:
        recommended_next_action: What the support system should do next.
        order_details:           Filled in if an order lookup was performed.
        faq_response:            Filled in if an FAQ lookup was performed.
        creation_date:           Timestamp when the ticket was created.
    """

    recommended_next_action: Literal[
        "escalate_to_agent",
        "send_faq_response",
        "send_order_status",
        "no_action_needed",
    ] = Field(..., description="LLM's recommended next action for support")
    order_details: Optional[OrderDetails] = Field(
        None, description="Order details if action is send_order_status"
    )
    faq_response: Optional[str] = Field(
        None, description="FAQ response if action is send_faq_response"
    )
    creation_date: datetime = Field(
        ..., description="Date and time the ticket was created"
    )
