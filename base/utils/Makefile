
MAKE=`which make`

SUB_DIRS=

all: 
	
.SUFFIXES:
.SUFFIXES:	.py .conf .css .less .html .sh

count:
	wc *.py *.conf

clean:
	for subdir in $(SUB_DIRS); do \
		cd $$subdir && $(MAKE) clean  && cd ..; \
	done
	rm -f *.pyc *~

.PHONY: all
.PHONY: count
.PHONY: clean
