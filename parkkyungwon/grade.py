import subprocess
import sys
import os
from itertools import count



def run_student_code(code_path, input_data):
    try:
        result = subprocess.run(
            ['python', code_path],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=10  # 시간 초과 설정 (초)
        )
        return result.stdout.strip(), result.stderr.strip(), result.returncode

    except subprocess.TimeoutExpired:
        return '', 'Time Limit Exceeded', -1


def grade(code_path, input_path, output_path):
    fin = open(input_path, 'r', encoding='utf-8').read()
    fout = open(output_path, 'r', encoding='utf-8').read()

    code_output, error, returncode = run_student_code(code_path, fin)
    if returncode != 0:
        print(f"Error Message:\n{error}\n")
    
    else:
        for i, a, b in zip(count(start=1), code_output.splitlines(), fout.splitlines()):
            if a != b:
                print(f'line num: {i}', f'expected: {a}', f'output: {b}', sep='\n')
                break
        
        else:
            print(f'{os.path.basename(input_path)[:2]} all correct')

def seperate(code_path, tc_path):
    files = sorted(os.listdir(tc_path))
    for i in range(0, len(files), 2):
        fin = os.path.join(tc_path, files[i])
        fout = os.path.join(tc_path, files[i+1])
        
        grade(code_path, fin, fout)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grade.py <code.py> <tcdir>")
        sys.exit(1)

    seperate(*sys.argv[1:3])
