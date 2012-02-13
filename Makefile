
SUB_DIRS=base \
	static \
	templates \
	modules

MODULES=`ls modules/*/__init__.py | sed -e 's/modules\///g' -e 's/\/__init__.py//g'`

DEV_ENTRY_POINT=main.py

VIRTUAL_ENV=`which virtualenv`
VIRTUAL_ENV2=`which virtualenv2`
VIRTUAL_ENV_DIR=env

EASY_INSTALL=./$(VIRTUAL_ENV_DIR)/bin/easy_install
PYTHON=./$(VIRTUAL_ENV_DIR)/bin/python

PACKAGES= py-bcrypt \
	Flask \
	Flask-SQLAlchemy \
	Flask-WTF \
	Flask-SiJax \
	Flask-Bcrypt \
	Flask-Mail \
	Flask-Silk

CWD=`pwd`

all: setup setup-db app.wsgi

app.wsgi:
	echo "import sys, os\nos.chdir('$(CWD)/')\nactivate_this = os.getcwd() + '/env/bin/activate_this.py'\nexecfile(activate_this, dict(__file__=activate_this))\nsys.path.insert(0, os.getcwd())\nfrom main import base_app as application\n" >> app.wsgi


setup: 
	if ! [ -x $(VIRTUAL_ENV) ]; then \
		echo "Error: failed dependency Virtualenv"; \
		exit -1; \
	fi 
	$(VIRTUAL_ENV) $(VIRTUAL_ENV_DIR) 
	if ! [ -x $(EASY_INSTALL) ]; then \
		echo "Error: missing $(EASY_INSTALL) incomplete virutal enviornment"; \
	fi
	for pkg in $(PACKAGES); do \
		$(EASY_INSTALL) $$pkg; \
	done

setup-db: $(VIRTUAL_ENV_DIR)
	$(PYTHON) initial_setup.py --all

setup-modules: 
	for mod in $(MODULES); do \
		echo "==> Setting up models for $$mod"; \
		echo "from base import base_app\nimport modules.$$mod.models\nbase_app.db.create_all()\nquit()" | $(PYTHON); \
	done

devel-server: $(DEV_ENTRY_POINT)
	$(PYTHON) $(DEV_ENTRY_POINT)

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
.PHONY: count setup setup-db
.PHONY: clean
