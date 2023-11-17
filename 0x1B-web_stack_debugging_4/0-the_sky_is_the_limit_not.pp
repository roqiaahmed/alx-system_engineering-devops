# Increases the amount of traffic an Nginx server can handle.

exec { 'fix-ulimit':
    command => 'sed -i "s/15/4096/" /etc/default/nginx',
    path    => '/usr/local/bin/:/bin/',
}
service { 'nginx':
    ensure    => 'running',
    enable    => true,
    require   => Exec['fix-ulimit'],
}
