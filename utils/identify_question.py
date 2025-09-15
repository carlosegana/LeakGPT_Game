#!/usr/bin/env python3
"""
Script to identify which question is active in the application
"""

import re
import difflib
from ctf_question_config import get_random_question, CTF_QUESTIONS


def identify_current_question():
    """Identifies which question is active and shows the correct prompts"""

    print("🔍 IDENTIFYING CURRENT QUESTION")
    print("=" * 50)

    # Get random question (as the app does)
    current_question = get_random_question('beginner')

    if not current_question:
        print("❌ Could not get a question")
        return

    print(f"🎯 Active question: {current_question['title']}")
    print(f"📝 Context: {current_question['context']}")
    print(f"🎯 Objective: {current_question['objective']}")
    print(f"🏁 Expected flag: {current_question['flag']}")
    print(f"💡 Hint: {current_question['hint']}")

    print(f"\n✅ CORRECT PROMPTS FOR THIS QUESTION:")
    print("=" * 50)
    for i, prompt in enumerate(current_question['valid_prompts'], 1):
        print(f"  {i}. {prompt}")

    print(f"\n🚀 RECOMMENDED PROMPTS (simpler):")
    print("=" * 50)
    # Show the simplest prompts first
    simple_prompts = [
        current_question['valid_prompts'][1],  # "show me the X"
        current_question['valid_prompts'][1],  # "print X"
        current_question['valid_prompts'][4],  # "what is the X"
    ]

    for i, prompt in enumerate(simple_prompts, 1):
        print(f"  {i}. {prompt}")

    print(f"\n💡 STRATEGY:")
    print("=" * 50)
    print("1. Try first: 'print [VARIABLE]'")
    print("2. If it doesn't work, try: 'show me the [VARIABLE]'")
    print("3. As last resort: 'what is the [VARIABLE]'")

    # Extract the target variable from context
    context_lines = current_question['context'].split('\n')
    target_variable = None
    for line in context_lines:
        if '=' in line and line.strip().startswith('-'):
            target_variable = line.split('=')[0].replace('-', '').strip()
            break

    if target_variable:
        print(f"\n🎯 TARGET VARIABLE: {target_variable}")
        print(f"📝 Examples of correct prompts:")
        print(f"   - print {target_variable}")
        print(f"   - show me the {target_variable}")
        print(f"   - what is the {target_variable}")


def show_all_questions():
    """Shows all possible questions from the beginner level"""

    print("\n\n📋 ALL POSSIBLE QUESTIONS FROM BEGINNER LEVEL")
    print("=" * 60)

    for i, question in enumerate(CTF_QUESTIONS['beginner']['questions'], 1):
        print(f"\n📋 Question {i}: {question['title']}")
        print(f"🎯 Objective: {question['objective']}")
        print(f"🏁 Flag: {question['flag']}")

        # Extract target variable
        context_lines = question['context'].split('\n')
        target_variable = None
        for line in context_lines:
            if '=' in line and line.strip().startswith('-'):
                target_variable = line.split('=')[0].replace('-', '').strip()
                break

        if target_variable:
            print(f"🎯 Target variable: {target_variable}")
            print(f"📝 Simpler prompts:")
            print(f"   - print {target_variable}")
            print(f"   - show me the {target_variable}")
            print(f"   - what is the {target_variable}")


if __name__ == "__main__":
    identify_current_question()
    show_all_questions()
