import os, sys
from fabric.api import env, run, cd, local, settings, abort
from fabric.contrib.console import confirm
from fabric.colors import red, green

if os.path.exists('shopkeeper1.pem'):
	env.user = 'ubuntu'
	env.key_filename = os.getenv('TEST_PROD', 'shopkeeper1.pem')
else:
	env.use_ssh_config = True

roles = {
	'master': ['65.0.130.220',]
}

env.roledefs = roles
code_dir_master = '/home/ubuntu/main/shopkeeper'

def production():
	env.hosts = roles['master']
	if os.path.exists('shopkeeper1.pem'):
		print('pem file exists')
		env.user = 'ubuntu'
		env.key_filename = 'shopkeeper1.pem'
	env.code_dir = code_dir_master


def deploy():
	if env.host_string in roles['master']:
		print(green('found host string'))
		with cd(env.code_dir):
			print(green("Pulling"))
			run("git pull origin master")

	else:
		print('no host string found')

