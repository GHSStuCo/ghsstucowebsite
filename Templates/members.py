import sys
output = ""
members = open("./Sources/members.txt", "r")
member_file = open("./Templates/member.thtml", "r")
member_base = member_file.read()
members_string = members.read()
members.close()
member_file.close()
members = members_string.split("\n")
line = 0
for member in xrange(0,len(members)):
  i = members[member]
  #print (member, i)
  #print("Member("+str(member)+", i[0]='"+i[0]+"'): "+i)
  if (i[0] != " "):
    if(i[0] == "*"):
      #print("Making table")
      output += "  </table>\n"
    elif(i[0] != "-"):
      output += """  <h1 class="membersh1" id="{id}">{title}</h1>
  <table>
""".replace("{id}",i.split("|")[1]).replace("{title}",i.split("|")[0])
  else:
    if (line == 0):
      cur_member = member_base[:]
      cur_member = cur_member.replace("{member}", i[1:])
    if (line == 1):
      cur_member = cur_member.replace("{title}", i[1:])
    if (line == 2):
      cur_member = cur_member.replace("{person}", i[1:])
    if (line == 3):
      cur_member = cur_member.replace("{bio}", i[1:])
      line = -1
      output += cur_member
    line += 1

print output
