
MAKE=`which make`
LESSC=`which lessc`

SUB_DIRS=

DIST_CSS=main.layout.css \
	admin.css \
	news-posts.css \
	content.css \
	about-us.css \
	seminar.css

SRC=$(wildcard *.less jquery-ui/*.less)

all: $(DIST_CSS)
	cp *.css ../
	rm -rf *.css

%.css: %.less $(SRC)
	$(LESSC) -x $< > $(subst .,-,$(basename $@)).css

.SUFFIXES:
.SUFFIXES:	.py .conf .css .less .html .sh

count:
	wc *.less */*.less

clean:
	rm -rf *.css

.PHONY: all
.PHONY: count
.PHONY: clean
