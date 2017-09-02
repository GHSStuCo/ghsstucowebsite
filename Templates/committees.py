import sys
from itertools import izip

def get_template(name, templates):
  name = "{%s}" % name
  start = templates.find(name)
  end = templates.find(name, start+1)
  return templates[start+len(name)+1:end-1]

def template_replace(template, keys, values):
  for key, value in izip(keys,values):
    template = template.replace(key, value)
  return template

with open("./Templates/committees.thtml", "r") as file:
  templates = file.read()

committee_template = get_template("committee_template", templates)
spacer = get_template("spacer", templates)
committees = []

with open("./Sources/committees.txt", "r") as file:
  members = []
  name = ""
  chair = ""
  for line in file:
    if(line[0] == "-"):
      members.sort(key = lambda a: a.split(" ")[1])
      committees.append(template_replace(committee_template, ["{name}", "{chair}", "{members}"], [name, chair, ", ".join(members)]))
    elif(line[0] == "*"):
      name,chair = line.strip().split("|")
      name = name[1:] # Remove initial * character
      members = []
    else:
      members.append(line.strip())

print spacer.join(committees)