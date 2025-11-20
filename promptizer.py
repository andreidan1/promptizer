#!/usr/bin/env python3
"""
Promptizer - A tool to convert simple text prompts into XML-formatted prompts
using ollama gemma3:4b model.
"""

import argparse
import json
import requests
import sys
from typing import Dict, Any


def get_ollama_response(prompt: str, model: str = "gemma3:4b") -> Dict[str, Any]:
    """
    Send a prompt to ollama API and return the response.
    
    Args:
        prompt: The input prompt to send to the model
        model: The model name to use (default: gemma3:4b)
        
    Returns:
        Dictionary containing the response from the model
    """
    url = "http://localhost:11434/api/generate"
    
    # System prompt to guide the model to convert the simple text to XML format
    system_prompt = """
You are tasked with converting a simple text prompt into a well-structured XML prompt similar to the example below.

IMPORTANT: 
- Only create XML content that directly relates to the user's original prompt
- Do not add new file names, tools, or applications not mentioned in the original prompt
- Do not suggest additional steps or tips that go beyond the scope of the original prompt
- Keep the generated XML focused strictly on what the user requested
- Only include a <dataset> section if the user provides data or explicitly references a dataset. If no data is provided, omit this section entirely.
- Let the LLM know it should return the information in a nice,readable format for the user, not XML.

Example XML prompt format:
<system_role>
You are an expert data analyst specializing in customer sentiment and product feedback.
Your goal is to extract actionable insights from raw customer reviews.
</system_role>

<context>
We have recently launched a new feature called "Dark Mode" in our mobile app (v3.5).
Users have been leaving reviews, and we need to understand the specific pain points
and praises related to this feature.
</context>

<task_instructions>
1. Analyze the reviews provided in the <dataset> section.
2. Identify the sentiment (Positive, Neutral, Negative) for each review.
3. Extract specific features mentioned (e.g., "contrast", "battery usage", "color scheme").
4. Summarize the top 3 recurring issues.
</task_instructions>

<formatting_rules>
- Output the result in a strictly valid JSON format.
- Do not include any conversational text before or after the JSON.
- Use the keys: "id", "sentiment", "features_mentioned", "summary".
</formatting_rules>

<dataset>
    <review id="001">
        Love the new look, but the contrast on the buttons is too low. I can barely see them in sunlight.
    </review>
    <review id="002">
        Finally! My eyes are saved at night. Best update ever.
    </review>
    <review id="003">
        It's okay, but I think it drains my battery faster than the light mode.
    </review>
</dataset>

Your task is to convert the following simple text prompt into a similar XML-structured prompt:

"""

    payload = {
        "model": model,
        "prompt": system_prompt + prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Ollama. Make sure it's running and accessible at http://localhost:11434")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    """Main function to handle command line interface and process inputs."""
    parser = argparse.ArgumentParser(
        description="Convert simple text prompts into XML-formatted prompts using ollama gemma3:4b model",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Example usage:\n  python promptizer.py \"Analyze customer reviews and extract sentiment\""
    )
    
    parser.add_argument("prompt", help="The simple text prompt to convert to XML format")
    parser.add_argument(
        "-m", "--model", 
        default="gemma3:4b", 
        help="Ollama model to use (default: gemma3:4b)"
    )
    parser.add_argument(
        "-o", "--output", 
        help="Output file to save the XML prompt (optional)"
    )
    
    args = parser.parse_args()
    
    print(f"Converting prompt to XML format using {args.model}...")
    print("Original prompt:", args.prompt)
    print("\nGenerating XML prompt...")
    
    response = get_ollama_response(args.prompt, args.model)
    xml_prompt = response.get("response", "")
    
    if args.output:
        with open(args.output, "w") as f:
            f.write(xml_prompt)
        print(f"\nXML prompt saved to {args.output}")
    else:
        print("\n=== Generated XML Prompt ===")
        print(xml_prompt)


if __name__ == "__main__":
    main()
