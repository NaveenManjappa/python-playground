import asyncio
from pydantic import BaseModel, Field, EmailStr, field_validator
from pydantic_ai import Agent
from typing import Literal, List, Optional
from datetime import date
from dotenv import load_dotenv
load_dotenv()

class UserInput(BaseModel):
    name: str = Field(..., description="User's name")
    email: EmailStr = Field(..., description="User's email address")
    query: str = Field(..., description="User's query")
    order_id: Optional[str] = Field(None, description="Order ID if available (format: ABC-12345)")
    @field_validator("order_id")
    def validate_order_id(cls, order_id):
        import re
        if order_id is None:
            return order_id
        pattern = r"^[A-Z]{3}-\d{5}$"
        if not re.match(pattern, order_id):
            raise ValueError("order_id must be in format ABC-12345")
        return order_id
    purchase_date: Optional[date] = None

class CustomerQuery(UserInput):
    priority: str = Field(..., description="Priority level: low, medium, high")
    category: Literal['refund_request', 'information_request', 'other'] = Field(..., description="Query category")
    is_complaint: bool = Field(..., description="Whether this is a complaint")
    tags: List[str] = Field(..., description="Relevant keyword tags")

async def main():
    user_input_json = '''
    {
        "name": "Joe User",
        "email": "joe@example.com",
        "query": "When can I expect delivery of the headphones I ordered?",
        "order_id": "ABC-12345",
        "purchase_date": "2025-12-01"
    }
    '''
    valid_data = UserInput.model_validate_json(user_input_json)
    print("user input validated...")

    agent = Agent(model="google-gla:gemini-2.5-flash", output_type=CustomerQuery)
    response = await agent.run(valid_data.model_dump_json())
    print("CustomerQuery generated...")
    print(type(response.output))
    print(response.output.model_dump_json(indent=2))

asyncio.run(main())