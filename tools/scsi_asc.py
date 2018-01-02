import sys
import urllib2
import argparse

class scsi_asc_dictionary:
    t10_asc_url='http://www.t10.org/lists/asc-num.txt'

    def __init__(self):
        self.asc_txt_content = self.get_asc_code_content()
        self.asc_parser(self.asc_txt_content)

    def get_asc_code_content(self):
        req = urllib2.Request(scsi_asc_dictionary.t10_asc_url)
        response = urllib2.urlopen(req)
        the_page = response.read()
        return the_page

    def asc_parser(self, asc_txt_content):
        self.asc_dict = {}
        self.attr_desc = ""
        lines = asc_txt_content.splitlines()

        #Skill the commnet and get the attribute description
        asc_block=False
        for line in lines:
            if asc_block is False:
                if line[:9] == '         ':
                    self.attr_desc += line + '\n'
                elif line[:8] == "--------":
                    asc_block=True
            else:
                ascq_dict = self.asc_dict.setdefault(line[:2], {})
                ascq_dict[line[4:6]] = line

    def check_asc_desc(self, asc_code, ascq_code):
        if len(asc_code) != 2 or len(ascq_code) != 2 :
            print("Error asc code format: {!s}/{!s}".format(asc_code, ascq_code))
            return

        ascq_dict = self.asc_dict.get(asc_code.upper(), {})
        return ascq_dict.get(ascq_code.upper(), None)

    def show_attr_desc(self):
        print self.attr_desc

    def show_asc_dict(self):
        print self.asc_dict

    def show_txt_content(self):
        print self.asc_txt_content

parser = argparse.ArgumentParser(description='Parsing SCSI ASC/ASCQ Code.')
parser.add_argument('asc', metavar='ASC', nargs=1,
                    help='Hex code for SCSI ASC')
parser.add_argument('ascq', metavar='ASCQ', nargs=1,
                    help='Hex code for SCSI ASCQ')
parser.add_argument('-v', '--verbose', dest='verbose', action='count', default=0,
                    help='Show detail attribute')
args = parser.parse_args()

scsi_dict = scsi_asc_dictionary()
if args.verbose is not 0:
    scsi_dict.show_attr_desc()
print scsi_dict.check_asc_desc(args.asc[0], args.ascq[0])


