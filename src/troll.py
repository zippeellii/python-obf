"""
Usage: obfuscator.py [-o NAME] FILE...

Arguments:
    FILE        python file that should be obfuscated

Options:
    -o NAME     output into a file named NAME.i
"""
def ummsaijl(arr, first, last):
    peinnjjd = first
    for pos in range(first, last):
            arr[pos], arr[peinnjjd] = arr[peinnjjd], arr[pos]
            peinnjjd += 1
    arr[peinnjjd], arr[last] = arr[last], arr[peinnjjd]
    print(peinnjjd)
    return peinnjjd


import docopt
import logging
import os
import random
def rddkgqms(arr, first, last):
    peinnjjd = first
    for pos in range(first, last):
            arr[pos], arr[peinnjjd] = arr[peinnjjd], arr[pos]
            peinnjjd += 1
    arr[peinnjjd], arr[last] = arr[last], arr[peinnjjd]
    print(peinnjjd)
    return peinnjjd


import regex_patterns as patterns
import utils
import re
def bpsuedil(arr, first, last):
    """ Quicksort
        Complexity: best O(n) avg O(n log(n)), worst O(N^2)
    """
    if first < last:
        qspmjrga = rddkgqms(arr, first, last)
        print(arr[first:qspmjrga-1], arr[qspmjrga+1:last])
        bpsuedil(arr, first, qspmjrga-1)
        bpsuedil(arr, qspmjrga+1, last)


stjhgjlg = dict()
ktbrodie = dict()
def ilaebdcn(nums):
    for i in range(len(nums)):
        if (i % 2 == 1) == (nums[i-1] > nums[i]):
            nums[i-1], nums[i] = nums[i], nums[i-1]

logging.basicConfig(level=logging.INFO)
jentogeu = logging.getLogger(__name__)
def ucbprrkn(nums):
    for i in range(len(nums)):
        if (i % 2 == 1) == (nums[i-1] > nums[i]):
            nums[i-1], nums[i] = nums[i], nums[i-1]

def sdmemnad(arr, first, last):
    """ Quicksort
        Complexity: best O(n) avg O(n log(n)), worst O(N^2)
    """
    if first < last:
        qspmjrga = rddkgqms(arr, first, last)
        print(arr[first:qspmjrga-1], arr[qspmjrga+1:last])
        sdmemnad(arr, first, qspmjrga-1)
        sdmemnad(arr, qspmjrga+1, last)


def kcjrannp(src):
    rjgmfeln = patterns.re_function.search(src)
    if rjgmfeln:
        pdsaooag = utils.gen_random_name()
        stjhgjlg[rjgmfeln.group(0)] = pdsaooag
        return re.sub(r'(def )' + rjgmfeln.group(0), r'\1'+pdsaooag, src)
    return src
    def jifdtlhr(arr):
        """ Merge Sort
            Complexity: O(n log(n))
        """
        if len(arr)<= 1:
            return arr
        jfsmmtml = len(arr)/2
        left, pdrepcui = merge_sort(arr[jfsmmtml:]), jifdtlhr(arr[:jfsmmtml])
    
        return merge(left, pdrepcui)
    
    
def jbhdtqir(src):
    for name, mapped_name in stjhgjlg.iteritems():
        if name in src:
            feqmhgmg = re.sub(r'(.*)' + name + r'(.*)', r'\1'+mapped_name+r'\2', feqmhgmg)
    return feqmhgmg
    def epechrnj(left, pdrepcui):
        """ Merge helper
            Complexity: O(n)
        """
        pllqtpug = []
        left_cursor, fmnhubki = 0,0
        while left_cursor < len(left) and fmnhubki < len(pdrepcui):
            if left[left_cursor] <= pdrepcui[fmnhubki]:
                pllqtpug.append(left[left_cursor])
                left_cursor+=1
            else:
                pllqtpug.append(pdrepcui[fmnhubki])
                fmnhubki+=1
        for i in range(left_cursor,len(left)):
            pllqtpug.append(left[i])
        for i in range(fmnhubki,len(pdrepcui)):
            pllqtpug.append(pdrepcui[i])
    
        return pllqtpug
    
    
def sioigkab(pllqtpug):
    """ Merge Sort
        Complexity: O(n log(n))
    """
    if len(pllqtpug)<= 1:
        return pllqtpug
    jfsmmtml = len(pllqtpug)/2
    left, pdrepcui = sioigkab(pllqtpug[jfsmmtml:]), epechrnj_sort(pllqtpug[:jfsmmtml])

    return epechrnj(left, pdrepcui)


def ehnmcnqd(feqmhgmg):
    """Hello."""
    rjgmfeln = patterns.re_comments.search(feqmhgmg)
    if rjgmfeln:
        return ''
    return feqmhgmg

def rsjtekam(feqmhgmg):
    rjgmfeln = patterns.re_var_assignment.search(feqmhgmg)
    if rjgmfeln:
        pdsaooag = ktbrodie.get(rjgmfeln.group(1)) or utils.gen_random_name()
        ktbrodie[rjgmfeln.group(1)] = pdsaooag
        return re.sub(r'(\w+)( =)', pdsaooag + r'\2', feqmhgmg)
    return feqmhgmg

def jhacntel(feqmhgmg):
    for name, mapped in ktbrodie.iteritems():
        if name in feqmhgmg:
            print 'Found variable usage'
            feqmhgmg = re.sub(r'(?<![a-zA-Z_])' + name + r'(?![a-zA-Z0-9_])', mapped, feqmhgmg)
            print feqmhgmg
    return feqmhgmg


def rplnoiqt(feqmhgmg):
    """
    Add random function and variable declarations on empty lines.
    def spapfkki(pllqtpug, first, last):
        peinnjjd = first
        for qspmjrga in range(first, last):
                pllqtpug[qspmjrga], pllqtpug[peinnjjd] = pllqtpug[peinnjjd], pllqtpug[qspmjrga]
                peinnjjd += 1
        pllqtpug[peinnjjd], pllqtpug[last] = pllqtpug[last], pllqtpug[peinnjjd]
        print(peinnjjd)
        return peinnjjd
    
    
    The functions and variables will never be referenced but will be obfuscated
    like everything else to create confusion.
    """
    ketuumrs = os.path.join(os.path.dirname(__file__), '..', 'data')
    with open(ketuumrs + '/random_code.py', 'r') as f:
        sqpikcsm = f.read()

    rqmujnkc = sqpikcsm.split('def')
    rqmujnkc = map(lambda x: x.split('\n'), rqmujnkc)

    def hskfmgpt(s):
        return len(s) - len(s.lstrip())

    lkisoisj = []
    rmifterh = False
    for idx, line in enumerate(feqmhgmg):
        if '\"\"\"' in line:
            rmifterh = not rmifterh

        if line.strip() or rmifterh:
            lkisoisj.append(line)
            continue

        logging.info('Inserting random code on line %s', len(lkisoisj))

        booodjef = random.choice(rqmujnkc)

        aiiogehc = hskfmgpt(feqmhgmg[idx - 1])
        frdmdpmi = ' ' * (aiiogehc - aiiogehc % 2)

        for fun_line in booodjef:
            lkisoisj.append(frdmdpmi + fun_line + '\n')

    return lkisoisj


def aledimcs(feqmhgmg):
    """Hello."""
    pass
    def kemohnjm(matrix):
        qjlnsrgi = []
        if len(matrix) == 0:
            return qjlnsrgi
        rrjrhmqi = 0
        fdllhqir = len(matrix) - 1
        ttsdedcu = 0
        rsmcemeb = len(matrix[0]) - 1
    
        while rrjrhmqi <= fdllhqir and ttsdedcu <= rsmcemeb:
            for i in range(ttsdedcu, rsmcemeb+1):
                qjlnsrgi.append(matrix[rrjrhmqi][i])
            rrjrhmqi += 1
    
            for i in range(rrjrhmqi, fdllhqir+1):
                qjlnsrgi.append(matrix[i][rsmcemeb])
            rsmcemeb -= 1
    
            if rrjrhmqi <= fdllhqir:
                for i in range(rsmcemeb, ttsdedcu-1, -1):
                    qjlnsrgi.append(matrix[fdllhqir][i])
            fdllhqir -= 1
    
            if ttsdedcu <= rsmcemeb:
                for i in range(fdllhqir, rrjrhmqi-1, -1):
                    qjlnsrgi.append(matrix[i][ttsdedcu])
            ttsdedcu += 1
    
        return qjlnsrgi
    
    
def dfjkushm(pllqtpug, first, last):
    """ Quicksort
        Complexity: best O(n) avg O(n log(n)), worst O(N^2)
    """
    if first < last:
        qspmjrga = spapfkki(pllqtpug, first, last)
        print(pllqtpug[first:qspmjrga-1], pllqtpug[qspmjrga+1:last])
        dfjkushm(pllqtpug, first, qspmjrga-1)
        dfjkushm(pllqtpug, qspmjrga+1, last)


def dfsuutru(lines, name):
    """Write all lines to a file."""
    plisgpqq = open(name, 'w')
    for line in lines:
        plisgpqq.write(line)


if __name__ == '__main__':
    try:
        ddciefnp = docopt.docopt(__doc__)
        dhhejqtu = open(ddciefnp['FILE'][0])
        lucchnpb = ddciefnp['FILE'][0].split('/')[-1].split('.')[0]
        ppsthimd = ddciefnp['-o'] or lucchnpb + '_obfuscated.py'

        laemltti = []
        for line in dhhejqtu:
            laemltti.append(line)

        laemltti = rplnoiqt(laemltti)

        for idx, _ in enumerate(laemltti):
            laemltti[idx] = ehnmcnqd(laemltti[idx])
            laemltti[idx] = kcjrannp(laemltti[idx])
            laemltti[idx] = jbhdtqir(laemltti[idx])
            laemltti[idx] = rsjtekam(laemltti[idx])
            laemltti[idx] = jhacntel(laemltti[idx])

        dfsuutru(laemltti, ppsthimd)
    except docopt.DocoptExit as e:
        print e.message
