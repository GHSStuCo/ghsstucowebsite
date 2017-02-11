import sys
def template(file):
  while(file.find("<template>") != -1):
    start = file.find("<template>")
    end = file.find("</template>")
    data = file[start+11:end]
    vars = {}
    data = data.split("\n")
    name = data[0]
    for i in xrange(1, len(data)-1):
      cur_row = data[i].split("=")
      vars[cur_row[0]] = cur_row[1]
    template_file = open("./Templates/"+name+".thtml", "r")
    template_data = template_file.read()
    for i in vars.keys():
      template_data = template_data.replace("{"+i+"}",vars[i])
    file = file[:start]+template_data+file[end+11:]
  return file

name = sys.argv[1].split(".")[0]
inputF = open("./Sources/"+name+".shtml", "r")
source = inputF.read()
inputF.close()
source = template(source)
#open("./Templates/"+sys.argv[1]+".thtml", "w")
outputF = open(name+".html", "w") 
outputF.write(source)
outputF.close()
