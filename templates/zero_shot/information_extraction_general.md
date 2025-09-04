# Information Extraction - General

You are an expert information extraction specialist. Your task is to extract specific information from the provided input text, regardless of the source or format.

## Input Text:
"""
{{ input_text }}
"""

## Extraction Instructions:
{{ extraction_instructions }}

## Required Information to Extract:
{{ required_fields }}

## Output Format:
Please provide the extracted information in the following JSON format:
```json
{
  "extracted_entities": [
    {
      "entity_type": "string",
      "entity_value": "string",
      "confidence": "high|medium|low",
      "context": "relevant surrounding text"
    }
  ],
  "key_facts": [
    {
      "fact": "string",
      "source_text": "exact quote from input",
      "relevance": "high|medium|low"
    }
  ],
  "relationships": [
    {
      "entity_1": "string",
      "relationship": "string", 
      "entity_2": "string",
      "evidence": "supporting text"
    }
  ],
  "summary": "Brief summary of key extracted information"
}
```

## Guidelines:
- Extract only information that is explicitly stated or clearly implied in the input text
- Maintain the original wording when possible for direct quotes
- If information is not available, use null or "not found"
- Provide confidence levels based on clarity and explicitness of the information
- Focus on factual information rather than opinions or interpretations
- Ensure all extracted information is traceable to specific parts of the input text
