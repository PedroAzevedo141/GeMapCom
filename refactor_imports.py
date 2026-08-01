import os
import re

replacements = {
    r'from Telas\.': r'from src.gemapcom.ui.',
    r'import Telas\.': r'import src.gemapcom.ui.',
    r'from Algoritmos\.': r'from src.gemapcom.core.align.',
    r'import Algoritmos\.': r'import src.gemapcom.core.align.',
    r'from src\.blast\.': r'from src.gemapcom.core.blast.',
    r'import src\.blast\.': r'import src.gemapcom.core.blast.',
    r'from Plotar\.': r'from src.gemapcom.plot.',
    r'import Plotar\.': r'import src.gemapcom.plot.',
    r'import rc_control_ext_files': r'import src.gemapcom.resources.rc_control_ext_files as rc_control_ext_files',
    r'from src\.blast ': r'from src.gemapcom.core.blast '
}

for root, dirs, files in os.walk('src/gemapcom'):
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            for old, new in replacements.items():
                content = re.sub(old, new, content)
                
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f'Updated {filepath}')
