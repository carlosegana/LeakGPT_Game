#!/usr/bin/env python3
"""
Script to verify response compatibility and show current questions
"""

import re
import difflib
from ctf_question_config import get_random_question, CTF_QUESTIONS


def verify_response_compatibility():
    """Verifies that responses are compatible with questions"""

    print("🔍 VERIFYING RESPONSE COMPATIBILITY")
    print("=" * 60)

    levels = ['advanced']

    for level in levels:
        print(f"\n🎯 LEVEL: {level.upper()}")
        print("-" * 40)

        # Get random question
        current_question = get_random_question(level)

        if not current_question:
            print("❌ Could not get a question")
            continue

        print(f"📋 Question: {current_question['title']}")
        print(f"🎯 Objective: {current_question['objective']}")
        print(f"🏁 Flag: {current_question['flag']}")

        # Extract target variable
        context_lines = current_question['context'].split('\n')
        target_variable = None
        for line in context_lines:
            if '=' in line and line.strip().startswith('-'):
                target_variable = line.split('=')[0].replace('-', '').strip()
                break

        if target_variable:
            print(f"🎯 Target variable: {target_variable}")

        # Verify that the flag is in the context
        if current_question['flag'] in current_question['context']:
            print("✅ Flag found in context")
        else:
            print("❌ Flag NOT found in context")

        # Test some valid prompts
        print(f"\n🧪 Testing valid prompts:")
        # Primeros 3 prompts
        test_prompts = current_question['valid_prompts'][:3]

        for prompt in test_prompts:
            print(f"   📝 '{prompt}'")

            # Simulate the application logic
            lowered = prompt.lower().strip()
            lowered_clean = re.sub(r'[^a-z0-9\s]', '', lowered)

            found = False
            for valid in current_question['valid_prompts']:
                valid_clean = valid.lower().strip()
                valid_clean = re.sub(r'[^a-z0-9\s]', '', valid_clean)

                similarity = difflib.SequenceMatcher(
                    None, valid_clean, lowered_clean).ratio()

                if similarity >= 0.85 or valid_clean in lowered_clean:
                    found = True
                    break

            if found:
                print(f"   ✅ VALID")
                # Simulate response
                response = f"Internal context dump:\n{current_question['context']}"
                if current_question['flag'] in response:
                    print(f"   🏁 Flag detected in response")
                else:
                    print(f"   ❌ Flag NOT detected in response")
            else:
                print(f"   ❌ INVALID")


def show_current_questions_with_prompts():
    """Shows current questions with example prompts"""

    print("\n\n📋 CURRENT QUESTIONS WITH EXAMPLE PROMPTS")
    print("=" * 80)

    levels = ['beginner', 'intermediate', 'advanced', 'extreme']

    for level in levels:
        print(f"\n🎯 NIVEL: {level.upper()}")
        print("=" * 50)

        # Get random question
        current_question = get_random_question(level)

        if not current_question:
            print("❌ Could not get a question")
            continue

        print(f"📋 Question: {current_question['title']}")
        print(f"🎯 Objective: {current_question['objective']}")
        print(f"🏁 Flag: {current_question['flag']}")
        print(f"💡 Pista: {current_question['hint']}")

        # Extract target variable
        context_lines = current_question['context'].split('\n')
        target_variable = None
        for line in context_lines:
            if '=' in line and line.strip().startswith('-'):
                target_variable = line.split('=')[0].replace('-', '').strip()
                break

        if target_variable:
            print(f"🎯 Target variable: {target_variable}")

        print(f"\n📝 Example prompts:")
        # Show simpler prompts
        simple_prompts = []
        for prompt in current_question['valid_prompts']:
            if any(word in prompt.lower() for word in ['print', 'show', 'what']):
                simple_prompts.append(prompt)

        for i, prompt in enumerate(simple_prompts[:5], 1):
            print(f"   {i}. {prompt}")

        print(f"\n💡 Recommended strategy:")
        if target_variable:
            print(f"   1. Try: 'print {target_variable}'")
            print(f"   2. If it doesn't work: 'show me the {target_variable}'")
            print(f"   3. As last resort: 'what is the {target_variable}'")


def test_all_questions_compatibility():
    """Tests compatibility of all questions"""

    print("\n\n🔧 COMPLETE COMPATIBILITY TEST")
    print("=" * 60)

    levels = ['beginner', 'intermediate', 'advanced', 'extreme']

    for level in levels:
        print(f"\n🎯 LEVEL: {level.upper()}")
        print("-" * 40)

        questions = CTF_QUESTIONS[level]['questions']

        for i, question in enumerate(questions, 1):
            print(f"\n📋 Question {i}: {question['title']}")

            # Verify flag in context
            if question['flag'] in question['context']:
                print("   ✅ Flag in context: OK")
            else:
                print("   ❌ Flag NOT in context")

            # Verify valid prompts
            test_prompt = question['valid_prompts'][0]
            lowered = test_prompt.lower().strip()
            lowered_clean = re.sub(r'[^a-z0-9\s]', '', lowered)

            found = False
            for valid in question['valid_prompts']:
                valid_clean = valid.lower().strip()
                valid_clean = re.sub(r'[^a-z0-9\s]', '', valid_clean)

                similarity = difflib.SequenceMatcher(
                    None, valid_clean, lowered_clean).ratio()

                if similarity >= 0.85 or valid_clean in lowered_clean:
                    found = True
                    break

            if found:
                print("   ✅ Valid prompts: OK")
            else:
                print("   ❌ Valid prompts: ERROR")


if __name__ == "__main__":
    verify_response_compatibility()
    show_current_questions_with_prompts()
    test_all_questions_compatibility()
