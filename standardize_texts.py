from unidecode import unidecode

def read_text(infile):
    with open(infile,'r') as f:
        return f.read()

def standardize_text(text):
    """ remove newlines and arabic numerals """

    for ch in ['\t','\n','0','1','2','3','4','5','6','7','8','9']:
        text = text.replace(ch,' ')

    while '  ' in text:
        text = text.replace('  ',' ')

    text = unidecode(text)

    return text

def write_text(text,outfile):
    with open(outfile,'w') as f:
        f.write(text)

if __name__ == '__main__':
    infile = 'Library/allAPReadings.txt'
    outfile = 'ap_readings.txt'
    text = read_text(infile)
    text = standardize_text(text)
    write_text(text,outfile)
