#!/usr/bin/env python3
"Basic usage example for LLM Router."

from llm_router import Router

# Initialize router
router = Router()

# Simple query (auto-routed)
response = router.query(What is the capital of France?)
print(fResponse:   ' No content ' )})

# Code task (routes to code-specialized model)
code_response = router.query(
    Write a Python function to calculate fibonacci,
    task=code
)
print(fCode:   ' No content ' )})

# Check usage
usage = router.get_usage()
print(fUsage today: usage)
