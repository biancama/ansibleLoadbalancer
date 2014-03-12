# (c) 2014, Massimo Biancalani <massimo@info.nl>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

from lxml import etree
from io import StringIO
import json

class FilterModule(object):
    ''' Custom filters are loaded by FilterModule objects '''

    def filters(self):
        ''' FilterModule objects return a dict mapping filter names to
            filter functions. '''
        return {
            'parse_xml': self.parse_xml,
        }

    def parse_xml(self, value):
        xml_without_declaration = value[value.index("\r\n"):]
	f = StringIO(xml_without_declaration)
	tree = etree.parse(f)
	r = tree.xpath('/Response/Success/Data/Rs/Addr')	
	s = ""
	rng = len(r)	
	for i in range(rng):
		elem = r[i]
		if i == rng -1:
			s+=str(elem.text)
		else:
    			s+=str(elem.text+"\n")	
	return s	
	#l = []
	#for elem in r:
	#	l.append(elem.text)
	#return json.dumps(l)		
	#return xml_without_declaration

