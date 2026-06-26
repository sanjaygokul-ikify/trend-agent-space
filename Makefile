BINARY=agent-space
CLUSTER_SIZE=4

build: 	poetry build

run: 	export AGENT_SPACE_CLUSTER_SIZE=${CLUSTER_SIZE}; poetry run python agent_space/main.py

test: 	poetry run pytest --cov=agent_space

test-cluster: 	mkdir -p logs
	AGENT_SPACE_CLUSTER_SIZE=4 $(MAKE) test

fmt: 	poetry run black agent_space tests

lint: 	poetry run mypy agent_space
	$(MAKE) fmt