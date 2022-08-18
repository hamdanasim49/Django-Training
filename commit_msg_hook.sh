#!/usr/bin/env bash

# prevents overwriting if the file already exists
set -o noclobber

# creating a file named commit-msg in the .git/hooks directory
cat << EOF > .git/hooks/commit-msg
#!/usr/bin/env python

import sys, re

# reading the commit msg written by user
commit_msg_filepath = sys.argv[1]
with open(commit_msg_filepath, 'r') as f:
	content = f.read()

# checking if the commit msg follows the standard tintash commit msg format
commitRegex = re.compile (r'what:|why:|impact:', re.I)
found_list = commitRegex.findall(content)

# exits if the commit msg is not standardized and prints the error message
if len(found_list) != 3:
	print("ERROR: The commit message does not follow the required format")
	sys.exit(1)
EOF

chmod +x .git/hooks/commit-msg
