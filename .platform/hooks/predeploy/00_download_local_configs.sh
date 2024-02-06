#!/bin/bash
# PYTHONPATH='' aws s3 cp s3://hartsfield-deploy-configs/hartsfield/${EB_ENVIRONMENT}.py config/production-local.py
PYTHONPATH='' aws secretsmanager get-secret-value --secret-id hartsfield-${EB_ENVIRONMENT}.py --query 'SecretString' --output text > config/production-local.py
printf "\nEB_ENVIRONMENT = '${EB_ENVIRONMENT}'\n\n" >> config/production-local.py
chown webapp config/production-local.py
chmod 400 config/production-local.py
