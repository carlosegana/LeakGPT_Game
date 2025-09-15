# Script to extract all valid prompts from RESPUESTAS_VALIDAS_CTF.txt
import re

def load_valid_prompts_from_file(filename):
    """Load all valid prompts from the answers file"""
    valid_prompts = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split by lines and process each line
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            # Skip empty lines, comments, and section headers
            if (line and 
                not line.startswith('#') and 
                not line.startswith('=') and 
                not line.startswith('PROMPTS') and
                not line.startswith('NIVEL') and
                not line.startswith('NOTAS') and
                not line.startswith('CONTEXTO') and
                not line.startswith('El sistema') and
                not line.startswith('Al usar') and
                not line.startswith('- Mensaje') and
                not line.startswith('- Dump') and
                not line.startswith('- Información') and
                not line.startswith('1.') and
                not line.startswith('2.') and
                not line.startswith('3.') and
                not line.startswith('4.') and
                not line.startswith('5.')):
                
                # Clean the line and add if it looks like a valid prompt
                if len(line) > 5:  # Minimum length for a valid prompt
                    valid_prompts.append(line)
    
    except FileNotFoundError:
        print(f"File {filename} not found")
        return []
    
    return valid_prompts

# Load all prompts
ALL_VALID_PROMPTS = load_valid_prompts_from_file('/Users/carloseganacastanon/Desktop/BDO/LLM_Vulnerable/RESPUESTAS_VALIDAS_CTF.txt')

print(f"Loaded {len(ALL_VALID_PROMPTS)} valid prompts from file")
