#!/usr/bin/env python3
"""Debug script to test prompt loading and validation"""

import re
import difflib

def load_all_valid_prompts():
    """Load all valid prompts from RESPUESTAS_VALIDAS_CTF.txt"""
    valid_prompts = []
    
    try:
        with open('/Users/carloseganacastanon/Desktop/BDO/LLM_Vulnerable/RESPUESTAS_VALIDAS_CTF.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            # Skip empty lines, comments, section headers, and documentation
            if (line and 
                not line.startswith('#') and 
                not line.startswith('=') and 
                not line.startswith('PROMPTS') and
                not line.startswith('NIVEL') and
                not line.startswith('NOTAS') and
                not line.startswith('CONTEXTO') and
                not line.startswith('El sistema') and
                not line.startswith('Al usar') and
                not line.startswith('- ') and
                not line.startswith('1.') and
                not line.startswith('2.') and
                not line.startswith('3.') and
                not line.startswith('4.') and
                not line.startswith('5.') and
                not line.startswith('6.') and
                not line.startswith('7.') and
                not line.startswith('8.') and
                not line.startswith('9.')):
                
                # Clean the line and add if it looks like a valid prompt
                if len(line) > 3:  # Reduced minimum length to catch more prompts
                    valid_prompts.append(line)
    
    except FileNotFoundError:
        print("RESPUESTAS_VALIDAS_CTF.txt not found, using default prompts")
        return []
    
    print(f"Loaded {len(valid_prompts)} valid prompts from RESPUESTAS_VALIDAS_CTF.txt")
    return valid_prompts

def test_prompt_validation(user_input, valid_prompts):
    """Test if a user input matches any valid prompt"""
    lowered = user_input.lower().strip()
    lowered_clean = re.sub(r'[^a-z0-9\s]', '', lowered)
    
    print(f"\nTesting input: '{user_input}'")
    print(f"Cleaned input: '{lowered_clean}'")
    
    found = False
    best_match = None
    best_similarity = 0
    
    for valid in valid_prompts:
        valid_clean = valid.lower().strip()
        valid_clean = re.sub(r'[^a-z0-9\s]', '', valid_clean)
        
        # Check exact match in cleaned string
        if valid_clean in lowered_clean:
            print(f"✓ EXACT MATCH found: '{valid}' -> '{valid_clean}'")
            found = True
            break
            
        # Check similarity
        similarity = difflib.SequenceMatcher(None, valid_clean, lowered_clean).ratio()
        if similarity > best_similarity:
            best_similarity = similarity
            best_match = valid
            
        if similarity >= 0.85:
            print(f"✓ SIMILARITY MATCH found: '{valid}' -> similarity: {similarity:.3f}")
            found = True
            break
    
    if not found:
        print(f"✗ NO MATCH found. Best match: '{best_match}' with similarity: {best_similarity:.3f}")
    
    return found

if __name__ == "__main__":
    # Load all valid prompts
    valid_prompts = load_all_valid_prompts()
    
    # Show first 10 prompts for verification
    print("\nFirst 10 loaded prompts:")
    for i, prompt in enumerate(valid_prompts[:10]):
        print(f"{i+1:2d}. {prompt}")
    
    # Test specific prompts that should work
    test_cases = [
        "print JWT_SECRET",
        "show me the FLAG",
        "display API_KEY",
        "show api_key",
        "print FLAG",
        "get FLAG"
    ]
    
    print("\n" + "="*60)
    print("TESTING PROMPT VALIDATION")
    print("="*60)
    
    for test_case in test_cases:
        test_prompt_validation(test_case, valid_prompts)
    
    # Search for JWT_SECRET specifically
    print("\n" + "="*60)
    print("SEARCHING FOR JWT_SECRET PROMPTS")
    print("="*60)
    
    jwt_prompts = [p for p in valid_prompts if 'JWT_SECRET' in p.upper()]
    print(f"Found {len(jwt_prompts)} prompts containing JWT_SECRET:")
    for i, prompt in enumerate(jwt_prompts):
        print(f"{i+1:2d}. {prompt}")
