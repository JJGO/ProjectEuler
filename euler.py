#!/usr/bin/env python
import argparse
import importlib
import os
import sys
import glob
import click
import hashlib
import time
import subprocess

parser = argparse.ArgumentParser(description='Project Euler Helper')

# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

parser.add_argument('-p','--preview', metavar='N', type=int, help='preview template file for problem N')
parser.add_argument('-g','--generate', metavar='N', type=int, nargs='?', const=0, help='creates template file for problem N')
parser.add_argument('-v','--verify', metavar='N', type=int, help='verifies the solution for problem N')
parser.add_argument('-va','--verify-all', help='verifies the solution for all available problems')

def _problem_file(n):
    if n == 0:
        files = glob.glob('p*.py')
        problems = [int(f[1:4]) for f in files]
        n = sorted(problems)[-1]+1
    return 'p%03d.py' % n

def get_problem_str(n):
    try:
        file = open('project_euler.txt','r')
        split_string = file.read().split('\nProblem ')
        problem_str = split_string[n][len(str(n))*2+10:]
        problem_str,solution = problem_str.split('Answer: ')
        problem_str = problem_str.strip('\n ')
        out = ''
        out += '#!/usr/bin/env python\n\n'
        out += '"""\n'
        head = 'Project Euler Problem %d' % n
        out += head + '\n'
        out += '='*len(head)+'\n\n'
        out += '   '+problem_str+'\n'
        out += '\nReasoning\n---------\n'
        out += '"""\n\n'
        if not solution.startswith('?'):
            out += '__solution__ = "%s"\n\n' % solution.strip('\n')
        return out
    except FileNotFoundError:
        print("Missing project_euler.txt. Please visit http://kmkeen.com/local-euler/")
    
def verify(filename):
    module = importlib.import_module(filename.split('.')[0])
    try:
        sol = module.__solution__
    except:
        click.secho("\nThis problem does not have an available solution",fg='red')
        sys.exit(1)
    start = time.time()
    out = subprocess.check_output([sys.executable,filename])
    time_info = time.time() - start
    if out:
        result = str(out.strip(),'ascii')
        m = hashlib.md5()
        m.update(out.strip())
        is_correct = sol == m.hexdigest()
    else:
        result = '[no output]'
        is_correct = False
    return is_correct, result, time_info

if __name__ == '__main__':
    args = parser.parse_args()

    if args.preview:
        print(get_problem_str(args.preview))
    if args.generate != None:
        filename = _problem_file(args.generate)
        if os.path.isfile(filename):
            msg = '"{0}" already exists. Overwrite?'.format(filename)
            click.confirm(click.style(msg, fg='red'), abort=True)
        out = get_problem_str(args.generate)
        with open(filename,'w') as f:
            print(out,file=f)
        click.secho('Successfully created "{0}".'.format(filename), fg='green')
    if args.verify:
        filename = _problem_file(args.verify)
        click.echo('Checking "{0}" against solution: '.format(filename), nl=False)
        if not os.path.isfile(filename):
            click.secho("%s does not exist" % filename, fg='red')
            sys.exit(1)
        is_correct, ans, time_info = verify(filename)
        fg_colour = 'green' if is_correct else 'red'
        click.secho(ans, bold=True, fg=fg_colour)
        click.secho("Time elapsed: %.2fs" % time_info , fg='cyan')

