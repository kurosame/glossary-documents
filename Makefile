RUN_FN_EMU = docker-compose up -d fn_emu
RUN_TF = docker-compose run --rm tf

fn-emu:
	${RUN_FN_EMU}

set-token:
	echo 'credentials "app.terraform.io" { token = "${TF_TOKEN}" }' > ./terraform/.terraformrc

init:
	${RUN_TF} init

plan:
	${RUN_TF} plan

apply:
	${RUN_TF} apply

apply-refresh:
	${RUN_TF} apply -refresh-only

fmt:
	${RUN_TF} fmt -recursive
