import sys
import urllib2
import argparse

class scsi_op_dictionary:
    t10_op_url='http://www.t10.org/lists/op-num.txt'

    def __init__(self):
        self.op_txt_content = self.get_op_code_content()
        self.op_parser(self.op_txt_content)

    def get_op_code_content(self):
        req = urllib2.Request(scsi_op_dictionary.t10_op_url)
        response = urllib2.urlopen(req)
        the_page = response.read()
        return the_page

    def op_parser(self, op_txt_content):
        self.op_dict = {}
        self.attr_desc = ""
        lines = op_txt_content.splitlines()

        #Skill the commnet and get the attribute description
        op_block=False
        for line in lines:
            if op_block is False:
                if line[:3] == '   ':
                    self.attr_desc += line + '\n'
                elif line[:2] == "--":
                    op_block=True
            else:
                self.op_dict[line[:2]] = line

    def check_op_desc(self, op_code):
        if len(op_code) != 2 :
            print("Error OP code format: {!s}".format(op_code))
            return

        return self.op_dict.get(op_code.upper(), None)

    def show_attr_desc(self):
        print self.attr_desc

    def show_op_dict(self):
        print self.op_dict

    def show_txt_content(self):
        print self.op_txt_content

parser = argparse.ArgumentParser(description='Parsing SCSI Operation Code.')
parser.add_argument('cmd_codes', metavar='CMD', nargs='+',
                    help='Hex code for SCSI command')
parser.add_argument('-v', '--verbose', dest='verbose', action='count', default=0,
                    help='Show detail attribute')
args = parser.parse_args()

scsi_dict = scsi_op_dictionary()
if args.verbose is not 0:
    scsi_dict.show_attr_desc()

for cmd in args.cmd_codes:
    print scsi_dict.check_op_desc(cmd)


