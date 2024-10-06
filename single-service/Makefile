
VERSION := 0.0.1

reload: local-down docker local-up

local-up:
	docker-compose -f docker-compose.yml up -d

local-down:
	docker-compose -f docker-compose.yml down

docker:
	cd app && \
	docker build \
		-t loadtest-single-service-app:$(VERSION) \
		-t loadtest-single-service-app:latest \
		-f Dockerfile .

venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt
