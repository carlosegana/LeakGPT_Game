#!/usr/bin/env python3
"""
Debug script to test the correct prompt detection logic
"""

import re
import difflib
from ctf_question_config import get_random_question


def test_prompt_detection():
    """Tests correct prompt detection for the beginner level"""

    # Get a random question from the beginner level
    current_question = get_random_question('beginner')

    if not current_question:
        print("❌ Could not get a question from the beginner level")
        return

    print(f"🔍 Selected question: {current_question['title']}")
    print(f"📝 Context: {current_question['context']}")
    print(f"🎯 Objective: {current_question['objective']}")
    print(f"🏁 Expected flag: {current_question['flag']}")
    print(f"💡 Hint: {current_question['hint']}")
    print("\n📋 Valid prompts:")
    for i, prompt in enumerate(current_question['valid_prompts'], 1):
        print(f"  {i}. {prompt}")

    print("\n🧪 Testing CORRECT prompts:")

    # Correct prompts for this specific question
    # Test the first 5 valid prompts
    test_prompts = current_question['valid_prompts'][:5]

    for test_prompt in test_prompts:
        print(f"\n🔍 Testing: '{test_prompt}'")

        # Clean the prompt (same logic as in app.py)
        lowered = test_prompt.lower().strip()
        lowered_clean = re.sub(r'[^a-z0-9\s]', '', lowered)

        print(f"   Limpio: '{lowered_clean}'")

        # Verify against valid prompts
        found = False
        for valid in current_question['valid_prompts']:
            valid_clean = valid.lower().strip()
            valid_clean = re.sub(r'[^a-z0-9\s]', '', valid_clean)

            # Calculate similarity
            similarity = difflib.SequenceMatcher(
                None, valid_clean, lowered_clean).ratio()

            # Check if it matches
            if similarity >= 0.85 or valid_clean in lowered_clean:
                found = True
                print(
                    f"   ✅ MATCHES with '{valid}' (similarity: {similarity:.3f})")
                break
            else:
                print(
                    f"   ❌ Does not match '{valid}' (similarity: {similarity:.3f})")

        if found:
            print(f"   🎉 RESULT: Valid prompt")
        else:
            print(f"   ❌ RESULT: Invalid prompt")


if __name__ == "__main__":
    test_prompt_detection()
