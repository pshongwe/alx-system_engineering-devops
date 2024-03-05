# install nginx and add custom header

exec { 'update':
  provider => shell,
  command => 'sudo apt-get -y update',
  before  => Exec['install Nginx'],
}

exec { 'install Nginx':
  provider => shell,
  command => 'sudo apt-get -y install nginx',
  before  => Exec['add_header'],
}

exec { 'add_header':
  provider => shell,
  command     => "/bin/sed -i 's/include \\/etc\\/nginx\\/sites-enabled\\/*;/include \\/etc\\/nginx\\/sites-enabled\\/*;\\n\\tadd_header X-Served-By \"\$HN\";/' /etc/nginx/nginx.conf",
  environment => ['HN=${hostname}'],
  before      => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  provider => shell,
  command => 'sudo service nginx restart',
}
