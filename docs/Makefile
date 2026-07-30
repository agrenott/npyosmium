PYTHON ?= python3
PYTHON_BINDIR=$(abspath $(dir $(PYTHON)))
ARGPARSE_MANPAGE ?= argparse-manpage
ARGPARSE_BASEARGS=--author 'Sarah Hoffmann and Aurélien Grenotton' --author-email 'agrenott@gmail.com' --project-name npyosmium --url https://github.com/agrenott/npyosmium/
PYOSMIUM_VERSION=$(shell PATH='$(PYTHON_BINDIR):'$$PATH $(PYTHON) -c 'import npyosmium.version;print(npyosmium.version.npyosmium_release)' | tail -n 1)

man:
	mkdir -p man
	PATH='$(PYTHON_BINDIR):'$$PATH $(ARGPARSE_MANPAGE) --module npyosmium.tools.pyosmium_get_changes --version '${PYOSMIUM_VERSION}' --function get_arg_parser ${ARGPARSE_BASEARGS} --output man/pyosmium-get-changes.1
	PATH='$(PYTHON_BINDIR):'$$PATH $(ARGPARSE_MANPAGE) --module npyosmium.tools.pyosmium_up_to_date --version '${PYOSMIUM_VERSION}' --function get_arg_parser ${ARGPARSE_BASEARGS} --output man/pyosmium-up-to-date.1

.PHONY: man
