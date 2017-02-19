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
    while(template_data.find("{if") != -1):
      t_start = template_data.find("{if")
      t_end = template_data.find("}",t_start)
      test = template_data[template_data.find("(", t_start)+1 : template_data.find(")", t_start)]
      name, value = test.split("==")
      if (vars[name] == value):
        replace_start = template_data.find("[", t_start)
        replace_end = template_data.find("]", t_start)
      else:
        replace_start = template_data.find("[", template_data.find("]", t_start))
        replace_end = template_data.find("]", replace_start)
      template_data = template_data[:t_start] + template_data[replace_start+1:replace_end] + template_data[t_end+1:]
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
