objects := $(patsubst ./Sources/%,%,$(patsubst %.shtml,%.html,$(wildcard ./Sources/*.shtml)))
all : $(objects)
%.html: ./Sources/%.shtml ./Templates/header.thtml
	python compile.py $@
Members.html: ./Sources/Members.shtml ./Templates/header.thtml ./Templates/members.py ./Sources/members.txt ./Templates/member.thtml
	python compile.py $@