# install nginx and add custom header

exec { 'update':
  command => '/usr/bin/apt-get -y update',
  before  => Exec['install Nginx'],
}

exec { 'install Nginx':
  command => '/usr/bin/apt-get -y install nginx',
  before  => Exec['add_header'],
}

exec { 'add_header':
  command     => "/bin/sed -i 's/include \\/etc\\/nginx\\/sites-enabled\\/*;/include \\/etc\\/nginx\\/sites-enabled\\/*;\\n\\tadd_header X-Served-By \"\$HOSTNAME\";/' /etc/nginx/nginx.conf",
  environment => ['HOSTNAME=${hostname}'],
  before      => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  command => '/usr/sbin/service nginx restart',
}
