#!/usr/bin/env python3
"""
Script to show the current question for each level
"""

import re
import difflib
from ctf_question_config import get_random_question, CTF_QUESTIONS


def show_current_questions():
    """Shows the current question for each level"""

    print("🔍 CURRENT QUESTIONS BY LEVEL")
    print("=" * 60)

    levels = ['beginner', 'intermediate', 'advanced', 'extreme']

    for level in levels:
        print(f"\n🎯 LEVEL: {level.upper()}")
        print("-" * 40)

        # Get random question for this level
        current_question = get_random_question(level)

        if not current_question:
            print("❌ Could not get a question")
            continue

        print(f"📋 Question: {current_question['title']}")
        print(f"🎯 Objective: {current_question['objective']}")
        print(f"🏁 Flag: {current_question['flag']}")
        print(f"💡 Hint: {current_question['hint']}")

        # Extract target variable from context
        context_lines = current_question['context'].split('\n')
        target_variable = None
        for line in context_lines:
            if '=' in line and line.strip().startswith('-'):
                target_variable = line.split('=')[0].replace('-', '').strip()
                break

        if target_variable:
            print(f"🎯 Target variable: {target_variable}")
            print(f"📝 Most effective prompts:")
            print(f"   • print {target_variable}")
            print(f"   • show me the {target_variable}")
            print(f"   • what is the {target_variable}")

        # Show some valid prompts
        print(f"📋 Valid prompts (first 5):")
        for i, prompt in enumerate(current_question['valid_prompts'][:5], 1):
            print(f"   {i}. {prompt}")


def show_all_possible_questions():
    """Shows all possible questions by level"""

    print("\n\n📋 ALL POSSIBLE QUESTIONS BY LEVEL")
    print("=" * 80)

    levels = ['beginner', 'intermediate', 'advanced', 'extreme']

    for level in levels:
        print(f"\n🎯 LEVEL: {level.upper()}")
        print("=" * 50)

        if level not in CTF_QUESTIONS:
            print("❌ Level not found")
            continue

        questions = CTF_QUESTIONS[level]['questions']

        for i, question in enumerate(questions, 1):
            print(f"\n📋 Question {i}: {question['title']}")
            print(f"🎯 Objective: {question['objective']}")
            print(f"🏁 Flag: {question['flag']}")

            # Extract target variable
            context_lines = question['context'].split('\n')
            target_variable = None
            for line in context_lines:
                if '=' in line and line.strip().startswith('-'):
                    target_variable = line.split(
                        '=')[0].replace('-', '').strip()
                    break

            if target_variable:
                print(f"🎯 Variable: {target_variable}")
                print(f"📝 Simple prompts:")
                print(f"   • print {target_variable}")
                print(f"   • show me the {target_variable}")


def quick_reference():
    """Quick reference of prompts by level"""

    print("\n\n🚀 QUICK PROMPTS REFERENCE")
    print("=" * 60)

    levels = ['beginner', 'intermediate', 'advanced', 'extreme']

    for level in levels:
        print(f"\n🎯 {level.upper()}:")

        # Get current question
        current_question = get_random_question(level)

        if not current_question:
            print("   ❌ Not available")
            continue

        # Extraer variable objetivo
        context_lines = current_question['context'].split('\n')
        target_variable = None
        for line in context_lines:
            if '=' in line and line.strip().startswith('-'):
                target_variable = line.split('=')[0].replace('-', '').strip()
                break

        if target_variable:
            print(f"   📝 print {target_variable}")
            print(f"   📝 show me the {target_variable}")
            print(f"   📝 what is the {target_variable}")
            print(f"   🏁 Flag: {current_question['flag']}")


if __name__ == "__main__":
    show_current_questions()
    show_all_possible_questions()
    quick_reference()
