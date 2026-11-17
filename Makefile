.PHONY: help verify build check clean site preview site-check

help:
	@echo "make verify   conformance gate, including its own self-test"
	@echo "make build    regenerate indexes and discovery files"
	@echo "make check    everything CI runs, in the order CI runs it"
	@echo "make release  the release gate, in which deferrals count as failures"
	@echo "make preview  the private reading copy for gate B and C readers into _site/ (needs python-markdown)"
	@echo "make site     the production build into _site/, with the /id/ resolver (.htaccess)"

verify:
	python3 scripts/verify_public.py --self-test
	python3 scripts/verify_public.py

build:
	python3 scripts/build_indexes.py
	python3 scripts/gen_seo.py

check: verify
	python3 scripts/build_indexes.py --check
	python3 scripts/gen_seo.py --check

release:
	python3 scripts/verify_public.py --self-test
	python3 scripts/verify_public.py --strict
	python3 scripts/build_indexes.py --check
	python3 scripts/gen_seo.py --check

clean:
	rm -rf _site build dist .cache

preview:
	python3 scripts/build_site.py --preview

site:
	python3 scripts/build_site.py

site-check:
	python3 scripts/build_site.py --check
