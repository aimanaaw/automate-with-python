import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume = '''Ebony Moore
Portland, OR • (123) 456-7891
cell: 508-555-5555, Home: 508-555-1234
emoore@email.com

SUMMARY
Skilled DevOps Engineer with 3+ years of hands-on experience supporting, automating, and optimizing mission critical deployments in AWS, leveraging configuration management, CI/CD, and DevOps processes.

EDUCATION
NORTHWEST VERMONT UNIVERSITY
Aug '12 - May '14
Bachelor of Science in Computer Information Systems

EXPERIENCE
TRADELOT, DevOps Engineer
Jun '16 - Current
Create and maintain fully automated CI/CD pipelines for code deployment using Octopus Deploy and PowerShell
Actively manage, improve, and monitor cloud infrastructure on AWS, EC2, S3, and RDS, including backups, patches, and scaling
Reduced costs by ~$3,000 each month by eliminating unnecessary servers and consolidating databases
Built and deployed Docker containers to break up monolithic app into microservices, improving developer workflow, increasing scalability, and optimizing speed
CLOUD CLEARWATER, DevOps Engineer
Current - Current
Wrote Puppet manifests and modules to deploy, configure, and manage servers
Automated build and deployment using Jenkins to reduce human error and speed up production processes
Reduced deployment time for critical agile project infrastructure from ~1 month to 2 days
Installed and configured Nagios to constantly monitor network bandwidth, memory usage, and hard drive status
Managed GitHub repositories and permissions, including branching and tagging
SKILLS
Configuration management using Puppet, Ansible, and Chef
Knowledge of Python, C/C++, and Java
Version control systems: Git, Subversion, and Perforce
'''
mo1 = phoneRegex.findall(resume)
# print(mo1)

phoneRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo2 = phoneRegex2.findall(resume)
# print(mo2)

phoneRegex3 = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
mo3 = phoneRegex3.findall(resume)
# print(mo3)


# \d is a character class for digits

lyrics = '12 drummers drumming, 11 pipers piping, 10 loads a leaping, 9 ladies dancing, 8 maids a milking'
xmasRegex = re.compile(r'\d+\s\w+')
mo4 = xmasRegex.findall(lyrics)
print(mo4)

vowelRegex = re.compile(r'[aeiouAEIOU]')  # r'(a|e|i|o|u') we can put in ranges too for example [a-z] or [A-F]
mo5 = vowelRegex.findall('Robocop eats babyfood')
print(mo5)

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
mo6 = doubleVowelRegex.findall('Robocop eats babyfood')
print(mo6)

# Negative character class. Every character that is not specified in the character class
consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo7 = consonantRegex.findall('Robocop eats babyfood')
print(mo7)