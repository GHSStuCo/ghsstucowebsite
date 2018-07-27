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
      for var_name in vars.keys(): # For every variable defined in the source (.shtml) file
        template_data = template_data.replace("{" + var_name + "}", vars[var_name])
      while(template_data.find("{if") != -1): # As long as there are if statements left
        if_start = template_data.find("{if")
        if_end = template_data.find("}",if_start)
        test = template_data[template_data.find("(", if_start)+1 : template_data.find(")", if_start)]
        name, value = test.split("==")
        if (vars[name] == value):
          replace_start = template_data.find("[", if_start)
          replace_end = template_data.find("]", if_start)
        else:
          replace_start = template_data.find("[", template_data.find("]", if_start))
          replace_end = template_data.find("]", replace_start)
        template_data = template_data[:if_start] + template_data[replace_start+1:replace_end] + template_data[if_end+1:]
    file = file[:start]+template_data+file[end+11:]
  return file

file_name = sys.argv[1].split(".")[0]

with open("./Sources/"+file_name+".shtml", "r") as input_file:
  with open(file_name+".html", "w") as output_file:
    output_file.write(template(input_file.read()))
