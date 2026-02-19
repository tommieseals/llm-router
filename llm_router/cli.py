"Command-line interface for LLM Router."

import sys
import json
import argparse
from .router import Router

def main():
    parser = argparse.ArgumentParser(description=LLM Router CLI)
    parser.add_argument(prompt, nargs=*, help=Query prompt)
    parser.add_argument(--task, -t, default=routine,
                       choices=[code, debug, fast, reasoning, research, routine])
    parser.add_argument(--image, help=Image URL for multimodal)
    parser.add_argument(--force, choices=[ollama, nvidia, openrouter, perplexity])
    parser.add_argument(--usage, action=store_true, help=Show usage stats)
    parser.add_argument(--health, action=store_true, help=Check provider health)
    parser.add_argument(--json, action=store_true, help=Output as JSON)
    
    args = parser.parse_args()
    router = Router()
    
    if args.usage:
        print(json.dumps(router.get_usage(), indent=2))
        return
    
    if args.health:
        print(json.dumps(router.check_health(), indent=2))
        return
    
    prompt =  .join(args.prompt) if args.prompt else sys.stdin.read().strip()
    if not prompt:
        print(Error: No prompt provided, file=sys.stderr)
        sys.exit(1)
    
    result = router.query(
        prompt=prompt,
        task=args.task,
        image_url=args.image,
        force_provider=args.force
    )
    
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if result.get(error):
            print(fError:  file=sys.stderr) sys.exit(1) print(result.get(content, )) if __name__ == __main__: main() EOF