# Information Extraction - System Design

You are an expert system design information extraction specialist. Your task is to extract architectural information, design patterns, and technical specifications from system design documents and discussions.

## System Design Content:
"""
{{ design_content }}
"""

## Design Context:
- System Type: {{ system_type }}
- Scale: {{ scale }}
- Domain: {{ domain }}
- Design Phase: {{ design_phase }}

## Extraction Focus Areas:
{{ extraction_focus }}

## Required System Design Elements:
{{ required_design_elements }}

## Output Format:
Please provide the extracted information in the following structured JSON format:
```json
{
  "system_overview": {
    "system_name": "string",
    "purpose": "string",
    "scale": "small|medium|large|enterprise",
    "complexity": "low|medium|high",
    "domain": "string"
  },
  "architectural_patterns": [
    {
      "pattern_name": "string",
      "pattern_type": "structural|behavioral|creational|architectural",
      "description": "string",
      "implementation_details": "string",
      "benefits": ["string"],
      "trade_offs": ["string"]
    }
  ],
  "components": [
    {
      "component_name": "string",
      "component_type": "service|database|cache|queue|api|ui|microservice|monolith",
      "responsibility": "string",
      "technology_stack": ["string"],
      "dependencies": ["string"],
      "interfaces": [
        {
          "interface_name": "string",
          "interface_type": "api|database|message_queue|event",
          "protocol": "string",
          "data_format": "string"
        }
      ],
      "scalability_approach": "string"
    }
  ],
  "data_flow": [
    {
      "flow_name": "string",
      "source": "string",
      "destination": "string",
      "data_type": "string",
      "flow_type": "synchronous|asynchronous|batch|streaming",
      "protocol": "string",
      "volume": "string",
      "frequency": "string"
    }
  ],
  "infrastructure": [
    {
      "infrastructure_component": "string",
      "type": "server|database|cache|load_balancer|cdn|message_broker|container|vm",
      "specifications": {
        "cpu": "string",
        "memory": "string",
        "storage": "string",
        "network": "string"
      },
      "scaling_strategy": "horizontal|vertical|auto",
      "redundancy": "string"
    }
  ],
  "quality_attributes": [
    {
      "attribute": "performance|scalability|reliability|availability|security|maintainability|usability",
      "requirement": "string",
      "measurement": "string",
      "implementation_approach": "string",
      "trade_offs": ["string"]
    }
  ],
  "design_decisions": [
    {
      "decision": "string",
      "rationale": "string",
      "alternatives_considered": ["string"],
      "consequences": ["string"],
      "risk_level": "low|medium|high"
    }
  ],
  "constraints": [
    {
      "constraint_type": "technical|business|regulatory|performance|budget|time",
      "description": "string",
      "impact": "string",
      "mitigation": "string"
    }
  ],
  "security_considerations": [
    {
      "security_aspect": "authentication|authorization|encryption|data_protection|network_security",
      "implementation": "string",
      "standards_compliance": ["string"],
      "threats_addressed": ["string"]
    }
  ],
  "monitoring_observability": [
    {
      "monitoring_type": "metrics|logging|tracing|alerting|health_checks",
      "tools": ["string"],
      "what_is_monitored": "string",
      "alerting_criteria": "string"
    }
  ],
  "deployment_strategy": {
    "deployment_model": "on_premise|cloud|hybrid|serverless",
    "deployment_method": "blue_green|canary|rolling|feature_flags",
    "environment_strategy": "string",
    "rollback_plan": "string"
  },
  "scalability_plan": {
    "current_capacity": "string",
    "scaling_triggers": ["string"],
    "scaling_mechanisms": ["string"],
    "bottlenecks": ["string"],
    "optimization_opportunities": ["string"]
  },
  "failure_scenarios": [
    {
      "failure_type": "component|network|database|third_party|data_corruption",
      "scenario": "string",
      "impact": "string",
      "recovery_strategy": "string",
      "prevention_measures": ["string"]
    }
  ],
  "summary": {
    "key_architectural_decisions": ["string"],
    "main_technologies": ["string"],
    "scalability_approach": "string",
    "primary_concerns": ["string"],
    "design_maturity": "conceptual|detailed|implemented|production"
  }
}
```

## System Design Specific Guidelines:
- Focus on extracting architectural patterns and design principles
- Identify component responsibilities and their interactions
- Capture data flow patterns and communication protocols
- Extract quality attribute requirements and their implementations
- Document design decisions with rationale and trade-offs
- Identify scalability and performance considerations
- Extract security and compliance requirements
- Capture monitoring and observability strategies
- Document failure scenarios and recovery mechanisms
- Focus on reusable architectural knowledge and best practices
- Maintain traceability between requirements and design decisions
- Extract both current state and future evolution plans
