import sys
import subprocess

def template(file):
  while(file.find("<template>") != -1): # While there are still templates
    start = file.find("<template>")
    end = file.find("</template>")
    data = file[start+11:end] # Ignore template tags in data (11 is the length of <template>)
    vars = {}
    data = data.split("\n")
    name = data[0]
    if (name == "exec"): # If this an execute template
      template_data = subprocess.check_output("python ./Templates/"+data[1]+".py", shell=True)
    else:
      for i in xrange(1, len(data)-1):
        cur_row = data[i].split("=")
        vars[cur_row[0]] = cur_row[1]
      template_file = open("./Templates/"+name+".thtml", "r")
      template_data = template_file.read()
      for var_name in vars.keys(): # For every variable defined in the source file
        template_data = template_data.replace("{" + var_name + "}", vars[var_name])
      while(template_data.find("{if") != -1): # As long as there are if statements left
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
with open("./Sources/"+name+".shtml", "r") as file:
  source = file.read()

source = template(source)

with open(name+".html", "w") as file:
  file.write(source)
