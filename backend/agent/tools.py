# backend/agent/tools.py
from google.genai import types

TOOLS = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="search_trademark",
            description="Search trademark databases for existing marks similar to the given name.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "name": types.Schema(type=types.Type.STRING, description="Brand name to search"),
                    "jurisdiction": types.Schema(type=types.Type.STRING, description="Country code, default IN"),
                },
                required=["name"]
            )
        ),
        types.FunctionDeclaration(
            name="check_similarity",
            description="Check phonetic and semantic similarity of a name against known marks. Returns risk_score 0-1.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "name": types.Schema(type=types.Type.STRING),
                },
                required=["name"]
            )
        ),
        types.FunctionDeclaration(
            name="get_nice_class",
            description="Given a product or service description, return the correct Nice classification class(es).",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "description": types.Schema(type=types.Type.STRING),
                },
                required=["description"]
            )
        ),
        types.FunctionDeclaration(
            name="draft_application",
            description="Generate a trademark application draft given the mark name, Nice class, and description.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "name": types.Schema(type=types.Type.STRING),
                    "nice_class": types.Schema(type=types.Type.INTEGER),
                    "description": types.Schema(type=types.Type.STRING),
                },
                required=["name", "nice_class", "description"]
            )
        ),
    ]
)


def execute_tool(name: str, inputs: dict) -> dict:
    if name == "search_trademark":
        return {
            "matches": [
                {"mark": "ZOMATO", "class": 43, "status": "Registered", "owner": "Zomato Ltd"}
            ],
            "total_found": 1,
            "jurisdiction": inputs.get("jurisdiction", "IN")
        }

    if name == "check_similarity":
        return {
            "risk_score": 0.82,
            "phonetic_matches": ["ZOMATO", "ZOMATTO"],
            "semantic_matches": ["food delivery platform"],
            "verdict": "High similarity detected"
        }

    if name == "get_nice_class":
        return {
            "classes": [43],
            "primary": 43,
            "reasoning": "Class 43 covers restaurant and food delivery services"
        }

    if name == "draft_application":
        return {
            "draft": f"""
TRADEMARK APPLICATION DRAFT
============================
Mark: {inputs['name']}
Nice Class: {inputs['nice_class']}
Description: {inputs['description']}
Jurisdiction: India (IP India)

[Mock draft — replace with real template]
            """.strip()
        }

    return {"error": f"Unknown tool: {name}"}