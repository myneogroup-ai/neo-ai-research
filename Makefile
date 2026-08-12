.PHONY: help verify build check clean

help:
	@echo "make verify   conformance gate, including its own self-test"
	@echo "make build    regenerate indexes and discovery files"
	@echo "make check    everything CI runs, in the order CI runs it"
	@echo "make release  the release gate, in which deferrals count as failures"

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
