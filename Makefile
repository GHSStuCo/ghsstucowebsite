objects := $(patsubst ./Sources/%,%,$(patsubst %.shtml,%.html,$(wildcard ./Sources/*.shtml)))
all : $(objects)
%.html: ./Sources/%.shtml ./Templates/header.thtml
	python compile.py $@
