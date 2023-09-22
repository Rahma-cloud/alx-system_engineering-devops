#this is to install flask frpm pip3
package { 'python3-pip':
  ensure => installed,
}
exec { 'install flask':
  command    => '/usr/bin/pip3 install flask==2.1.0',
  path       => ['/usr/bin', '/usr/local/bin'],
  unless     => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
