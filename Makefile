PROJECT := atlas-starter

AWK  = awk
GREP = grep
SORT = sort
PR   = pr
CUT  = cut
GIT  = git
LN   = ln -s


# OS dependent variables
# darwin, linux, windows_nt
OS_NAME := $(shell uname -s | tr A-Z a-z)

TASKNAME = 'python*.*atlas*.*starter'
#TASKNAME = 'python*.*atlas'
ifeq ($(OS_NAME), linux)
    #$(info $(OS_NAME))
    STATAPP =  (pgrep -a -f  $(TASKNAME) ) || echo No active apps yet
    STATAPPc =  pgrep -f  $(TASKNAME)
    KILLAPP  =  pkill  -f $(TASKNAME)
else
    #$(info $(OS_NAME))
    STATAPP  =  (pgrep -lf -i $(TASKNAME) ) || echo No active apps yet
    STATAPPc =  pgrep -f -i $(TASKNAME)
    KILLAPP  =  pkill -i -f $(TASKNAME)
endif



# COLOR CODES
BLACK        := $(shell tput -Txterm setaf 0)
RED          := $(shell tput -Txterm setaf 1)
GREEN        := $(shell tput -Txterm setaf 2)
YELLOW       := $(shell tput -Txterm setaf 3)
LIGHTPURPLE  := $(shell tput -Txterm setaf 4)
PURPLE       := $(shell tput -Txterm setaf 5)
BLUE         := $(shell tput -Txterm setaf 6)
WHITE	     := $(shell tput -Txterm setaf 7)

RESET := $(shell tput -Txterm sgr0)


# Supported python versions, high to low
SUPPORTED_PYTHON_VERSIONS = python3.8 python38 python3.7 python37 python3.6 python36 python3.5 python35

# Take latest available version number
PYTHON_VERSION = $(firstword $(shell which $(SUPPORTED_PYTHON_VERSIONS)  2> /dev/null))

# If python version requirement is not met, exit.
ifeq ($(PYTHON_VERSION),)
  $(error Cannot find $(SUPPORTED_PYTHON_VERSIONS))
endif


BRANCH = $(shell $(GIT) branch | $(GREP) \* | $(AWK) '{print $2}')

MANAGE_PY = $(abspath ./manage.py)
DOCS	  = $(wildcard docs/*.md)
HTML	  = $(patsubst %.md, %.html, $(DOCS))

# SET HOSTNAME
HOSTN ?= geocadtek-dev-server
HOSTN := $(shell echo $${HOSTNAME\#*.})
MYSRV  = mijndatalab.nl

# SHELL and PYTHON ENVIRONMENTS
VENV                 	 = venv
export VIRTUAL_ENV  	:= $(abspath ${VENV})
export PATH		:= ${VIRTUAL_ENV}/bin:${PATH}

PYTHON = $(VIRTUAL_ENV)/bin/python

# CHOOSE PYTHON CONFIG file
ifeq (${HOSTN}, $(MYSRV))
        SETTINGS  = config_cloud
#        ENVFILE   = env_cloud.sh
else
	SETTINGS = config_local
#        ENVFILE  = env_local.sh
endif

MAKEFILE_LIST1 := $(MAKEFILE_LIST) # this is before any include

#EXPORTS=$(shell $(GREP) '^export' $(ENVFILE) | sed 's/"//g ; s/=/:=/ ; s/{\(.*\)}/(\1)/g ' )
#$(foreach line,$(EXPORTS),$(info --> $(line))) # debug
#$(foreach line,$(EXPORTS),$(eval $(line))) # works for multiple lines

# APPLICATION RUN MODE SETTINGS
#app-mode := Production
app-mode := DevelopmentConfig

#xport APP_SETTINGS := config.DevelopmentConfig
export APP_SETTINGS := $(SETTINGS).${app-mode}
#export PATH ?= /usr/pgsql-12/bin:${PATH}


SETTINGS_FILE   = $(SETTINGS).py

#
# PLEASE, DO NOT CHANGE ANYTHING BELOW.
#

# SCREEN INFO
$(info $(WHITE)Running service on host  : $(GREEN)$(HOSTN)$(RESET))
#$(info $(WHITE)Running with enviroment  : $(GREEN)$(ENVFILE)$(RESET))
$(info $(WHITE)Running with settings    : $(GREEN)$(SETTINGS_FILE)$(RESET))
$(info $(WHITE)Running application mode : $(GREEN)$(app-mode)$(RESET))
#$(info $(WHITE)Running with settings    : $(GREEN)$(shell echo $${HOSTNAME})$(RESET))

# default to list makefile targets
.DEFAULT_GOAL := ls

.PHONY: ls
ls:  ## list makefile targets, that is this list.
	@$(GREP) -E '^[a-zA-Z_-]+.*?:.*?## .*$$' $(MAKEFILE_LIST1) \
		| $(SORT) \
		| $(AWK) 'BEGIN {FS = ":.*?## "}; \
		{printf "${LIGHTPURPLE}%-30s${RESET} %s\n", $$1, $$2}'

help: ls


.PHONY: clean
clean: ## Delete the virtual environment, flask modules and unneccessary files
	##-rm requirements.txt
	-rm -rf venv
	-rm -rf migrations
	-rm -rf __pycache__
	-rm -rf db.sqlite
	-rm -rf install_reqs


.PHONY: all
all: ## Do a setup and run the service: e.g. git pull && install && db-init && db-migrate && run
all: $(SETTINGS_FILE) update install db-init db-migrate db-insert run

setup: all


${VENV}:
	$(PYTHON_VERSION) -m venv $@
	$(VENV)/bin/pip install --upgrade pip


install_reqs: requirements.txt | ${VENV}
	$(VENV)/bin/pip install --upgrade -r $<
	@touch $@

.PHONY: save-reqs
save-reqs: ## generate requirements.txt for the install # DEV step
		 $(VENV)/bin/pip freeze > requirements.txt


.PHONY: install
install:  ## Install module requirements into the virtual environment.
install: install_reqs | $(VENV)

.PHONY: db-init
db-init: ## initialize database tables: users and layers
db-init: $(SETTINGS_FILE) install | $(VENV)
	$(PYTHON) $(MANAGE_PY) db init

.PHONY: db-migrate
db-migrate: ## Run database table migrations and upgrades
#db-migrate: db-init
	$(PYTHON) $(MANAGE_PY) db migrate ; \
	$(PYTHON) $(MANAGE_PY) db upgrade

.PHONY: db-insert
db-insert: ## fill in tables users and layers in the database
db-insert: db-migrate sqlite_users_table.py sqlite_layers_table.py 
		$(PYTHON) sqlite_users_table.py
		$(PYTHON) sqlite_layers_table.py

.PHONY: showmigrations  
showmigrations: ## Show new db model migrations in edit mode
showmigrations: $(SETTINGS_FILE) install | $(VENV)  
	$(PYTHON) $(MANAGE_PY) db edit


.PHONY: shell
shell: ## Run flask shell.
shell: $(SETTINGS_FILE) install | $(VENV)
	$(PYTHON) $(MANAGE_PY) $@ $(SETTINGS_STRING)

.PHONY: deploy 
deploy: ## Do a complete deploy: e.g. git pull && install && db-migrate && restart supervisor.
#deploy: $(SETTINGS_FILE) update install db-init db-migrate db_insert restart
deploy: $(SETTINGS_FILE) update install db-migrate restart 


.PHONY: run
run:  ## Run our app on the server.
#run: $(MANAGE_PY) install | $(VENV)
run: $(MANAGE_PY) status | $(VENV)
	@#$(PYTHON) $(MANAGE_PY) runserver
	@nohup $(PYTHON) $(MANAGE_PY) runserver > atlas.log 2>&1 &
	@sleep 2
	@echo
	@- $(STATAPP)
	@echo
	@sleep 2
	cat atlas.log

.PHONY: restart
restart: # Restart app unix way
#restart: $(SETTINGS_FILE) $(MANAGE_PY) | $(VENV)
restart: $(SETTINGS_FILE) $(MANAGE_PY) status | $(VENV) 
	@- $(KILLAPP)
	@echo "${YELLOW}Re-starting the service.. ${RESET}"
	@nohup $(PYTHON) $(MANAGE_PY) runserver > atlas.log 2>&1 &
	@- $(STATAPP)
	@echo
	@sleep 2
	@cat atlas.log

#.PHONY: restart
#restart: ## Restart app service via supervisorctl
#restart: $(SETTINGS_FILE) 
#	supervisorctl restart $(PROJECT)
#

.PHONY: stop
stop: ## stop app
stop: status
	@echo
	@ $(STATAPPc) && \
	echo "${YELLOW}Do you want to stop the app? [y/n] ${RESET}" && \
	read input && [[ $${input} == "y" ]] && $(KILLAPP) && echo "${YELLOW}Stopping the service.. ${RESET}"  || echo Nothing to stop

.PHONY: status
status: ## Show status of running app
	@echo
	@-$(STATAPP)

.PHONY: test
test: ## Run the test
test: $(MANAGE_PY) install | $(VENV)  
	$(PYTHON) $(MANAGE_PY) runserver

# GIT related make targets
.PHONY: push
push: ## Do a git push, but run tests first. Not recommended on the server side.
push: .git test 
	$(GIT) status -b
	$(GIT) push -u origin $(BRANCH)

.PHONY: update
update: .git  ## Do a git pull. Update the current branch.
	$(GIT) pull

up: update


.PHONY: var
var: # list environmental variables
	@env


# vim:noexpandtab:ts=8:sw=8:ai
