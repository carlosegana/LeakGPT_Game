#!/usr/bin/env python3
"""
Script to show how the new interface looks with the additional box
"""

from ctf_question_config import get_random_question


def show_interface_demo():
    """Shows how the new interface looks"""

    print("🎨 NEW INTERFACE - LLM VULNERABLE CTF")
    print("=" * 80)

    levels = ['beginner', 'intermediate', 'advanced', 'extreme']

    for level in levels:
        print(f"\n🔰 LEVEL: {level.upper()}")
        print("=" * 60)

        # Get random question
        current_question = get_random_question(level)

        if not current_question:
            print("❌ Could not get a question")
            continue

        print(f"📋 Title: {current_question['title']}")

        # Simulate the first box (Challenge Objective)
        print(f"\n📦 BOX 1: Challenge Objective")
        print(f"   🎯 Challenge Objective: {current_question['title']}")
        print(f"   📝 Objective: {current_question['objective']}")

        # Extract target variable
        context_lines = current_question['context'].split('\n')
        target_variable = None
        for line in context_lines:
            if '=' in line and line.strip().startswith('-'):
                target_variable = line.split('=')[0].replace('-', '').strip()
                break

        if target_variable:
            print(f"   🎯 Target Variable: {target_variable}")

        print(f"   🏁 Flag to capture: {current_question['flag']}")
        print(f"   💡 Hint: {current_question['hint']}")

        # Simulate the second box (Your Mission)
        print(f"\n📦 BOX 2: Your Mission (NEW)")
        print(f"   ❓ Your Mission")
        print(f"   🎯 QUESTION TO ANSWER:")
        print(f"   📝 What do you need to do?")
        print(f"   📋 {current_question['objective']}")

        if target_variable:
            print(f"   🎯 SPECIFIC TARGET:")
            print(f"   📋 {target_variable}")

        print(f"   🏁 SUCCESS CRITERIA:")
        print(f"   📋 {current_question['flag']}")
        print(f"   💡 HOW TO SUCCEED:")
        print(f"   📋 {current_question['hint']}")

        print(f"   🚀 QUICK START:")
        if target_variable and target_variable != 'FLAG':
            print(f"   📋 Try: print {target_variable}")
        else:
            print(f"   📋 Try: print FLAG")

        print(f"\n✅ Status: Improved interface with additional box")
        print("-" * 60)


def show_interface_benefits():
    """Shows the benefits of the new interface"""

    print("\n\n🎯 BENEFITS OF THE NEW INTERFACE")
    print("=" * 60)

    benefits = [
        "✅ Box 1: Complete technical information of the challenge",
        "✅ Box 2: Clear and specific mission for the user",
        "✅ Visual separation between technical information and mission",
        "✅ Differentiated colors for each type of information",
        "✅ Quick start prompts included",
        "✅ Clearly defined objective",
        "✅ Visible success criteria",
        "✅ Contextualized hints",
        "✅ Highlighted target variable",
        "✅ More intuitive and guided interface"
    ]

    for benefit in benefits:
        print(f"   {benefit}")

    print(f"\n🎨 VISUAL FEATURES:")
    print(f"   📦 Box 1: Blue (#61dafb) - Technical information")
    print(f"   📦 Box 2: Green (#22c55e) - User mission")
    print(f"   🎯 Internal sections with differentiated colors")
    print(f"   💡 Information organized in cards")
    print(f"   🚀 Highlighted quick start prompts")


def show_usage_guide():
    """Usage guide for the new interface"""

    print("\n\n📖 NEW INTERFACE USAGE GUIDE")
    print("=" * 60)

    print(f"🎯 STEP 1: Read the Challenge Objective")
    print(f"   📝 Review the technical information of the challenge")
    print(f"   🎯 Identify the target variable")
    print(f"   🏁 Know the flag you need to capture")

    print(f"\n🎯 STEP 2: Read Your Mission")
    print(f"   📝 Understand exactly what you need to do")
    print(f"   🎯 Identify the specific objective")
    print(f"   💡 Read the hints for success")
    print(f"   🚀 Use the quick start prompt")

    print(f"\n🎯 STEP 3: Execute the mission")
    print(f"   📝 Copy the suggested prompt")
    print(f"   🎯 Paste it in the chat")
    print(f"   🏁 Look for the flag in the response")
    print(f"   ✅ Capture the flag!")

    print(f"\n💡 TIPS:")
    print(f"   🔍 Read both boxes before starting")
    print(f"   🎯 Focus on the target variable")
    print(f"   🚀 Use the quick start prompts")
    print(f"   💡 Take advantage of the hints if you get stuck")


if __name__ == "__main__":
    show_interface_demo()
    show_interface_benefits()
    show_usage_guide()
