
MAKE=`which make`

SUB_DIRS=templates

all: 
	
.SUFFIXES:
.SUFFIXES:	.py .conf .css .less .html .sh

count:
	wc *.py *.conf

clean:
	if [ -d $(SUB_DIRS) ]; then \
		for subdir in $(SUB_DIRS); do \
			cd $$subdir && $(MAKE) clean && cd ..; \
		done \
	fi
	rm -f *.pyc *~

.PHONY: all
.PHONY: count
.PHONY: clean
